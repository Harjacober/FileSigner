pipeline {
    agent any { docker { image 'python:3.7.5' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Hello there, this is my first jenkins script"'
            }
        }
    }
    post {
        always {
            sh 'echo "I ensured this run always"'
        }
        success {
            sh 'echo "Yess, I made this pass"'
        }
        failure {
            sh 'echo "it is my fault this failed"'
        }
    }
}
