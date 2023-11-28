from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field
# from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(default=None)
    dateOfBirth: date = Field(...)
    email: EmailStr = Field(..., unique=True)
    password: str = Field(...)
    emailVerified: bool = Field(...)
    createDate: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "dateOfBirth": "1990-01-01",
                "email": "jdoe@example.com",
                "password": "secure_password",
                "emailVerified": True,
                "createDate": "2023-11-27"
            }
        }
    
    '''
    def setPassword(self,password):
        self.password = generate_password_hash(password)
    
    def checkPassword(self,password):
        return check_password_hash(self.password, password)
    '''    



class UpdateUserModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    dateOfBirth: Optional[date] 
    email: Optional[EmailStr] = Field(const=True)
    password: Optional[str]
    emailVerified: Optional[bool]
    createDate: Optional[date] = Field(const=True)

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "dateOfBirth": "1990-01-01",
                "email": "jdoe@example.com",
                "password": "secure_password",
                "emailVerified": True,
                "createDate": "2023-11-27"
            }
        }

