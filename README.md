<h1 align='center'><img src='https://user-images.githubusercontent.com/88055229/167256181-daa5f692-1b94-436f-8f14-230a9fa3de57.png' /></h1>

<h2 align='center'>App about Supports and Users</h2> 

### About project:
This is an educational project.
However, in the future it may become a full-fledged technical support service, 
where the user can ask a question of interest to him on any topic, 
and the support team will promptly solve the user's problem


### Development tools

**Stack:**
- Python >= 3.10.4
- Django >= 4
- PostgreSQL
- Django Rest Framework
- Celery
- Docker


## Getting started

##### 1) Clone repository

    git clone link_generated_in_your_repository

##### 2) Build and up docker containers

    docker-compose build
    docker-compose up
    
##### 3) Create superuser

    docker-compose exec bweb python manage.py createsuperuser
    
    
## Project configurations

##### Use the .env file to set up the project

    DEBUG = True or Fale  (Debug mode)
    SECRET_KEY = 'very_reliable_secret_key'
    DJANGO_ALLOWED_HOSTS = (some_allowed_hosts, )


###### DB credentials

    DB_NAME = data_base_name
    DB_USER = data_base_name
    DB_PASS = data_base_password
    DB_SERVICE = service name from docker-compose.yml
    DB_PORT = data_base_port


###### smtp credentials

    SMTP_EMAIL_USE_TLS = True or False                   TLS and SSL is certificates protecting user information from intruders.
    SMTP_EMAIL_USE_SSL = True or False                   Can be only SSL or TLS, rather TLS. 
    SMTP_EMAIL_HOST = 'smtp.gmail.com'
    SMTP_EMAIL_HOST_USER = 'email_for_sendind_messages'
    SMTP_EMAIL_HOST_PASSWORD = 'email_password'
    SMTP_EMAIL_PORT = email_port


###### Celery & Redis

    REDIS_HOST='redis'
    REDIS_PORT='6379'
    CELERY_BROKER_URL='redis://redis:6379/0'
    CELERY_RESULT_BACKEND='redis://redis:6379/0'
    CELERY_TASK_SERIALIZER = some data format
    CELERY_RESULT_SERIALIZER = json'some data format

###### CORS

    CORS_ALLOW_ALL_ORIGINS= True or False (enable disable CORS for certain urls)

