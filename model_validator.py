from pydantic import BaseModel,EmailStr,AnyUrl,model_validator
from typing import List,Dict,Optional, Annotated

class patient(BaseModel):
    name: str
    email:EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies : list[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have emergency contact')
        return model
    
    
def insert_patient_data(Patient:patient):
    print(Patient.name)
    print(Patient.email)
    print(Patient.linkedin_url)
    print(Patient.age)
    print(Patient.weight)
    print(Patient.married)
    print(Patient.contact_details)
    print('inserted')
    
patient_info = {'name':'abhinandan','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322','age':71,'weight':43.56,'married':True,'allergies':['pollan','dust'],'contact_details':{'email':'abc@gmail.coom','phone':'992874384','emergency':'29484'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
    