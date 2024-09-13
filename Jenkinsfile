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

        
       stage('Docker Compose Build and Tag') {
            steps {
                script {
                    // Define image name and tags
                    def imageName = 'seema24/web-app'
                    def buildTag = 'latest'  // Default tag for the build
                    def newTag = 'v1.0.0'    // New tag you want to assign

                    // Build Docker images using Docker Compose
                    sh 'docker-compose -f docker-compose.yml build'

                    // Tag Docker images with the specified tags
                    // Tagging assumes that the image was built with the 'latest' tag
                    sh """
                    docker tag ${imageName}:${buildTag} ${imageName}:${newTag}
                    """
                }
            }
        }
        stage('Docker Compose Push') {
            steps {
                script {
                    // Log in to Docker registry
                    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
                        // Push the tagged image to Docker Hub
                        sh """
                        docker push seema24/web-app:v1.0.0
                        """
                    }
                }
            }
        }
    }
    
}
