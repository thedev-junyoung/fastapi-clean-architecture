from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from user.interface.controller.user_controller import router as user_router
app = FastAPI()

app.include_router(user_router)

@app.exception_handler(RequestValidationError) # RequestValidationError 예외가 발생하면 처리하는 핸들러
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400, # 상태 코드를 400으로 설정한다.
        content=exc.errors(), # 에러 메시지를 반환한다.
    )


@app.get("/")
def hello():
    return {"hello": "FastAPI"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)