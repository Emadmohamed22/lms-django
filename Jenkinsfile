pipeline{
    agent {
        docker {image 'python:3.8-slim'}
    }

    stages{
        stage("install dependencies"){
            steps{
                sh'sudo pip3 install - r requirements.txt'
                echo "installation done"
            }
        }
       stage("migrate"){
            steps{
                sh'sudo python3 manage.py makemigrations'
                sh'sudo python3 manage.py migrate'
                echo "migration done"
            }
        }
    }
}
