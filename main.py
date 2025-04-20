from fastapi import FastAPI
from routers.user import user_router
from routers.mood import router as mood_router
from routers.tests import test_router as test_router
from routers.articles import articles_router as articles_router
from routers.quotes import quotes_router as quotes_router


app = FastAPI()

from routers import tests


app.include_router(user_router)
app.include_router(mood_router)
app.include_router(test_router)
app.include_router(quotes_router)
app.include_router(articles_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)