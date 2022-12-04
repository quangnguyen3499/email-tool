## Owner: Quang Nguyen

Please follow this step for usage

### Installation:

- docker
- docker-compose

### How to run:
```
cd <project_path>/mailtracking
import backup file database.bak
create file local.env, copy content from local.env.example and modify it (including SELLER_MAIL)
docker-compose up --build
```

3 app will be running:
- database (postgres)
- web (django)
- rabbitmq (queue)

### Document:
- list contacts page: http://{DOMAIN}:8000/api/v1/contacts/list/
- add contact api: http://{DOMAIN}:8000/api/v1/contacts/
- download schema: http://{DOMAIN}:8000/api/schema/
- swagger doc: http://{DOMAIN}:8000/api/schema/swagger-ui/
- cron job console in terminal and send email to seller (SELLER_MAIL in settings.py) every Monday & Wednesday

DOMAIN = localhost (local) 
         ... (production) -> reopen in the future
         
I have manually deployed the project to EC2 to use it public.
