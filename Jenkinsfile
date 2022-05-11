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
                //sh "ln -s DevOps-Project2/docker-compose.yaml build" 
                sh "sudo docker-compose build --parallel"
               // sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "sudo docker-compose push"
            }
        }
    }
}
