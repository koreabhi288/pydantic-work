from pydantic import BaseModel,EmailStr,AnyUrl,field_validator
from typing import List,Dict,Optional, Annotated

class patient(BaseModel):
    name: str
    email:EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float
    married: bool
    allergies : List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Npt a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after') #field_validator has teo modes 'before' and 'after
    @classmethod
    def transform_age(cls,value):
        if 0 < value <120:
            return value
        else:
            raise ValueError('Age should be between 0 and 120')
    
    
def insert_patient_data(Patient:patient):
    print(Patient.name)
    print(Patient.email)
    print(Patient.linkedin_url)
    print(Patient.age)
    print(Patient.weight)
    print(Patient.married)
    print(Patient.contact_details)
    print('inserted')
    
patient_info = {'name':'abhinandan','email':'abc@icici.com','linkedin_url':'http://linkedin.com/1322','age':'21','weight':43.56,'married':True,'allergies':['pollan','dust'],'contact_details':{'email':'abc@hdfc.com','phone':'992874384'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
    