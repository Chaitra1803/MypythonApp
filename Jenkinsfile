pipeline {
  agent any

  triggers {
    cron('* * * * *')  // Run every minute
  }

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t my-flask .'
        sh 'docker tag my-flask $DOCKER_BFLASK_IMAGE'
      }
    }

    stage('Automated Testing in CI') {
      steps {
        sh 'docker run my-flask python -m pytest app/tests/'
      }
    }

    stage('Deploy (with Rollback)') {
      steps {
        script {
          def imageTag = env.BUILD_FAULTY_VERSION == 'true' ? '$DOCKER_BFLASK_FAULTY_IMAGE' : '$DOCKER_BFLASK_IMAGE'
          echo "Deploying image: ${imageTag}"

          try {
            withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
              sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
              sh 'docker push $DOCKER_BFLASK_IMAGE'
              sh "docker rm -f mypycont"
              sh "docker run --name mypycont -d -p 3000:5000 ${imageTag}"
              echo "Deployment successful!"
            }
          } catch (Exception e) {
            stage('Rollback') {
              steps {
                script {
                  def previousStableImageTag = readFile('previous_stable_image.txt').trim()

                  sh "docker rm -f mypycont"
                  sh "docker run --name mypycont -d -p 3000:5000 ${previousStableImageTag}"
                  echo "Rolled back to image: ${previousStableImageTag}"
                  echo "Deployment failed! Rolled back to the previous stable version."
                }
              }
            }
          }
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline completed successfully and deployed latest image."
    }
  }
}
