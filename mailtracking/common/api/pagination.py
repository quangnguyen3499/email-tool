from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination as _LimitOffsetPagination
from rest_framework.response import Response


def get_paginated_response(
    *, pagination_class, serializer_class, data, request, view
):
    paginator = pagination_class()

    page = paginator.paginate_queryset(data["queryset"], request, view=view)

    if page is not None:
        serializer = serializer_class(page, many=True)
        return paginator.get_paginated_response({
            "queryset": serializer.data,
            "new_this_month": data["new_this_month"],
            "unsubscribed": data["unsubscribed"],
        })

    serializer = serializer_class(data, many=True)

    return Response(data=serializer.data)


class LimitOffsetPagination(_LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_data(self, data):
        return OrderedDict(
            [
                ("limit", self.limit),
                ("offset", self.offset),
                ("count", self.count),
                ("next", self.get_next_link()),
                ("previous", self.get_previous_link()),
                ("results", data),
            ]
        )

    def get_paginated_response(self, data):
        """
        We redefine this method in order to return `limit` and `offset`.
        This is used by the frontend to construct the pagination itself.
        """
        return Response(
            OrderedDict(
                [
                    ("limit", self.limit),
                    ("offset", self.offset),
                    ("count", self.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("new_this_month", data["new_this_month"]),
                    ("unsubscribed", data["unsubscribed"]),
                    ("results", data["queryset"]),
                ]
            )
        )
