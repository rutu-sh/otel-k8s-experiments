# Auto Instrumented FastAPI Application

This is a simple FastAPI application that is instrumented with OpenTelemetry using the [OpenTelemetry Auto Instrumentation for Python](https://opentelemetry.io/docs/instrumentation/python/automatic/). It listens on the port 8000, and generates telemetry data for each request. 

## Testing the application locally

### Build

```shell
make build-app TAG=0.0.1
```

### Run

```shell
make run-app TAG=0.0.1
```

The run command also contains certain environment variables that are required for auto-instrumentation:

`OTEL_SERVICE_NAME`: The name of the service generating the telemetry data. 

`OTEL_LOGS_EXPORTER`: The logs exporter to use, In this case we're using the `console` exporter. If you have an opentelemetry collector set up, you can change this variable's value to `console,otlp` or just `otlp`. You will also have to set the `OTEL_EXPORTER_OTLP_ENDPOINT` variable to the endpoint of your opentelemetry collector.

`OTEL_TRACES_EXPORTER`: The traces exporter to use, In this case we're using the `console` exporter. If you have an opentelemetry collector set up, you can change this variable's value to `console,otlp` or just `otlp`. You will also have to set the `OTEL_EXPORTER_OTLP_ENDPOINT` variable to the endpoint of your opentelemetry collector.

`OTEL_METRICS_EXPORTER`: The metrics exporter to use, In this case we're using the `console` exporter. If you have an opentelemetry collector set up, you can change this variable's value to `console,otlp` or just `otlp`. You will also have to set the `OTEL_EXPORTER_OTLP_ENDPOINT` variable to the endpoint of your opentelemetry collector.

`OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED`: This variable enables auto-instrumentation for the `logging` module.


### Stop

```shell
make stop-app
```

## Using docker-compose to run the application

To run the application using docker-compose, define the following in your `docker-compose.yml` file:

```yaml
version: "3.8"
services:
  app:
    image: rutush10/otel-autoinstrumentation-fastapi-simple-app:${TAG}
    ports:
      - "8000:8000"
    environment:
      - OTEL_SERVICE_NAME=otel-autoinstrumentation-fastapi-simple-app
      - OTEL_LOGS_EXPORTER=console
      - OTEL_TRACES_EXPORTER=console
      - OTEL_METRICS_EXPORTER=console
      - OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

Then run the following command:

```shell
TAG=0.0.1 docker-compose up
```

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

