from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from loguru import logger
from starlette.responses import JSONResponse

from .router import api_router


def create_app() -> FastAPI:
    app = FastAPI(title="JoyEnergy")

    app.include_router(api_router)

    @app.exception_handler(RequestValidationError)
    async def custom_validation_exception_handler(request, e):
        exc_str = f"{e}".replace("\n", " ").replace("   ", " ")
        logger.warning(f"{request}: {exc_str}")
        content = {"message": exc_str, "data": None}
        return JSONResponse(content=content, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)

    return app


app = create_app()
