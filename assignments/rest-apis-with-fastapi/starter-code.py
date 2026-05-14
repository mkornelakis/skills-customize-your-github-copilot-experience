# Install dependencies before running:
#   pip install fastapi uvicorn
#
# Run the server with:
#   uvicorn starter_code:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ── Task 1: Root endpoint ──────────────────────────────────────────────────────
# TODO: Define a GET / route that returns:
#   {"message": "Welcome to the Homework API!"}


# ── Task 2: Path parameter ─────────────────────────────────────────────────────
# TODO: Define a GET /greet/{name} route that returns a personalized greeting.
#   Example: GET /greet/Alice → {"message": "Hello, Alice! Welcome to the API."}


# ── Task 3: POST endpoint with request body ────────────────────────────────────
# TODO: Define a Pydantic model called Submission with:
#   - student_name: str
#   - assignment_title: str
#
# Then define a POST /submit route that accepts a Submission body and returns:
#   {"status": "received", "student": ..., "assignment": ...}


# ── Task 4 (Stretch): Query parameter filtering ────────────────────────────────
# TODO: Define a GET /assignments route with an optional `difficulty` query param.
#   Store a list of assignments (each with title + difficulty) and return them,
#   filtering by difficulty when provided.
