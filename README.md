# Auth Service

**Authentication and authorization Service**

Swagger documentation: [http://localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/)

Admin: [http://localhost:8000/lbhr5Q2NPWNizVb/](http://localhost:8000/lbhr5Q2NPWNizVb/)

### Requirements
- Python (3.7)
- Django (2.2)
- Django REST Framework (3.9)

### Installation - Docker

```
git clone git@github.com:mridulsust/auth-service.git
cd auth-service

docker-compose -f local.yml build
docker-compose -f local.yml up
```

### Run Test

```
sudo docker-compose -f local.yml run django python manage.py test
```

## Built With

* [Python 3.7](https://docs.python.org/3.7/) - Python version 3.7
* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](http://www.django-rest-framework.org/) - Used to generate RESTful API
