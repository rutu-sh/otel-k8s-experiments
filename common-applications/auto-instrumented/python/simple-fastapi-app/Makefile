APP_IMAGE_NAME=otel-autoinstrumentation-fastapi-simple-app
DOCKER_REGISTRY=rutush10
DOCKER_REPO_NAME=otel-autoinstrumentation-fastapi-simple-app


build-docker-context:
	@echo "Building docker context"
	cp -r ${CURDIR}/src ${CURDIR}/build 


clear-docker-context:
	@echo "Clearing docker context"
	rm -rf ${CURDIR}/build/src


build-app: build-docker-context
	@echo "Building app"
	cd ${CURDIR}/build && \
	docker build --no-cache -t ${APP_IMAGE_NAME}:$(TAG) .
	$(MAKE) clear-docker-context


run-app:
	@echo "Running app"
	docker run --rm --name ${APP_IMAGE_NAME} -p 8000:8000 ${APP_IMAGE_NAME}:$(TAG)


publish: build-app
	@echo "Publishing app"
	docker tag ${APP_IMAGE_NAME}:$(TAG) ${DOCKER_REGISTRY}/$(DOCKER_REPO_NAME):$(TAG) && \
	docker push ${DOCKER_REGISTRY}/${APP_IMAGE_NAME}:$(TAG)