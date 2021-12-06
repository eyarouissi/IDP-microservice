from pymongo.mongo_client import MongoClient
import motor.motor_asyncio
from bson import ObjectId
from pydantic.networks import EmailStr
import ssl
import pymongo 
from models import  * 

dev = 'mongodb+srv://Rania_Hamdeni:careerboosts2000@cluster0.vfuyb.mongodb.net/test?authSource=admin&replicaSet=atlas-12sscv-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
client = pymongo.MongoClient(dev, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
database = client['CareerBoosts']

Roles_collection = database.get_collection('roles')
Competencies_collection = database.get_collection('competencies')
CurrentProfiles_collection = database.get_collection('currentProfiles')
TargetProfiles_collection = database.get_collection('targetProfiles')
Employees_collection = database.get_collection('employees')
Courses_collection = database.get_collection('courses')
Certifications_collection = database.get_collection('certifications')






   
   









