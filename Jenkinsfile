pipeline {
    agent any
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
                    def oldImageRepo = 'application'
                    def oldImageTag = 'django'
                    def newImageRepo = 'seema24/web-app'
                    def newTag = 'latest'
                    
                    // Tag the Docker image
                    sh "docker tag ${oldImageRepo}:${oldImageTag} ${newImageRepo}:${newTag}"
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
    }
    
}
