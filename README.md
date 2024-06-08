<div align="center">
   <h1>Social Networking</h1>
   <img src="https://github.com/anjali0719/networking-site/assets/169834149/4ff0bd38-f58d-4261-a4e1-b4ba08906f09">
</div>

A place where you can make friends.

## Usage
1. Anyone can register using their email and password
2. User can Login using the credentials
3. Once you're successfully logged in, you can:
   1. Send friend request to other users
   2. Search users by their email / first name
   3. Get your list of friends
   4. Get the list of friend request you've received so far
   
> [!NOTE]
> In a minute you can send upto 3 friend requests only!

## Requirements
 * Python: 3.12
 * Django: 5.0

## Installation Steps
1. Make sure you've Python & Pip
```sh
python --version
pip --version
```
```sh
pip install pip
```
2. Install Pipenv (A pkg manager for python application, pipenv lets you easily create virtual env for your projects without conflicting with other versions of the same pkgs used by other projects)
```sh
pip install pipenv
```
3. Activate Virtual Env (Incase if you don't have, it'll create one for you)
```sh
pipenv shell
```
4. Install Django & DjangoRestFramework
```sh
pipenv install django
pipenv install djangorestframework
```
5. For authentication: Install JWT (JSON Web Token)
```sh
pip install djangorestframework-simplejwt
```
6. Install Django Filters
```sh
pip install django-filter
```
7. Generate necessary migration files
```sh
python manage.py makemigrations
python manage.py migrate
```
8. Create superuser to access django admin panel ``` http://localhost:8000/admin/ ``` or ``` http://127.0.0.1:8000/admin/ ```
```sh
python manage.py createsuperuser
```

> [!NOTE]
> You can use ``` pip freeze -r requirements.txt ``` to install the req pkgs mentioned in the requirements file

## Postman Collection
1. Register User (SignUp API):
   * API Endpoint: http://127.0.0.1:8000/sign-up/
   * Method: POST
   * Authention: No Auth (since anyone can signup)
   * Body:
         {
          "email": "abctest123@gmail.com",
          "password": "abctest123"
         }

2. Login User (this API returns you the access token which can be used to call other APIs which requires authentication):
   > NOTE: Copy the `access` from the response
   * API Endpoint: http://127.0.0.1:8000/login/
   * Method: POST
   * Authentication: No Auth
   * Body:
        {
             "email": "abctest123@gmail.com",
             "password": "abctest123"
        }
     
4. Search User:
   * API Endpoint: http://127.0.0.1:8000/search-user/?search=test123&limit=15&offset=0
   * Method: GET
   * Authentication: Bearer Token (paste the access token received from login api response)
   * Query Params:
     search, limit, offset

5. Send Friend Request:
   * API Endpoint: http://127.0.0.1:8000/friend-request/
   * Method: POST
   * Authentication: Bearer Token (paste the access token received from login api response)
   * Body:
        {
          "to_user_uuid": "6b12bca5-416a-3399-b689-8f5d995251b7"
        }
     (uuid of the user to whom you want to send request)
     
6. Accept or Reject Friend Request:
   * API Endpoint: http://127.0.0.1:8000/friend-request/72b4dcdd-7d63-35f7-ac99-70e0e098fbb6/
     (send the UUID of the Friend Request Obj which you want to update)
   * Method: PUT
   * Authentication: Bearer Token (paste the access token received from login api response)
   * Body:
        {
          "status": "accepted"
        }
     (send the status as `accepted` or `rejected`)
     
7. Get the Friend List of logged in user:
   * API Endpoint: http://127.0.0.1:8000/friend-request/friends-list/?limit=15&offset=0
   * Method: GET
   * Authentication: Bearer Token (paste the access token received from login api response)

8. Get the List of Pending Requests:
   * API Endpoint: http://127.0.0.1:8000/friend-request/received-list/?limit=15&offset=0
   * Method: GET
   * Authentication: Bearer Token (paste the access token received from login api response)

## Refer To 🎥

https://github.com/anjali0719/networking-site/assets/169834149/0c0f90aa-16cd-4197-a072-f6c23b9a597f

