pipeline {
    agent any

    tools {
        nodejs "NodeJS"
    }

    stages {
        stage('Test') {
            steps {
                echo 'Testing Static (pylint)..'
            }
            steps {
                echo 'Testing Unit..'
            }
        }
        stage('Generate Documentaion') {
            steps {
                echo 'Documenting....'
            }
        }
    }
}
