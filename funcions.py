import os
from app import *

students = []

def validate_number(massage, type = int):
    
    next = True
    while next:
        try:
            if type == "int":
                value = int(input(massage))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def student_register():
    
    id = input("Enter ID:")
    name_student = input ("Enter student name: ")
    age_student = validate_number("Enter student age: ", "int")
    program = input("Enter student program: ")
    state = input ("If student is active, writing (yes/no): ")
    
    student = {
        "ID": id,
        "name": name_student, 
        "age": age_student,
        "program ": program, 
        "state": state
    }
    student.append()
    return 

def consult_list (alumn : list):
   
  for c in range(len(alumn)):
    print(alumn)

        
def search_student (ID, name_student, students: list):
    
    search = input ("Enter the ID o student name: ")
    
    for s in students():
        if s ['ID'] == search or students ['name'] == search:
            print (s)
        else: 
            print("Incorrect information.")
        
        
     
        
    
def update_information (): 
    asdasd = 1
    
def delete_student ():
    asdasd = 1
    
