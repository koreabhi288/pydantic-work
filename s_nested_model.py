#from email.headerregistry import Address
from pydantic import BaseModel
from pydantic 
# class Patient(BaseModel):
#     name : str
#     gender : str
#     age : int
    #address : 'house no 2,sec 66,gurgaon,haryana,1239489 '  #complex to understand different fields
    
    #so we build pydantic model for address#
class Address(BaseModel):
        city : str
        state : str
        pin : str
        
class Patient(BaseModel):
        name : str
        gender: str
        age : int
        address : Address
        
address_dict = {'city':'gurgaon','state':'hryana','pin':'12384'}
    
address1 = Address(**address_dict)
    
patient_dict = {'name':'nitish','gender':'male','age':35,'address':address1}
    
patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=['name'])  #convert pydantic model into dictionary
temp1=patient1.model_dump_json()

temp2 = patient1.model_dump(exclude={'address':['state']})
print(temp2)
# print(type(temp))
# print(type(temp1))
    
# print(patient1)
# print(patient1.name)
    