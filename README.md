# Task Manager API (Techolution Python Cloud Intern Assignment)

A cloud-ready Task Management API built with **FastAPI**, **MongoDB**, **Docker**, and **Kubernetes (Minikube)**.  
The system supports full CRUD operations for tasks and integrates with **GitHub Issues** to automatically create, update, and close issues corresponding to tasks.

---

# Features

- Create, read, update, delete tasks
- Mark tasks as completed
- Pagination support for task listing
- Health check endpoint
- GitHub Issues integration
- MongoDB Atlas database
- Docker containerization
- Kubernetes deployment using Minikube
- Secure credential handling using Kubernetes Secrets

---

# Architecture

```
Client
   ↓
FastAPI (Routes)
   ↓
Service Layer
   ↓
Repository Layer
   ↓
MongoDB Atlas
```

External integration:

```
FastAPI
   ↓
GitHub SDK (PyGithub)
   ↓
GitHub Issues
```

Deployment architecture:

```
Docker Container
      ↓
Kubernetes Deployment
      ↓
Pod
      ↓
Service (NodePort)
      ↓
Accessible API
```

---

# Tech Stack

Backend
- FastAPI
- Python

Database
- MongoDB Atlas
- PyMongo

External Integration
- GitHub API (PyGithub)

Infrastructure
- Docker
- Kubernetes (Minikube)

---

# API Endpoints

## Create Task
```
POST /tasks
```

Example request:

```json
{
 "title": "Fix login bug",
 "description": "Resolve authentication issue",
 "priority": "high",
 "status": "pending"
}
```

Creates a task and automatically generates a **GitHub Issue**.

---

## Get All Tasks (Pagination)

```
GET /tasks?page=1&limit=5
```

Returns paginated list of tasks.

---

## Get Single Task

```
GET /tasks/{task_id}
```

Returns details of a specific task.

---

## Update Task

```
PUT /tasks/{task_id}
```

Updates the task and synchronizes changes with the **GitHub Issue**.

---

## Delete Task

```
DELETE /tasks/{task_id}
```

Deletes the task and closes the corresponding **GitHub Issue**.

---

## Mark Task Completed

```
POST /tasks/{task_id}/complete
```

Updates task status to completed.

---

## Health Check

```
GET /health
```

Returns API health status.

---

# Database Schema

Example MongoDB document:

```json
{
 "_id": "ObjectId",
 "title": "Fix login bug",
 "description": "Resolve authentication issue",
 "priority": "high",
 "status": "pending",
 "created_at": "...",
 "updated_at": "...",
 "external_reference_id": "GitHub Issue Number"
}
```

---

# GitHub Integration

Task actions automatically sync with GitHub Issues:

| Task Action | GitHub Action |
|-------------|--------------|
| Create Task | Create Issue |
| Update Task | Update Issue |
| Delete Task | Close Issue |

Github Issues Repository: https://github.com/SGCODEX/task-manager-api-test/issues

---

# Running the Project Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

# Docker Setup

Build Docker image:

```
docker build -t task-manager-api .
```

Run container:

```
docker run -p 8000:8000 --env-file .env task-manager-api
```

---

# Kubernetes Deployment (Minikube)

Start Minikube:

```
minikube start
```

Deploy application:

```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Access the API:

```
minikube service task-manager-service
```

---

# Environment Variables

The following environment variables are required:

```
MONGO_URI=your_mongodb_connection
GITHUB_TOKEN=your_github_token
GITHUB_REPO=your_repo_name
```

---

# Project Structure

```
task-manager-api
│
├── app
│   ├── main.py
│   ├── routes.py
│   ├── service.py
│   ├── repository.py
│   ├── models.py
│   └── github_service.py
│
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

---

# Key Highlights

- Clean layered architecture (Routes → Service → Repository)
- GitHub issue synchronization
- Containerized backend
- Kubernetes-ready deployment
- Scalable API design with pagination

---

# Author

Shivam Gupta