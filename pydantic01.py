from pydantic import BaseModel

class patient(BaseModel):
    name: str
    age: int
    weight: float
    
def insert_patient_data(Patient:patient):
    print(Patient.name)
    print(Patient.age)
    print(Patient.weight)
    print('inserted')
    
patient_info = {'name':'abhinandan','age':21,'weight':43.56}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
    