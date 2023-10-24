# Auto Instrumented FastAPI Application

This is a simple FastAPI application that is instrumented with OpenTelemetry using the [OpenTelemetry Auto Instrumentation for Python](https://opentelemetry.io/docs/instrumentation/python/automatic/). It listens on the port 8000, and generates telemetry data for each request. 


## Environment variables

A full reference of the Opentelemetry environment variables can be found here: [opentelemetry/environment-variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/)

`OTEL_SERVICE_NAME`: The name of the service generating the telemetry data. 

`OTEL_LOGS_EXPORTER`: The logs exporter to use, In this doc we're using the `console` exporter. If you have an opentelemetry collector set up, you can change this variable's value to `console,otlp` or just `otlp`. You will also have to set the `OTEL_EXPORTER_OTLP_ENDPOINT` variable to the endpoint of your opentelemetry collector.

`OTEL_TRACES_EXPORTER`: The traces exporter to use, In this doc we're using the `console` exporter. If you have an opentelemetry collector set up, you can change this variable's value to `console,otlp` or just `otlp`. You will also have to set the `OTEL_EXPORTER_OTLP_ENDPOINT` variable to the endpoint of your opentelemetry collector.

`OTEL_METRICS_EXPORTER`: The metrics exporter to use, In this doc we're using the `console` exporter. If you have an opentelemetry collector set up, you can change this variable's value to `console,otlp` or just `otlp`. You will also have to set the `OTEL_EXPORTER_OTLP_ENDPOINT` variable to the endpoint of your opentelemetry collector.

`OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED`: This variable enables auto-instrumentation for the `logging` module.


## Using the DockerHub repository

The image for this application is published on DockerHub, it can be found here: [rutush10/otel-autoinstrumentation-fastapi-simple-app
](https://hub.docker.com/repository/docker/rutush10/otel-autoinstrumentation-fastapi-simple-app/general)


To use the image with simple `docker run` command: 

```shell
docker run
	-e OTEL_SERVICE_NAME=single-app-single-collector-fastapi-app \
	-e OTEL_LOGS_EXPORTER=console \
	-e OTEL_TRACES_EXPORTER=console \
	-e OTEL_METRICS_EXPORTER=console \
	-e OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true \
	-p 8000:8000 \
	rutush10/otel-autoinstrumentation-fastapi-simple-app:latest
```

To use it within a `docker-compose.yaml`: 

```yaml
services:
  app:
    image: rutush10/otel-autoinstrumentation-fastapi-simple-app:latest
    ports:
      - "8000:8000"
    environment:
      - OTEL_SERVICE_NAME=otel-autoinstrumentation-fastapi-simple-app
      - OTEL_LOGS_EXPORTER=console
      - OTEL_TRACES_EXPORTER=console
      - OTEL_METRICS_EXPORTER=console
      - OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

To create a k8s deployment: 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-fastapi-app
  labels:
    app: simple-fastapi-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-fastapi-app
  template:
    metadata:
      labels:
        app: simple-fastapi-app
    spec:
      containers:
      - name: simple-fastapi-app
        imagePullPolicy: Always
        image: rutush10/otel-autoinstrumentation-fastapi-simple-app:latest
        ports:
          - containerPort: 8000
        environment:
          -e OTEL_SERVICE_NAME=simple-fastapi-app
          -e OTEL_LOGS_EXPORTER=console
          -e OTEL_TRACES_EXPORTER=console
          -e OTEL_METRICS_EXPORTER=console
          -e OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

If you're working with this applicaiton within a k8s environment, don't forget to add a NodePort or a ClusterIP service: 

```yaml
apiVersion: v1
kind: Service
metadata:
  name: simple-fastapi-app
  labels:
    app: simple-fastapi-app
spec:
  type: NodePort
  selector:
    app: simple-fastapi-app
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
      nodePort: 30000
```

For a ClusterIP service, change the `ports` to 

```yaml
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
```


## Testing the application locally

### Build

```shell
make build-app TAG=0.0.1
```

### Run

```shell
make run-app TAG=0.0.1
```

### Stop

```shell
make stop-app
```

## Make Requests

The [postman](./postman/) directory contains the postman collection and the environment for testing the application locally. You have to simply import the collection and environment in your postman and run the requests. 

Examples are provided within the requests for reference.


## Auto Instrumenting FastAPI Applications

The `opentelemetry-instrument` command line tool can be used to automatically instrument a FastAPI application. In this case we define the application without any instrumentation code: 

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Hello World"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
```

Then we run application via the `opentelemetry-instrument` command line tool.

```shell
opentelemetry-instrument python main.py
```

You can see the run command in `build/Dockerfile` for this application. 


## Using this code as a reference for your own application

If you want to use this code as a reference for your own FastAPI application, you can copy the following to your own application:

1. The `build` directory, which contains the `Dockerfile` and the `requirements.txt` file. You can edit the `requirements.txt` file to add any additional dependencies that you might need. 

2. The `src` directory, which contains the source code. You can add more files and folders as needed.

3. The `Makefile`, which contains the commands to build, run, publish, and stop the application. To publish the application to your own repository, edit the `REPOSITORY`, `APP_IMAGE_NAME`, and the `DOCKER_REPO_NAME` variables in the `Makefile`.

