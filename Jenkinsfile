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
                sh "docker-compose build --parallel"
                //sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
               // sh "ln -s QA-Project-2/docker-compose.yaml building"
                //sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }

    }
    

}
