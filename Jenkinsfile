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
"""
      }
    }
    stage('test') {
      steps {
sh """
export PATH=${VIRTUAL_ENV}/bin:${PATH}
python --version
python -m game.test_Board.py
"""
      }
    }
  }
}
