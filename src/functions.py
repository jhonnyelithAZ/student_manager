#From this file we will import all the functions that we will use in main.py#


import csv

##We use a list to store the data we will use##
student_list=[]

##With this function we add a student to the list##
def add_student(name, id, age, program, status):
    student = {
        "name": name,
        "ID": id,
        "age": age,
        "program": program,
        "status" : status
        }
    student_list.append(student)

##With this function we delete a student##

def delete_student(name):
    for student in student_list:
        if student['name']== name:
            student_list.remove(student)
            print(f"==student {name} DELETE.==\n")

##With this function we update a student's data##
def update_student(name, id=None, age=None, program=None, status=None ):
    for student in student_list:
        if student['name']==name:
            if id is not None:
                student['ID']=id
        if age is not None:
            student['age']=age
        if program is not None:
            student['program']==program
        if status is not None:
            status['status']==status
        print(f"....student {name} UPDATE.... \n ")
        return
##If the student's name does not appear for modification...return to menu##
    print(f"....STUDENT{name} NO FOUND....\n")


##function to display a specific student##
def show_student(name):
    for student in student_list:
        if student['name']==name:
            print(f">>Name: {student['name']}\n, >>ID: {student['ID']}\n, >>age: {student['age']}\n, >>program: {student['program']}\n, >>status: {student['status']}\n")
            return
    print(f"...Student {name} NO FOUND...")

##Function to display all students registered so far.##
def full_record():
    for student in student_list:
        print(f">>Name:{student['name']}\n, >>ID: {student['ID']}\n, >>age: {student['age']}\n, >>program:{student['program']}\n, >>status:{student['status']}\n")

##Function to save the complete list of students registered so far through a CSV file.##  
def save_list(list_name):
    with open(list_name, 'w', newline='') as csvfile:
        fieldnames=['name', 'ID', 'age', 'program', 'status']
        writer= csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow(student)
            print("......list saved successfully......")


##This function allows us to load a list of students from a previously created CSV file##
def upload_list(list_name):
    try:
        with open(list_name, 'r',newline='') as csvfile:
            reader= csv.DictReader(csvfile)
            student_list.clear()
            for row in reader:
                student={
                    'name': row['name'],
                    'ID': int(row['ID']),
                    'age': int(row['age']),
                    'program': row['program'],
                    'status' : row['status']
                }
                student_list.append(student)
                print(f"studend upload: {student}\n")
        print(f"studend list uploaded from {list_name}\n")
    except FileNotFoundError:
        print(f"===Error: THE LIST NAME{list_name} NO FOUND...===")
    except Exception as e:
        print(f"==ERROR LOADING INVENTORY{e}==")
