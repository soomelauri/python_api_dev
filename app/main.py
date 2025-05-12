from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, post

models.Base.metadata.create_all(bind=engine)

# let's simplify this by first creating the connection string, and then for each of the API requests, we close and open the connection
conn_string = "dbname=fast-api-demo user=postgres"

# to create an instance, run app = FastAPI()
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
# auto code
@app.get("/")
async def root():
    return {"message": "welcome to my API"}
