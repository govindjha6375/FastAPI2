
# **Backend Challenge Application**

This repository contains a FastAPI-based backend application for managing student data, designed to be deployed on Render with a modular and maintainable project structure.

---

## **Features**

- **CRUD operations**: Manage student data (Create, Read, Update, Delete).
- **MongoDB integration**: Uses `motor` (async MongoDB client) for database interactions.
- **RESTful APIs**: Built using FastAPI for simplicity and scalability.
- **Environment configuration**: Secrets like the MongoDB URI are managed using environment variables.
- **Production-ready**: Dockerized and deployable on Render with dynamic port binding.
- **Asynchronous design**: Ensures better performance and scalability.

---


## **Installation**

### **Prerequisites**
- Python 3.8+
- MongoDB
- [Render](https://render.com) account (for deployment)
- Docker (optional, for containerized deployment)

---


## **API Endpoints**

| Method | Endpoint        | Description                  |
|--------|-----------------|------------------------------|
| GET    | `/students`     | Fetch all student records    |
| POST   | `/students`     | Add a new student record     |
| GET    | `/students/{id}`| Fetch a specific student     |
| PUT    | `/students/{id}`| Update a student record      |
| DELETE | `/students/{id}`| Delete a student record      |

---


4. **Deploy**:
   - Render will detect the open port using the `$PORT` environment variable and deploy the service.

---


## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch and create a pull request.

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for details.

---

## **Acknowledgments**

- **[FastAPI](https://fastapi.tiangolo.com/)**: The framework powering this application.
- **[Render](https://render.com/)**: For easy deployment and hosting.
- **[Motor](https://motor.readthedocs.io/)**: Asynchronous MongoDB client.

---

