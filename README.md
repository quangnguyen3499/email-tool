## Owner: Quang Nguyen

Please follow this step for usage

### Introduction
This is a tool written in Python with Django used to collect email from customer for commercial purpose. There's a cron job run every Monday and Wednesday to send email statistics to shop owner.
Please follow installation to set up and run this tool.

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
