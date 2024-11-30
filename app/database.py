from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.student_management
students_collection = db.students
