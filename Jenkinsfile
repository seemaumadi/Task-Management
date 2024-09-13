pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main',
                    url: 'https://github.com/seemaumadi/Task-management.git'
            }
        }

        stage('Install System Dependencies') {
            steps {
                sh 'apt-get update && apt-get install -y pkg-config libmariadb-dev-compat libmariadb-dev'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Migrations') {
            steps {
                // Activate virtual environment and run migrations
                sh '''
                    . venv/bin/activate
                    python manage.py migrate
                '''
            }
        }
        stage('Collect Static Files') {
            steps {
                // Activate virtual environment and run collectstatic
                sh '''
                    . venv/bin/activate
                    python manage.py collectstatic --noinput
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t webapp:latest .
                '''
            }
        }
    }
}
