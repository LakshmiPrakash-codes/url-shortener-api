# URL Shortener API

Production-grade URL shortening REST API built with FastAPI and PostgreSQL.

## Features

- Shorten long URLs
- Redirect using short codes
- Click tracking
- PostgreSQL database integration
- Swagger/OpenAPI documentation
- Cloud deployment on Render

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Render

## Live API

https://url-shortener-api-vfai.onrender.com/docs

## GitHub Repository

https://github.com/LakshmiPrakash-codes/url-shortener-api

## API Endpoints

### Create Short URL

POST `/shorten`

Example request:

```json
{
  "original_url": "https://google.com"
}
```

### Redirect to Original URL

GET `/{short_code}`

Example:

```text
/abc123
```

## Run Locally

```bash
uvicorn app.main:app --reload
```

## Deployment

Deployed publicly using Render with PostgreSQL cloud database support.

## Author

Lakshmi Prakash
