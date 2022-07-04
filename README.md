# Django Rest Framework First Project
This app is realized GET, POST and DELETE methods of API using Django-Rest-Framework

###[Link to deployed project](https://heroku-courses-api-app.herokuapp.com/api/v1/courses/)

Getting Started
----
[Create Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

Go to the directory where the requirements.txt and in the terminal enter this:
```bash
pip install -r requirements.txt
```


Lets run our localhost server:  
```bash
python manage.py runserver
```

So, you are ready to start work with my app!

Example
----

Use [postman](https://www.postman.com/downloads/) to work with API's, if you will use postman first time, read [postman docs](https://learning.postman.com/docs/getting-started/sending-the-first-request/)


## POST 

create new post

For create new course use `post`, paste this link `http://127.0.0.1:8000/api/v1/courses/`

On body select json and write this (you can change data if you want :) )
```json
    {
        "id": 1,
        "name": "CodeMind",
        "description": "be powerfull coder",
        "category": {
            "name": "Programming",
            "imgpath": "/media/"
        },
        "logo": "logo.png",
        "contact": [
            {
                "suit": 3,
                "value": "codem1nd@course.com"
            }
        ],
        "branch": [
            {
                "latitude": "1",
                "longitude": "3",
                "address": "code street 101"
            }
        ]
    }
```
and click ```send```
After this this data will be saved on database
> create 2-3 courses, we will work with them

## Get Courses List

For get list of courses use ```get``` method on postman, paste this link ```http://127.0.0.1:8000/api/v1/courses/``` and click ```send```

You will see all datas

## GET 

get course by id

For get specific course use ```get``` method on postman, paste this link ```http://127.0.0.1:8000/api/v1/courses/{your_id}/``` and click ```send```

you will see couse with ID that you paste on `/{your_id}/` previos link

## DELETE
delete specific course

For delete specific course use ```delete``` method on postman, paste this link ```http://127.0.0.1:8000/api/v1/courses/{your_id}/``` and click ```send```
You will see 
```json 
"object with id: 2 has been deleted"
```
#### be  mega sure that after id you put `/` in the end

## Built With
[Django](https://www.djangoproject.com/) - web framework

[Django rest framework](https://www.django-rest-framework.org/) - toolkit for building Web APIs
