************************************** Task Management Application Documentation ****************************************************
Overview:

The Task Management Application is a web-based tool developed using the Django framework, designed to help users manage their tasks efficiently. The application allows users to perform key actions such as creating, updating, deleting, and viewing tasks. The backend is powered by Django, and the frontend can be built using HTML, CSS, and JavaScript or any modern front-end framework.

--This documentation provides an overview of the application features, architecture, and guides for setting up and using the application.

Key Features
1.User Authentication:

-Users can register, log in, and log out.
-Password management and secure authentication are handled by Django’s authentication system.

2.Task Creation & Management:

Users can create new tasks, specifying details such as title, description, due date, and priority.
Tasks can be marked as completed or in progress.

3.Task Editing:

Users can edit the details of existing tasks.

4.Task Deletion:

Users can delete tasks they no longer need.

5.Responsive Design:

The application is designed to be responsive, ensuring a smooth user experience on both mobile and desktop devices.

******Logging & Monitoring*********

The system implements logging for tracking important actions and errors.
Metrics for API response times and error rates can be collected and visualized.

*************************************************** SystemArchitecture *****************************************************************

1. Frontend:
-HTML/CSS/JavaScript used
-The frontend communicates with the backend using API endpoints.

2. Backend:
-The backend is built using Django, a high-level Python web framework.
-MySQL is used as the database to store task information, user data, and other related entities.

3. Database:
MySQL Database: Stores all the tasks, user details, and related entities.

-Tables:
 -users: Stores user authentication information.
-tasks: Stores task-related details such as title, description, due date, and status.

4. Deployment:
-The application  containerized using Docker for simplified deployment.
-Jenkins or other CI/CD tools used for continuous integration and deployment.
-Monitoring with Prometheus and Grafana is implemented for real-time performance and error tracking.

************************************** SetupInstruction*********************************************************************************

Prerequisites=
--Python 3.x
--Django 3.x or higher
--MySQL Database (here I used RDS service )
--Docker (for containerized deployment)

****************************************************************************************************************************************
--Installation SetUp

git clone https://github.com/seemaumadi/Task-management
cd Task-management
virtualenv venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
--- enter name, - enter email and password
python manage.py runserver

access the application
for admin page use (/admin)

If you face error 500 then go to setting.py file DEBUG = True //set debug true (its for developer environment)

***************************************************************************************************************************************