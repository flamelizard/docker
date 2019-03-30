docker build -t identijenk .
docker run --name jenkins-data identijenk echo "Jenkins Data Container"
docker run -d --name jenkins -p 8080:8080 --volumes-from jenkins-data -v /var/run/docker.sock:/var/run/docker.sock identijenk