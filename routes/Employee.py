#from _typeshed import ReadableBuffer
from re import MULTILINE
import pydantic
from bson import ObjectId
import bson
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
from fastapi import APIRouter, Body,  Request
from fastapi.encoders import jsonable_encoder
import pymongo
from starlette.routing import request_response 
from database.database import *
from models.Employee import *
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import  pymongo
import asyncio
router = APIRouter()


#Returns the roles
@router.get("/roles", response_description="roles retrieved")
async def get_roles():

    doc = list ( Roles_collection.find({},{"roleCompetencies":0,"roleIsTailored":0,"roleAssessment":0}))
    
    if doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The roles are not found")
    else :
     
     
     return ResponseModel_get(doc, "Roles retrieved successfully")
    
#Returns courses
@router.get("/courses", response_description="courses retrieved")
async def courses():

    doc = list ( Courses_collection.find({}))
    
    if doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The courses are not found")
    else :
     
     
     return ResponseModel_get(doc, "Courses retrieved successfully")

#Returns certfications
@router.get("/certifications", response_description="certifications retrieved")
async def certifications():

    doc = list ( Certifications_collection.find({}))
    
    if doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The certifcations are not found")
    else :
     
     
     return ResponseModel_get(doc, "Certifications retrieved successfully")
 
