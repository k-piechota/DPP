pipeline {
  agent any
  environment {
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }
  stages {
    stage('build') {
      steps {     
sh """
export PATH=${VIRTUAL_ENV}/bin:${PATH}
pwd
pip install -r requirements.txt
"""
      }
    }
    stage('test') {
      steps {
sh """
export PATH=${VIRTUAL_ENV}/bin:${PATH}
python --version
python test.py
"""
      }
      post {
        always {
          junit '**/test-reports/*.xml'
        }
      }
    }
  }
}
