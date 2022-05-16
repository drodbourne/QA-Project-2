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
               //sh "ln -s QA-Project-2/docker-compose.yaml building"
                sh "docker-compose push"
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
    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'front-end/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'name-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'unit-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'effect-api/coverage.xml', failNoReports: false
        }
    }

}
