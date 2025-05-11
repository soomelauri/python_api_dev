from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional
from random import randrange
import psycopg
import time
from . import models, schemas
from sqlalchemy.orm import Session
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

# let's simplify this by first creating the connection string, and then for each of the API requests, we close and open the connection
conn_string = "dbname=fast-api-demo user=postgres"

# to create an instance, run app = FastAPI()
app = FastAPI()
# auto code
@app.get("/")
async def root():
    return {"message": "welcome to my API"}

# NEWEST GET all posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# NEWEST GET specific post 
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    return post


# NEWEST POST a new post -- unpacking a dict happens through **
@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    # create the Post structure using the Post object
    new_post = models.Post(**post.model_dump())
    return new_post

# DELETE a post
@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    deleted_post = db.query(models.Post).filter(models.Post.id == id)

    if not deleted_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with id {id} was not found")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# NEWEST (PUT) request for a post
@app.put("/posts/{id}")
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    updated_post = post_query.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    
    post_query.update(post.model_dump(), synchronize_session=False)

    db.commit()

    return post
