from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/posts"
)

# NEWEST GET all posts
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# NEWEST GET specific post 
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    return post


# NEWEST POST a new post -- unpacking a dict happens through **
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    # create the Post structure using the Post object
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# DELETE a post
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    deleted_post = db.query(models.Post).filter(models.Post.id == id)

    if not deleted_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with id {id} was not found")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# NEWEST (PUT) request for a post
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    updated_post = post_query.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    
    post_query.update(post.model_dump(), synchronize_session=False)

    db.commit()

    return post
