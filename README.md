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


