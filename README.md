Documentation: Setting Up a Django Application Locally
1. Prerequisites
Before setting up the Django application locally, make sure you have the following installed:

Python (version 3.8+ recommended)
pip (Python package manager)
Git (for cloning the repository)
MySQL database 


2. Clone the Repository
First, clone the repository from GitHub.

git clone https://github.com/seemaumadi/Task-management.git
cd Task-management

3/Set Up a Virtual Environment 
Creating a virtual environment helps isolate your Python environment for the project.

# Install virtualenv if you haven't
pip install virtualenv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/MacOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate

4. Install Project Dependencies
After activating the virtual environment, install the dependencies from the requirements.txt file:

pip install -r requirements.txt

5.Run Migrations
Run Django’s database migrations to create the necessary tables:

python manage.py migrate

6.Create a Superuser 
Create a superuser to access the Django admin interface:

python manage.py createsuperuser

Follow the prompts to create the admin user.

7.Run the Development Server
Start the Django development server locally:

python manage.py runserver
By default, the application will run on http://127.0.0.1:8000/. Open this in your web browser to view the application.

8. Access the Django Admin Interface
You can access the Django admin interface at:

http://127.0.0.1:8000/admin/
Log in using the superuser credentials you created earlier.
