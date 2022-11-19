pipeline{
    agent {
        docker {image 'python:3.8-slim'}
    }

    stages{
        stage("install dependencies"){
            steps{
                sh'pip install - r requirements.txt'
                echo "installation done"
            }
        }
       stage("migrate"){
            steps{
                sh'python manage.py makemigrations'
                sh'python manage.py migrate'
                echo "migration done"
            }
        }
    }
}
