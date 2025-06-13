from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

# to create an instance, run app = FastAPI()
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# auto code
@app.get("/")
async def root():
    return {"message": "welcome to my API"}
