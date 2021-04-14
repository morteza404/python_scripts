from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
import uvicorn

app = FastAPI()

postdb = []

class Post(BaseModel):
    id: int
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/blog")
def get_posts():
    return postdb

@app.get("/blog/{id}")
def get_post(id:int):
    return postdb[id]

@app.post("/blog")
def add_post(post:Post):
    postdb.append(dict(post))
    return postdb[-1]

@app.put("/blog/{id}")
def update_post(id:int, post:Post):
    postdb[id] = post
    return {"message": "Post has been updated succesfully"}

@app.delete("/blog/{id}")
def delete_post(id:int):
    postdb.pop(id)
    return {"message": "Post has been deleted succesfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)