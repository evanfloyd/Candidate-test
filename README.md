# Magic 8 Ball

Provides a response to a yes or no question (must be asked verbally/mentally)

## Installation and use

(Must have docker installed)
### Create docker network

- Run ```docker network create <network name> --driver bridge```
### Magic-8ball

- Clone repo
- Navigate into Magic-8ball folder
- Run ```docker build -t <image name> .```
- Run ```docker run --network <network name> -p 5000:5000 -d <image name>```
- Ask your question verbally or mentally and go to ```http://127.0.0.1:5000/```
- Refresh page to receive more answers

### Prometheus

- Navigate into Prometheus folder
- Run ```docker build -t <2nd image name> .```
- Run ```docker run --network <network name> -p 9090:9090 -d <2nd image name>```
- Go to ```http://localhost:9090/```
- Select ```Status``` and select ```Targets```

### Grafana

- Navigate into Grafana folder
- Run ```docker build -t <3rd image name> .```
- Run ```docker run --network <network name> -p 3000:3000 -d <3rd image name>```
- Go to ```http://localhost:3000/```
- Login with ```User: admin``` ```Pass:admin``
- Create new Password
- Hover over Configurations and select ```Data Sources``` and select ```Prometheus```
- In Settings set the URL as ```http://host.docker.internal:9090/```
- Under Auth Select ```Basic Auth``` then enter ```User: admin``` ```Pass: admin```
- Under Dashboards import ```Prometheus Stats```
- Navigate to ```Integrations and Connections```
- In ```Search integrations``` enter ```Prometheus``` select ```Hosted Prometheus metrics```
- Under ```Configuration Details``` select ```From my local Prometheus server```
- Enter API key name and select ```Create API key```
- Copy the code and run it in your Prometheus container shell
- Navigate to ```Dashboards``` under Browse select ```Prometheus Stats```
- Select the Uptime name and click edit
- Under the first query select ```Metrics browser``` and select ```up``` and select your ```Instance```
- Select ```Use query```
