import logging

import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}


@app.get("/hello/{name}")
def hello(name: str):
    logger.info("Hello called")
    return {"message": f"Hello {name}!"}


@app.get("/error")
def error():
    logger.error("Error called")
    return JSONResponse(status_code=500, content={"message": "Error"})


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
