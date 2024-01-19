# from pydantic import BaseModel
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.exceptions import RequestValidationError
# from pydantic import BaseModel
# from fastapi.responses import PlainTextResponse

# app = FastAPI()


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     import pdb
#     pdb.set_trace()
#     return PlainTextResponse(str(exc), status_code=400)


# class Item(BaseModel):
#     name: str


# app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [f"{i['msg']}" for i in exc.errors()]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": errors},

    )


class Demo(BaseModel):
    content: str = None


@app.post("/demo")
async def some_func(d: Demo):
    return d
