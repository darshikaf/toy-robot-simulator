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
    stage('release') {
      when { branch 'master' }
      steps {
        // Publish as a Python package
        sh 'make release'
      }
    }
}
