from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import TemplateHTMLRenderer

from drf_spectacular.utils import extend_schema

from common.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)
from common.api.mixins import APIErrorsMixin

from .models import Contact
from .selectors import (
    email_list,
    get_contact_by_email,
    get_email_statistic,
)
from .services import create_contact

from django.contrib.humanize.templatetags import humanize

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    status = serializers.CharField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = "__all__"
    
    def get_created_at(self, obj):
        return humanize.naturaltime(obj.created_at)

class CreateContactAPIView(APIView):
    class CreateContactRequestSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=254)

    @extend_schema(request=CreateContactRequestSerializer, responses=ContactSerializer)
    def post(self, request):
        serializer = self.CreateContactRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        email_check = get_contact_by_email(email=cleaned_data["email"])
        if email_check:
            raise ValidationError("duplicate email")

        contact = create_contact(**cleaned_data)
        data = ContactSerializer(contact).data
        return Response(data, status=201)

class ListContactView(APIErrorsMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'email_list.html'

    class Pagination(LimitOffsetPagination):
        default_limit = 50
        max_limit = 100

    def get(self, request):
        contacts = email_list()
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=ContactSerializer,
            data={
                "queryset": contacts,
                "statistic": get_email_statistic(),
            },
            request=request,
            view=self,
        )

class ContactInfoView(APIErrorsMixin, APIView):
    def get(self, request):
        response = get_email_statistic()
        return Response(response)
