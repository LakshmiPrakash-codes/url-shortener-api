# from fastapi import FastAPI
# from app.database import engine, Base
# from app.routes import router

# # Create all tables automatically on startup
# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="URL Shortener API",
#     description="A production-grade URL shortening service built with FastAPI and PostgreSQL. Supports custom short codes, click tracking, and URL statistics.",
#     version="1.0.0",
#     contact={
#         "name": "Lakshmi Prakash Nagati",
#         "url": "https://github.com/LakshmiPrakash-codes",
#         "email": "nlpcoding51@gmail.com"
#     }
# )

# app.include_router(router)

# @app.get("/", tags=["Health"])
# def root():
#     return {
#         "message": "URL Shortener API is running",
#         "docs": "/docs",
#         "version": "1.0.0"
    


from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    description="A production-grade URL shortening service built with FastAPI and PostgreSQL.",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "URL Shortener API is live 🚀",
        "docs": "/docs"
    }
