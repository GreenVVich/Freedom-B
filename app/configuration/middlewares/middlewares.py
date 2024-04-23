from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware


async def catch_response_validation_error_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
    except ResponseValidationError as exc:
        return JSONResponse(
            status_code=400,
            content={"detail": exc.errors(), "body": exc.body},
        )
    except HTTPException as exc:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
    except Exception as exc:
        return JSONResponse(
            status_code=500,
            content={"detail": "Unhandled server error"},
        )
    return response


@dataclass(frozen=True)
class Middlewares:
    """
    Basic Middlewares class.
    To initialise ur middleware add it to __init__ file.
    """

    middlewares: tuple

    def register_middlewares(self, app: FastAPI):
        """
        Register all given middlewares function.
        """

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # app.middleware("http")(catch_response_validation_error_middleware)

        for middleware in self.middlewares:
            app.add_middleware(middleware)
