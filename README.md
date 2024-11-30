
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

## **Project Structure**

```plaintext
backend_challenge/
├── app/
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── main.py                 # Application entry point
│   ├── routes.py               # API routes definitions
│   ├── database.py             # Database connection and collections
│   ├── models/
│   │   ├── __init__.py         # Models package
│   │   ├── student.py          # Pydantic models for validation
│   └── utils/
│       ├── __init__.py         # Utilities package
│       └── id_conversion.py    # Helper function for MongoDB _id to id conversion
├── .env                        # Environment variables (e.g., MongoDB URI)
├── start.sh                    # Script to start the application
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation (this file)
```

---

## **Installation**

### **Prerequisites**
- Python 3.8+
- MongoDB
- [Render](https://render.com) account (for deployment)
- Docker (optional, for containerized deployment)

---

### **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/backend_challenge.git
   cd backend_challenge
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory:
     ```plaintext
     MONGO_URI=<your_mongodb_connection_string>
     ```
   - Replace `<your_mongodb_connection_string>` with your MongoDB URI.

4. **Run the application**:
   ```bash
   ./start.sh
   ```

5. **Access the API**:
   - The application will be available at `http://localhost:8000` (or the `$PORT` specified).

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

## **Deployment on Render**

1. **Create a new Web Service**:
   - Log in to Render and create a new web service.
   - Link your GitHub repository to the service.

2. **Set Environment Variables**:
   - Add the `MONGO_URI` environment variable in the Render dashboard.

3. **Start Command**:
   ```bash
   ./start.sh
   ```

4. **Deploy**:
   - Render will detect the open port using the `$PORT` environment variable and deploy the service.

---

## **Docker Setup (Optional)**

1. **Build the Docker image**:
   ```bash
   docker build -t backend_challenge .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 -e PORT=8000 -e MONGO_URI=<your_mongodb_connection_string> backend_challenge
   ```

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

