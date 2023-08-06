from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.routers.users import users_router
from api.api_v1.routers.auth import auth_router
from core import config
from db.session import SessionLocal
from core.auth import get_current_active_user
from core.celery_app import celery_app
import tasks


app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

# Configure CORS
origins = [
    "http://localhost",        # Replace with your React.js app's URL
    "http://localhost:3000"    # Add any additional allowed origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range"]
)





@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
