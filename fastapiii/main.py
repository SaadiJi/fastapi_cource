from typing import Union
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id":2}]

def find_pos(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
# request Get method url: "/"
@app.get("/")
def read_root():
    return {"Hello": "Wellcom to FastApi"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_pos(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"post with id: {id} not found"}
    return {"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)
    my_posts.pop(index)
    return {'message': 'post was sucessfully deleted'}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    # print(post)
    # return {'message': "updated post"}
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
        
        post_dict = post.dict()
        post_dict['id'] = id
        my_posts[index] = post_dict
        return {"data": post_dict}
    
    

