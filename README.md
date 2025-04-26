# Todo List API

This is a Todo List API built with FastAPI and PostgreSQL. The application allows users to manage their todo items, including creating, reading, updating, and deleting tasks.

## Requirements

- Python 3.12
- Docker and Docker Compose

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:iKenshu/todolist.git
   cd todo-list
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:

   ```bash
   fastapi run main.py
   ```

5. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Running with Docker

1. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Testing

Run the tests using `pytest`:

```bash
pytest
```
