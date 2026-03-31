from pydantic import BaseModel,EmailStr,AnyUrl,computed_field
from typing import List,Dict,Optional, Annotated

class patient(BaseModel):
    name : str
    email:EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float
    height : float
    married: bool
    allergies : List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
    
    
def insert_patient_data(Patient:patient):
    print(Patient.name)
    print(Patient.email)
    print(Patient.linkedin_url)
    print(Patient.age)
    print(Patient.weight)
    print(Patient.married)
    print(Patient.contact_details)
    print('BMI',Patient.bmi)
    print('inserted')
    
patient_info = {'name':'abhinandan','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322','age':21,'weight':75.2,'height':1.72,'married':True,'allergies':['pollan','dust'],'contact_details':{'email':'abc@gmail.coom','phone':'992874384'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
    