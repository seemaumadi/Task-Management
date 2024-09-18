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
                }
            }
        }
        stage('Tag Docker Image') {
            steps {
                script {
                    // Use the actual image name and tag from the build output
                    
                    def newImageRepo = 'seema24/web-app'
                    def newImageTag = 'latest'
                    def newTag = 'v1.0.0'
                    
                    // Tag the Docker image
                    sh "docker tag ${newImageRepo}:${newImageTag} ${newImageRepo}:${newTag}"
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
        //stage('Run Tests') {
            //steps {
                //script {
                    // Run Django tests
                    //sh 'docker-compose -f docker-compose.yml run --rm app python manage.py test'
                //}
            //}
        //}
        stage('Deploy') {
            steps {
                script {
                    // Deploy application (e.g., pull new images and restart containers)
                    // This will depend on your deployment strategy, such as using Docker Compose to restart the stack
                    sh 'docker-compose -f docker-compose.yml down'
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }

    }
    
}
