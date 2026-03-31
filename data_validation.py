def insert_patient_data(name : str,age : int):
    if type(name) == str and type(age) == int:
        if (age<0):
            print("Age cannot be negative")
        else:
            
            print(name)
            print(age)
            print('inserted into database')
            print(type(name))
    else:
        raise TypeError('Incorrect data type')

insert_patient_data("Abhinandan",21)

def update_patient_data(name : str,age : int):
    if type(name) == str and type(age) == int:
        print(name)
        
    
        print(age)
        print('updated')
        print(type(name))
    else:
        raise TypeError('Incorrect data type')