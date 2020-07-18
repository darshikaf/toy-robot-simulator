#!/usr/bin/env groovy

pipeline {
  agent any

  stages {
    stage('Test') {
        steps {
          sh 'make test-python-lint'
          sh 'make test'
          }
        }
    }
      steps {
        // Publish as a Python package
        sh 'python setup.py sdist bdist_wheel; twine upload --repository testpypi dist/*'
      }
    }
  }
}
