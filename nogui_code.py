#Project without GUI code:-
from sys import exit
import mysql.connector as mysq
con_obj = mysq.connect(host="localhost", user="root", password="root", database="project")
cursor_obj = con_obj.cursor()

def type_login():
    print("""Select the type of login:-
---------------------------------
[1] Admin
[2] User
---------------------------------""")
    type_choice = int(input("Your choice: "))

    if type_choice==1:
        admin_login_screen()

    if type_choice==2:
        user_login_screen()

#Under a subject of research and development
def admin_login_screen():
    pass

def user_login_screen():
    while True:
        print("""\nUSER LOGIN
[1] Log-in 
[2] Register
[3] Exit
[4] File a complaint""")
        user_choice = int(input("\nYour choice: "))

        if user_choice==1:
            log_in()

        elif user_choice==2:
            pass

        elif user_choice==3:
            print("\nThank you for using the online shopping service!!")
            exit()

        elif user_choice==4:
            complaints()

        else:
            print("Invalid Choice!")

def log_in():
    cursor_obj.execute("SELECT * FROM USER_DATA")
    user_data_tup = cursor_obj.fetchall()

    while True:
        username = input("Enter your username: ")
        username_list = []
        password_list = []

        for data_sets in user_data_tup:
            username_list.append(data_sets[0])
            
        
        if username in username_list:
            password = input("Enter your password: ")
            valid_us_index = username_list.index(username)

            for pw_data in user_data_tup:
                password_list.append(pw_data[1])
            
            if password==password_list[valid_us_index]:
                print("Successfully logged in!")
                exit()

            else:
                print("Invalid password!")
        else:
            print("Username not found!")
            
    #print(user_data_tup)

# if con_obj.is_connected():
#     print("Successfully connected")

#Under a subject of research and development
def complaints():
    complaint = input("Enter your complaint: ")

    query = "INSERT INTO USER_COMPLAINTS VALUES(%s)"%(complaint)
    cursor_obj.execute(query)
    user_complaints = cursor_obj.fetchall()
    print(user_complaints)




if __name__ == '__main__':
    print("""=========================================
Welcome to Online Shopping Service!!
=========================================""")

    type_login()

