from fastapi import APIRouter, HTTPException
from app.schemas import Student, UpdateStudent
from app.database import students_collection
from app.utils import convert_object_id
from bson import ObjectId

router = APIRouter()

@router.post("/students/")
async def create_student(student: Student):
    student_dict = student.dict()
    result = await students_collection.insert_one(student_dict)
    student_dict["id"] = str(result.inserted_id)
    return student_dict

@router.get("/students/")
async def list_students():
    students = await students_collection.find().to_list(100)
    return [convert_object_id(student) for student in students]

@router.get("/students/{id}")
async def get_student(id: str):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return convert_object_id(student)

@router.patch("/students/{id}")
async def update_student(id: str, student_update: UpdateStudent):
    update_data = {k: v for k, v in student_update.dict().items() if v is not None}
    result = await students_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    student = await students_collection.find_one({"_id": ObjectId(id)})
    return convert_object_id(student)

@router.delete("/students/{id}")
async def delete_student(id: str):
    result = await students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
