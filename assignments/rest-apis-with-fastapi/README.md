# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python, including defining routes, handling path and query parameters, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up a Basic FastAPI Application

#### Description
Create a FastAPI application with a root endpoint that returns a welcome message. Install the required packages and run the development server.

#### Requirements
Completed program should:

- Import `FastAPI` from the `fastapi` module
- Create an app instance using `FastAPI()`
- Define a `GET /` route that returns `{"message": "Welcome to the Homework API!"}`
- Be runnable with `uvicorn` (e.g., `uvicorn main:app --reload`)

### 🛠️ Add a Route with Path Parameters

#### Description
Add a new endpoint that accepts a student's name as a path parameter and returns a personalized greeting.

#### Requirements
Completed program should:

- Define a `GET /greet/{name}` route
- Accept `name` as a path parameter (string)
- Return a JSON response like `{"message": "Hello, Alice! Welcome to the API."}`

Example:
```
GET /greet/Alice
→ {"message": "Hello, Alice! Welcome to the API."}
```

### 🛠️ Build a Homework Submission Endpoint

#### Description
Create a `POST /submit` endpoint that accepts a JSON body with a student's name and assignment title, and returns a confirmation message.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` class called `Submission` with fields `student_name` (str) and `assignment_title` (str)
- Define a `POST /submit` route that accepts a `Submission` body
- Return a JSON response like `{"status": "received", "student": "Alice", "assignment": "Loops and Conditionals"}`

Example request body:
```json
{
  "student_name": "Alice",
  "assignment_title": "Loops and Conditionals"
}
```

### 🛠️ Add Query Parameter Filtering (Stretch Goal)

#### Description
Add a `GET /assignments` endpoint that returns a list of assignment names and supports an optional query parameter to filter by difficulty level.

#### Requirements
Completed program should:

- Define a `GET /assignments` route with an optional `difficulty` query parameter (default: `None`)
- Store a list of assignments, each with a `title` and `difficulty` field (e.g., `"beginner"`, `"intermediate"`, `"advanced"`)
- Return all assignments if no `difficulty` is provided, or filter by the given value
- Return results as a JSON list

Example:
```
GET /assignments?difficulty=beginner
→ [{"title": "Python Basics", "difficulty": "beginner"}, ...]
```
