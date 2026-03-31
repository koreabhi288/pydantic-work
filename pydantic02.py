from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional, Annotated

class patient(BaseModel):
    name: Annotated[str ,Field(max_length=50, title='name of the patient ',description='Give the name of the patient in less than 50 chars',examples=['nitish','Amit'])]
    email:EmailStr
    linkedin_url: AnyUrl
    age: int = Field(ge=0, lt=120)
    weight: Annotated[float ,Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies : Annotated[Optional[List[str]] , Field(default=None,max_length=5)]
    contact_details: Dict[str, str]
    
    
def insert_patient_data(Patient:patient):
    print(Patient.name)
    print(Patient.email)
    print(Patient.linkedin_url)
    print(Patient.age)
    print(Patient.weight)
    print(Patient.married)
    print(Patient.contact_details)
    print('inserted')
    
patient_info = {'name':'abhinandan','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322','age':21,'weight':43.56,'married':True,'allergies':['pollan','dust'],'contact_details':{'email':'abc@gmail.coom','phone':'992874384'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
    