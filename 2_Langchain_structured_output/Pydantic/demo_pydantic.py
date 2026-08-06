from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Review(BaseModel):
    name: str = 'Nitesh'
    age: Optional[int] = None
    email: EmailStr


new_student = {"age": "21", "email": "abc@gmail.com"}

student = Review(**new_student)

print(student)
