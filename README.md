# otel-k8s-experiments

![created with https://socialify.git.ci/](./docs/assets/otel-k8s-experiments.svg)

Examples for using Opentelmetry in a Kubernetes environment. 

## About
[Opentelemetry](https://opentelemetry.io) and [Kubernetes](https://kubernetes.io) are two of the most popular [CNCF](https://www.cncf.io) [projects](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/). 

Kubernetes is an already accepted solution for a variety of orchestration usecases, it has been tried and tested for deploying a cluster of microservices at different scales. In a distributed environment with multiple microservices, a kubernetes cluster can get quite complex as the microservices interact with each other. In such a setup, if there is no uniform layer for observability, the MTTD (Mean Time To Detect) and the MTTR (Mean Time To Resolve) can significantly go up. Having a standard observability layer would help in this situation by allowing for fetching the telemetry data (metrics, traces, logs) and displaying it in a dashboarding tool such as [Grafana](https://grafana.com) to trace out the flow and pinpoint the problem.

Opentelemetry is aimed at providing a standard protocol and tools for observability. It defines the [opentelemetry specification](https://opentelemetry.io/docs/specs/otel/) for instrumenting telemetry data. The benefit of having a standard specification for telemetry data is in using the data with other tools down the line. The instrumented data can then be integrated with tools like [Jaeger](https://www.jaegertracing.io), [Zipkin](https://zipkin.io), [Prometheus](https://prometheus.io), etc. or with some [vendor-specific](https://opentelemetry.io/ecosystem/vendors/) tools.


# Experiments

### 1. [Single Application Single Collector](./experiments/single-app-single-collector)

This experiment demonstrates how to set up a single application with a single opentelemetry collector. The application is a simple FastAPI application that has been auto-instrumented using the `opentelemetry-instrument` command line tool. The collector is configured to receive telemetry data from the application and log the telemetry data. 

![Single App Single Collector](./experiments/single-app-single-collector/docs/assets/high-level-architecture.drawio.png)


# Applications

Following applications are defined in this repository. 


| Application | Instrumentation | Description | Reference |
| ----------- | --------------- | ----------- | --------- |
|Simple Fastapi Application | Auto Instrumentation | A simple FastAPI application that is instrumented with OpenTelemetry using the [OpenTelemetry Auto Instrumentation for Python](https://opentelemetry.io/docs/instrumentation/python/automatic/). It listens on the port 8000, and generates telemetry data for each request. | [README.md](./common-applications/auto-instrumented/python/simple-fastapi-app/docs/README.md) |



---
