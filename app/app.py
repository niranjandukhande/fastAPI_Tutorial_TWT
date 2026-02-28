from fastapi import FastAPI

app = FastAPI()

text_posts = {
    1: {"title": "First Post", "content": "cool test post"},
    2: {"title": "Second Post", "content": "cool test post 2"},
}


@app.get("/posts")
def get_all_posts():
    return text_posts


@app.get(f"/posts/{id}")
def get_post(id: int):
    return text_posts.get(id)
