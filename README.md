# djangoproject
## 1 . I am using conda base env.
## 2. Install the django package.
    pip install django==3.2.9
    pip install djangorestframework==3.12.4
    pip install uritemplate==4.1.1 # must be installed for OpenAPI schema support.(swagger)
## 3. After the installation completed, make a new django project.
    django-admin startproject simpleprofile
## 4. The project is made by Django. Now, the last command is to make a new application. Move to the directory of manage.py file and make a new app.
    python manage.py startapp profiles
## 5. To run project:
    python manage.py runserver 8080

## 6. for more details: https://docs.djangoproject.com/en/3.2/intro/tutorial01/

## 7. Every after change models.py you need to make migrations into db.sqlite3 (database) to create the table for the new model. run bellow command:
    python manage.py makemigrations 
    python manage.py migrate

## 8. creating superuser (user/pass: admin/admin, Email address: admin@gmail.com):
    python manage.py createsuperuser
## 8. Create the views to create profiles app pages on browser, the file is profiles/views.py according the model class structure.

## 9.Sometimes, we'll need to update our database tables. Normally we'd create a database migration in order to do that, let's just delete the database and start again.

rm -f db.sqlite3
rm -r profiles/migrations
python manage.py makemigrations profiles
python manage.py migrate


## 10. End points url:
    Use below url in Postman(set appropriate request method[GET,POST,DELETE,PUT])
    GET api:
    http://127.0.0.1:8080/openapi   (This list out all urls signature)
    
    http://127.0.0.1:8080/profiles/newapi/profile_all/

    http://127.0.0.1:8080/profiles/newapi/profile_detail/{id}
    Ex.http://127.0.0.1:8080/profiles/newapi/profile_detail/1
   
    POST api:
    http://127.0.0.1:8080/profiles/newapi/profile_create    (send data as JSON)
    ex. {
        "firstName": "Lucky",
        "lastName": "Nikola",
        "dob": "2021-10-25",
        "email": "Lucky650@gmail.com",
        "mobileNumber": "+917453265650",
        "password": "faUgi[12]"
        }
    PUT api:
    http://127.0.0.1:8080/profiles/newapi/profile_update/{id}  (send data as JSON)
    ex. http://127.0.0.1:8080/profiles/newapi/profile_update/1
    {
        "firstName": "Lucky",
        "lastName": "Nikola Gani",
        "dob": "2021-10-30",
        "email": "Lucky655@gmail.com",
        "mobileNumber": "+917453265655",
        "password": "fauGi[12]"
        }

    DELETE api:
    http://127.0.0.1:8080/profiles/newapi/profile_delete/{id}
    ex.http://127.0.0.1:8080/profiles/newapi/profile_delete/1
