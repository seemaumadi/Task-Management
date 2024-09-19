pipeline {
    agent any
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        
        stage('clean workspace'){
            steps{
                cleanWs()
            }
        }
        stage('Checkout Code') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main',
                    url: 'https://github.com/seemaumadi/Task-management.git'
            }
        }
        stage("Sonarqube Analysis") {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=django \
                    -Dsonar.projectKey=django'''
                }
            }
        }

       stage('Docker Compose Build') {
            steps {
                script {
                    // Build Docker images using Docker Compose
                    sh 'docker-compose -f docker-compose.yml build'
                    
                    // List Docker images to confirm the build
                    sh 'docker images'
                    sh 'display image'
                }
            }
        }
        
        stage('Docker Compose Push') {
            steps {
                script {
                    // Log in to Docker registry
                    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
                        // Push Docker images to registry using Docker Compose
                        sh 'docker-compose -f docker-compose.yml push'
                    }
                }
            }
        }
        stage('Run Migrations') {
            steps {
                script {
                    // Run Django database migrations
                    sh 'docker-compose -f docker-compose.yml run --rm app python manage.py migrate'
                }
            }
        }
        stage('Collect Static Files') {
            steps {
                script {
                    // Collect Django static files
                    sh 'docker-compose -f docker-compose.yml run --rm app python manage.py collectstatic --noinput'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                
                    sh 'docker-compose -f docker-compose.yml down'
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }

    }
    
}
