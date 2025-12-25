from .. import models, schemas, utils, auth2
from typing import Union
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


# request Get method url: "/"
# @router.get("/")
# def read_root():
#     return {"Hello": "Wellcom to FastApi"}

@router.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}
    
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(auth2.get_current_user),
              Limit: int = 3, skip: int=0, search: Optional[str] = ""):
    # posts = db.query(models.Post).filter(
    #     models.Post.owner_id == current_user.id
    # ).limit(Limit).all()
    
    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall( )
    # print(posts)
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db), 
                 current_user: int = Depends(auth2.get_current_user)):
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0,1000000)
    # my_posts.append(post_dict)
    # cursor.execute("""INSERT INTO  posts(title, content, published) VALUES
    #                (%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    print(current_user.id)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return post

@router.get("/{id}")
def get_post(id: int,db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts where id = %s""", (str(id)))
    # post = cursor.fetchone()
    # print(test_post)
    # post = find_pos(int(id))
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"post with id: {id} not found"}
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts where id = %s returning *""",(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    # index = find_index_post(id)
    # my_posts.pop(index)
    if post.owner_id != auth2.current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = "Not Authorized for Perform this Operation")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(auth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s 
    #                where id = %s RETURNING *""",
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    u_post = post_query.first()
    # index = find_index_post(id)
    # print(post)
    # return {'message': "updated post"}
    if u_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
        
        # post_dict = post.dict()
        # post_dict['id'] = id
        # my_posts[index] = post_dict
        
    if post.owner_id != auth2.current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = "Not Authorized for Perform this Operation")
    
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()
    # return {"data": post_query.first()}