from fastapi import FastAPI, HTTPException
from typing_extensions import Text

from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {
        "title": "Morning Thoughts",
        "content": "Just woke up and feeling great today. Coffee is brewing.",
    },
    2: {
        "title": "Tech Talk",
        "content": "Python 3.12 has some really interesting new features worth checking out.",
    },
    3: {
        "title": "Weekend Plans",
        "content": "Thinking about hiking this Saturday if the weather holds up.",
    },
    4: {
        "title": "Book Review",
        "content": "Just finished reading Dune for the third time. Still a masterpiece.",
    },
    5: {
        "title": "Recipe Share",
        "content": "Made homemade pasta last night — surprisingly easy and absolutely delicious.",
    },
    6: {
        "title": "Random Observation",
        "content": "Has anyone else noticed how much better music sounds on a rainy day?",
    },
    7: {
        "title": "Project Update",
        "content": "Finally fixed that bug I've been chasing for three days. Feels amazing.",
    },
    8: {
        "title": "Travel Memories",
        "content": "Looking back at photos from Japan last spring. Need to go back someday.",
    },
    9: {
        "title": "Fitness Check-in",
        "content": "Hit a new personal record on my run today — 5k in under 24 minutes!",
    },
    10: {
        "title": "Late Night Thoughts",
        "content": "It's 1am and I'm still thinking about whether a hotdog is a sandwich.",
    },
}


@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {
        "title": post.title,
        "content": post.content,
    }
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
