pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Maza-Alain/first-pipeline']]])
            }
        }

        stage('Instalar dependencias') {
            steps {
                script {
                    // Instalar dependencias definidas en requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Validar tests') {
            steps {
                script {
                    // Verificar si las pruebas pasaron exitosamente
                    def test_result = sh(script: 'python tests.py', returnStatus: true)
                    if (test_result == 0) {
                        echo 'Los tests pasaron exitosamente.'
                    } else {
                        error 'Los tests fallaron. No se puede continuar.'
                    }
                }
            }
        }
    }
}



