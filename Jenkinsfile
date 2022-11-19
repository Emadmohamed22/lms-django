pipeline{
    agent {
        docker {image 'python:3.8-slim'}
    }

    stages{
        stage("install dependencies"){
            steps{
                sh'pip3 install - r requirements.txt'
                echo "installation done"
            }
        }
       stage("migrate"){
            steps{
                sh'python3 manage.py makemigrations'
                sh'python3 manage.py migrate'
                echo "migration done"
            }
        }
    }
}
