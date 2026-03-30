##With this line of code we call the functions contained in the functions file##
from src.functions import *
print("\n")
print("======Welcome to the student management program======  \n")
##Here we use a while loop for the interactive menu to return to it until option 8 is used##
while True:
    print("==student manager== :\n")
    print("-----------------------")
    print("|1.add student         |")
    print("|2.Delete student      |")
    print("|3.update student      |")
    print("|4.show student        |")
    print("|5.show full record    |")
    print("|6.save student list   |")
    print("|7.upload student list |")
    print("|8.Exit                |\n")
    print("-----------------------")
##Here we enter the option we need##
    option = input("Choose a valid option : \n")

##Here we use conditionals for the menu options; depending on the option, a function will be called##
    if option =="1":
        name=input ("Enter name: \n")
        id=int(input("enter the ID : \n"))
        age=int(input("Enter age : \n"))
        program =input("Enter the program it belongs to : \n")
        status=input("Enter student's status: \n")
        add_student(name, id, age, program, status)

    elif option =="2":
        name=input("Enter the name of the student to be removed: \n")
        delete_student(name)

    elif option=="3":
        name=input("Enter the name of the student to be updated: \n")
        id=int(input("enter new ID: \n"))
        age=int(input("enter new age: \n"))
        program=input("enter new program: \n")
        status=input("enter new status:  \n")
        update_student(name, id, age, program, status)

    elif option=="4":
        name=input("Enter the name of the student to be display: \n")
        show_student(name)

    elif option == "5":
        full_record()


    elif option == "6":
        list_name=input("Enter the file name to save the student list (example: studend_list.csv): \n")
        save_list(list_name)

    elif option=="7":
        list_name= input("Enter the name of the student list to load (example: student.csv):  \n")
        upload_list(list_name)
##This particular option breaks the while loop and allows us to exit the program##
    elif option == "8":
        print("===...Exiting the program...===")
        break
    else:
        print("==Invalid option. Please try again.== \n")