pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')   
    }

    environment {
        IMAGE     = 'arfbassem123/counter-app'
        DOCKERHUB = credentials('dockerhub-creds')
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

    stage('Unit tests') {
        steps {
            sh '''
                python3 -m venv .venv
                . .venv/bin/activate
                pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt
                pytest -v -p no:cacheprovider
            '''
        }
    }

        stage('Build image') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                sh 'docker push $IMAGE:$BUILD_NUMBER'
                sh 'docker push $IMAGE:latest'
            }
        }
    }

    post {
        always { sh 'docker logout || true' }
    }
}