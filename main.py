from fastapi import FastAPI
from routers.user import user_router
from routers.mood import router as mood_router

app = FastAPI()

app.include_router(user_router)
app.include_router(mood_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)