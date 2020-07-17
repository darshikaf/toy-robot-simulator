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
    
  //   stage('deploy') {
  //     when { branch 'master' }
  //     agent {
  //       docker {
  //         image 'dockerhub.com/darshika/darkf-build-scoring:latest'
  //         reuseNode true
  //         args '-v /var/run/docker.sock:/var/run/docker.sock'
  //       }
  //     }
  //     environment {
  //       PYPI_REPOSITORY='https://pypi.org/project/'
  //       VAULT_ADDR = 'https://url.to.secrets.com:443'
  //     }
  //     steps {
  //       // Publish as a Python package
  //       wrap([$class: 'JwtIssuer', tokenFile: '.vault-jwt']) {
  //          withVaultJWTLogin('build', '.vault-jwt', 'jwt_jenkins') {
  //           sh '''
  //             set +x
  //             # ADD_COMMANDS #
  //             set -x
  //           '''
  //         }
  //       }
  //       sh 'export HOME=${WORKSPACE}; python setup.py sdist bdist_wheel; twine upload -r artifactory dist/*'
  //     }
  //   }
  // }
}
