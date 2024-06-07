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

> [!NOTE]
> You can use ``` pip freeze > requirements.txt ``` to install the req pkgs mentioned in the requirements file
