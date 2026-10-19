pipeline {
    agent any
    options { disableConcurrentBuilds(); skipDefaultCheckout(true) }
    environment {
        STUDENT_NAME = 'Aisen'
        STUDENT_SURNAME = 'Eremeev'
        STUDENT_GROUP = 'IT2-2314'
        STUDENT_ID = '37128'
        IMAGE = 'eremeev-aisen-devops'
        CONTAINER = 'eremeev-aisen-jenkins-container'
    }
    stages {
        stage('Checkout') {
            steps { checkout scm; sh 'git log -1 --format="%H %s"' }
        }
        stage('Build') {
            steps {
                sh '''echo "Student: $STUDENT_NAME $STUDENT_SURNAME"
echo "Group: $STUDENT_GROUP"
echo "Student ID: $STUDENT_ID"
python3 -m compileall -q app'''
            }
        }
        stage('Test') {
            steps { sh "python3 -m unittest discover -s app -p 'test_*.py' -v" }
        }
        stage('Docker Build') {
            steps { sh 'docker build -t "$IMAGE:$BUILD_NUMBER" -t "$IMAGE:latest" .' }
        }
        stage('Docker Run') {
            steps {
                sh '''if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
  docker rm -f "$CONTAINER"
fi
docker run -d --name "$CONTAINER" -p 127.0.0.1:8001:8000 \\
  -e STUDENT_NAME -e STUDENT_SURNAME -e STUDENT_GROUP -e STUDENT_ID "$IMAGE:$BUILD_NUMBER"
ready=0
for attempt in $(seq 1 30); do
  if docker exec "$CONTAINER" python -c 'import urllib.request; urllib.request.urlopen("http://127.0.0.1:8000/health")' 2>/dev/null; then
    ready=1; break
  fi
  sleep 1
done
test "$ready" = 1
docker logs "$CONTAINER"
docker ps --filter "name=$CONTAINER"'''
            }
        }
    }
}
