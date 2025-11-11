# Testing API

A simple FastAPI-based fake API for testing purposes. This project provides mock endpoints for users, posts, and items to simulate a REST API.

## Requirements

- Python >= 3.13
- Poetry (for dependency management)

## Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Set Python version if needed:**
   ```bash
   poetry env use python3.13
   ```

3. **Run the API server:**
   ```bash
http://127.0.0.1:8000   
   ```

   The API will be available at `http://localhost:8000`.

## API Endpoints

- **GET /**: Welcome message.
- **GET /items/{item_id}**: Get an item by ID. Optional query parameter `q`.
- **GET /users**: List all users.
- **GET /users/{user_id}**: Get a specific user by ID.
- **GET /posts**: List all posts.
- **GET /posts/{post_id}**: Get a specific post by ID.

## Development

- **Linting:** Run `poetry run black src/` and `poetry run isort src/`.
- **Testing:** Run `poetry run pytest`.
- **Lint checks:** Run `poetry run flake8 src/`.

## Project Structure

- `src/main.py`: Main FastAPI application with endpoints.
- `tests/`: Test files.
- `pyproject.toml`: Project configuration and dependencies.
- `poetry.lock`: Locked dependencies.

poetry run uvicorn src.main:app  --port 8000 --reload
