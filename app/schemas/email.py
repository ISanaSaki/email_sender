from pydantic import BaseModel, EmailStr

class EmailCreate(BaseModel):
    email: EmailStr
    message: str