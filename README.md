# DevOps laboratory — Aisen Eremeev

Group IT2-2314 · Student ID 37128

Python HTTP application with Linux scripts, Docker Compose and a Jenkins pipeline.
The application returns student information at `/` and health status at `/health`.

## Run locally

```bash
python3 -m unittest discover -s app -p 'test_*.py' -v
python3 app/main.py
```

## Linux setup

Copy this project into `~/devops/eremeev_aisen` in Ubuntu, then run:

```bash
bash scripts/prepare_linux.sh
./scripts/Eremeev_Aisen_system.sh
```

## Docker

```bash
docker build -t eremeev-aisen-devops .
docker run -d --name eremeev-aisen-container -p 127.0.0.1:8000:8000 \
  -e STUDENT_NAME=Aisen -e STUDENT_SURNAME=Eremeev \
  -e STUDENT_GROUP=IT2-2314 -e STUDENT_ID=37128 eremeev-aisen-devops
curl http://localhost:8000/
docker logs eremeev-aisen-container
docker stop eremeev-aisen-container
docker start eremeev-aisen-container
docker stop eremeev-aisen-container
docker rm eremeev-aisen-container
docker compose up -d --build
curl http://localhost:8000/
docker compose down
```

## Jenkins prerequisites

Use a Linux agent with Git, Python 3, Docker CLI and access to a working Docker daemon.
Create Pipeline job `Eremeev_Aisen_DevOps`, select Pipeline script from SCM / Git,
set the URL of the actual GitHub repository, branch `*/main`, and script path `Jenkinsfile`.
The pipeline checks out source, compiles Python, runs tests, builds an image and
starts a container. The last stage verifies HTTP health before it can succeed.
The resulting application is bound to port 8001 on the Docker host's loopback address.

## Current verification status

The two Python tests passed on Windows. Linux execution, Docker build/run,
GitHub publication and Jenkins execution still require environment setup.
No successful Jenkins run or Docker result is claimed yet.
