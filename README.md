# trafficking-grader

Human-Trafficking Training Grade Database

## Setup

1. Ensure you have the latest version of Python 3: https://www.python.org/downloads/
2. Set up virtual environment: https://dev.to/kachiic/how-to-clone-a-django-project-from-github-and-run-it-locally-mac-ios-2o4k
    (*This link may be better: https://www.w3schools.com/django/django_create_virtual_environment.php#:~:text=It%20is%20suggested%20to%20have,we%20will%20call%20it%20myworld%20.*)
3. Ensure you have the latest version of Python 3: https://www.python.org/downloads/
4. Pull git project into your IDE (Suggested - Visual Studio Code)
– VS code  download - https://code.visualstudio.com/download
5. Complete the migration of the database tables to be in sync with our models. (run this when setting up the project)
```bash
pip install -r requirements.txt
python manage.py makemigrations
```
6. finish migrating the data
```bash
python manage.py migrate
```
7. create a super user
```bash
python manage.py createsuperuser
```
8. Populate database
```bash
python manage.py populate_database py
```
9. Run the project with:
```bash
python manage.py runserver
```
10. Look at you! You ran the project (yay) - very cool


Note: Create a FORK of the repository, then clone your fork on your local machine - You will create pull requests with your changes as opposed to updating the repository directly unless it's a small change (i.e. implementing a large feature vs updating ReadME or adding code comments). 
This will allow others a chance to approve changes! 

Any collaborator may merge a PR afer confirming the code works.

Be sure to update your fork regularly :)
