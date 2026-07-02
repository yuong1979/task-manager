# Task Manager — Product Specification

## Product Description

A simple web-based task manager that allows users to create, read, update, and delete tasks. Each task has a title, description, completion status, and timestamps. The app provides a clean REST API backend (Flask + SQLite in dev, Supabase PostgreSQL in production) and a React frontend with a minimal interface for managing tasks. The backend is deployed on Railway, the frontend on Vercel.

## User Stories

1. **View all tasks** — As a user, I want to see a list of all my tasks so I can see what needs to be done.
2. **Create a task** — As a user, I want to add a new task with a title and description so I can track new work items.
3. **Edit a task** — As a user, I want to update a task's title, description, or completion status so I can keep my task list accurate.
4. **Delete a task** — As a user, I want to remove a task I no longer need so my list stays clean.
5. **Toggle completion** — As a user, I want to mark a task as complete/incomplete with one click so I can track progress quickly.

## Acceptance Criteria

### AC1: View all tasks
- GET /api/tasks returns a JSON array of all tasks.
- Each task object includes id, title, description, completed, created_at, updated_at.
- The frontend displays tasks in a list, showing title and completion status.
- Empty list shows a "No tasks yet" message.

### AC2: Create a task
- POST /api/tasks accepts JSON body with title (required) and description (optional).
- Returns 201 with the created task object.
- Returns 400 if title is missing or empty.
- Frontend form has title input (required) and description textarea (optional).
- New task appears at the top of the list after creation.

### AC3: Edit a task
- PUT /api/tasks/:id accepts JSON body with any subset of: title, description, completed.
- Returns 200 with the updated task object.
- Returns 404 if task id does not exist.
- Frontend allows inline editing of title and description.
- Changes save on blur or Enter.

### AC4: Delete a task
- DELETE /api/tasks/:id returns 204 with no content.
- Returns 404 if task id does not exist.
- Frontend shows a delete button on each task item.
- Task is removed from the list after deletion.

### AC5: Toggle completion
- PUT /api/tasks/:id with {"completed": true/false} toggles status.
- Frontend checkbox or click-to-toggle on each task item.
- Completed tasks show with strikethrough style.

## Data Model

### Task

| Field       | Type      | Constraints          |
|-------------|-----------|----------------------|
| id          | integer   | PK, auto-increment   |
| title       | string    | NOT NULL, max 200    |
| description | text      | nullable             |
| completed   | boolean   | NOT NULL, default false |
| created_at  | datetime  | NOT NULL, server default |
| updated_at  | datetime  | NOT NULL, auto-update |

## REST API Endpoints

| Method   | Endpoint          | Request Body                    | Response        |
|----------|-------------------|---------------------------------|-----------------|
| GET      | /api/tasks        | —                               | 200 [Task]      |
| POST     | /api/tasks        | {title: string, description?: string} | 201 Task  |
| PUT      | /api/tasks/:id    | {title?: string, description?: string, completed?: boolean} | 200 Task |
| DELETE   | /api/tasks/:id    | —                               | 204             |

Error responses: 400 (validation), 404 (not found), 500 (server error). All errors return JSON: `{"error": "message"}`.

## Frontend Routes/Pages

| Route       | Component   | Description              |
|-------------|-------------|--------------------------|
| /           | TaskList    | Show all tasks, toggle   |
| /new        | TaskForm    | Create new task          |
| /edit/:id   | TaskForm    | Edit existing task       |
