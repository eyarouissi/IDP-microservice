from typing import List, Optional
from datetime import datetime, time, timedelta,date
from pydantic import BaseModel, EmailStr, Field,Json


class Employee(BaseModel): 
    email : EmailStr = Field(...)
    first: str = Field(...)
    last: str = Field(...)
    start_timestamp : str = Field(...)
    end_timestamp :str = Field(...)
    project_code : str = Field(...)
    titre_du_service : str = Field(...)

    class Config:
        orm_mode = True
        schema_extra = {
   
            
             "first": "employee's first name",
             "last": "employee's last name",
             "email": "employee's corporation email",
             "start_timestamp" : "first",
             "end_timestamp" : "first",
            
             "project_code" : "first",
             "titre_du_service" : "first" }




def ResponseModel_post(data, message):
    return {
        "data": [
            data
        ],
        "code": 201,
        "message": message,
    }

def ResponseModel_get(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
