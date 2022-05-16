pipeline{
    agent any
    stages {
        stage('Testing app'){
            steps{
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            steps {

               sh "ln -s QA-Project-2/docker-compose.yaml building"
            }
        }
    }
}
