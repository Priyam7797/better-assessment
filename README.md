# Better Assessment - Task Comments Application

## Project Setup

### Backend
- Python 3.x
- Flask: Web framework for REST API
- Flask-CORS: To handle Cross-Origin Resource Sharing (CORS)
- SQLAlchemy: ORM for database interactions
- SQLite: Lightweight database stored in a file

To set up backend:
1. Create a virtual environment and activate it.
2. Install dependencies from `backend/requirements.txt`.
3. Run the backend server:
   ```
   python backend/app.py
   ```
   The backend runs on `http://127.0.0.1:5000`.

### Frontend
- React: UI library for building the frontend
- Vite: Development server and build tool
- Axios: HTTP client for API requests

To set up frontend:
1. Navigate to `frontend` directory.
2. Install dependencies:
   ```
   npm install
   ```
3. Run the frontend dev server:
   ```
   npm run dev
   ```
   The frontend runs on `http://localhost:5174` or `http://localhost:5175`.

## API Structure

- `GET /api/comments/<task_id>`: Fetch comments for a task.
- `POST /api/comments`: Add a new comment. JSON body: `{ "task_id": int, "text": string }`
- `PUT /api/comments/<id>`: Update a comment's text. JSON body: `{ "text": string }`
- `DELETE /api/comments/<id>`: Delete a comment.

## How to Run Tests

- Currently, no automated tests are included.
- Manual testing can be done by running backend and frontend servers and interacting with the UI.
- Use tools like Postman or curl to test API endpoints.

## Design Decisions and Tradeoffs

- **Flask + SQLite**: Chosen for simplicity and ease of setup for a small project.
- **React + Vite**: Modern frontend stack for fast development and hot reloading.
- **CORS Configuration**: Explicitly allowed frontend dev server origins to avoid CORS issues.
- **Task ID Hardcoded**: For simplicity, task ID is hardcoded to 1 in frontend; can be extended for multiple tasks.
- **No Authentication**: The app is open; authentication can be added for security.
- **Error Handling**: Basic error logging is implemented; can be improved with user feedback.

## Possible Improvements

- Add automated tests for backend and frontend.
- Implement authentication and authorization.
- Support multiple tasks with dynamic task IDs.
- Add pagination for comments.
- Improve UI/UX with better styling and feedback.
- Deploy backend and frontend to production environments.

---

This README provides an overview of the project setup, API, and design considerations to help you prepare for interviews or further development.
