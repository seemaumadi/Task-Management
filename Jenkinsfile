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

        
       stage('Docker Compose Build') {
            steps {
                script {
                    // Build Docker images using Docker Compose
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
    }
}
