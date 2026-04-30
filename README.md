# ControlStack — Financial Tracking Backend (FastAPI, Distributed Architecture)

Backend service for managing financial transactions (expenses, income, services) designed with production-oriented architecture principles: modular design, containerization, and scalability.

## 🚧 Current Scope

* Transaction management (CRUD)
* REST API built with FastAPI
* MongoDB persistence layer
* Dockerized environment (multi-stage build + docker-compose)

## 🧠 Architecture Overview

The project follows a layered architecture:

* Routes → HTTP interface (FastAPI endpoints)
* Services → Business logic and orchestration
* Repositories → Data access abstraction
* Models/Schemas → Data structure and validation
* Core → Configuration and database setup

This structure enforces separation of concerns and prepares the system for future scalability (e.g., background processing, distributed components).

## ⚙️ Tech Stack

* Python (FastAPI)
* MongoDB
* Docker / Docker Compose
* Pydantic (data validation)

## 🚀 Running the Project

1. Clone or download this repository
2. Make sure docker is up and running:
   ```bash
   make build
   make up
   ```

The API will be available at `http://localhost:8000`

## API Documentation

The API includes automatic interactive documentation:

- **Swagger UI**: `http://localhost:8000/docs`

## 🎯 Purpose

This project is part of a transition toward Python backend engineering, focusing on applying distributed systems and backend architecture principles in a Python ecosystem.

## 📌 Notes

The current implementation focuses on clean architecture and maintainability. Future iterations will introduce more advanced system design components to simulate real-world backend environments.
