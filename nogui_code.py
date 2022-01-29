#Project without GUI code:-
from sys import exit
import mysql.connector as mysq
con_obj = mysq.connect(host="localhost", user="root", password="root", database="project")
cursor_obj = con_obj.cursor()

#Working as intended
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

#Under a subject of R&D
def admin_login_screen():
    pass

#Working as intended
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
            con_obj.close()
            exit()

        elif user_choice==4:
            complaints()

        else:
            print("Invalid Choice!")

#Working as intended
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
                success_login()                

            else:
                print("Invalid password!")
        else:
            print("Username not found!")
                        

#Working as intended
def complaints():
    complaint = input("Enter your complaint: ")

    query = "INSERT INTO COMPLAINTS VALUES('{}')".format(complaint)
    cursor_obj.execute(query)

    #Commit function used when insert/update/delete queries used
    con_obj.commit()                                                       


#Under development
def success_login():
    print("""\nWelcome user to our service!!

[1] Product Categories 
[2] Your order history
[3] Cart
[4] Go Back
[5] Exit""")

    user_choice = int(input("Your choice: "))

    if user_choice==1:
        print("""Product Categories:-
[1] Technology
[2] Groceries
[3] Clothing
[4] Home Decor""")

        catg_choice = int(input("Your choice: "))

        if user_choice==1:
            print("""Products Available:- 
[1] TVs
[2] Laptops
[3] Smartphones""")

            tech_choice = int(input("Your choice: "))
            
            if tech_choice==1:
#                 print("""---------------------------------
# Brands Available:-
# [1] SungSam
# [2] GL TV

# Resolution Available:-
# [1] FHD - 1920x1080
# [2] UHD - 3840x2160
# [3] 4K  - 4096x2160

# Display size:-
# [1] 65 inches
# [2] 60 inches
# [3] 55 inches
# ---------------------------------\n
# """)          
                print("TV Models Available:-")
                tv_choice_query = "SELECT * FROM TV"
                cursor_obj.execute(tv_choice_query)
                tv_data_tup = cursor_obj.fetchall()
                
                for i in tv_data_tup:
                    print(i)
                
                model_num = int(input("Enter model number: "))

                print("""[1] Add to cart
[2] Buy
[3] Exit""")
                next_option = int(input("Your choice: "))

                if next_option==1:
                    pass

                elif next_option==2:
                    transaction()

                # tv_res_choice = int(input("Your resolution choice: "))
                # tv_disp_choice = int(input("Your display size choice: "))

                # if tv_res_choice==1:
                #     res_choice = "FHD"

                # elif tv_res_choice==2:
                #     res_choice = "UHD"

                # elif tv_res_choice==3:
                #     res_choice = "4K"

                # disp_size = str(tv_disp_choice) + ' inches'
                # tv_choice_query = "SELECT * FROM TV WHERE RESOLUTION='{}' AND DISPLAY_SIZE='{}'".format(res_choice, disp_size)
                # cursor_obj.execute(tv_choice_query)
                # tv_data_tup = cursor_obj.fetchall()
                # print(tv_data_tup)
                # exit()

#                 if tv_brand_choice==1:
#                     print("""[1] SumSang 57 Inches UHD
# [2] SumSang 65 Inches 4K""")
#                 #Under development
#                 elif tv_brand_choice==2:
#                     pass
                
#                 #Under development
#                 elif tv_brand_choice==3:
#                     pass

#                 else:
#                     print("Invalid Choice!")

            #Under development
            elif tech_choice==2:
                pass
            
            #Under development
            elif tech_choice==3:
                pass

            else:
                print("Invalid Choice!")
        
        #Under development
        elif user_choice==2:
            pass
        
        #Under development
        elif user_choice==3:
            pass
        
        #Under development
        elif user_choice==4:
            pass

        else:
            print("Invalid Choice!")

    #Under development
    elif user_choice==2:
        pass
    
    #Under development
    elif user_choice==3:
        pass

    elif user_choice==4:
        log_in()

    elif user_choice==5:
        exit()

    else:
        print("Invalid choice!")

def transaction():
    print("""Mode of Transaction:-
[1] Credit Card
[2] Cash On Delivery""")

    while True:
        transaction_mode = int(input("Your choice: "))
        
        if transaction_mode==1:
            credit_card()

def credit_card():
    card_num = int(input("Enter card number: "))
    card_exp = input("Enter card expiry date: ")
    card_cvv = int(input("Enter card CVV: "))

if __name__ == '__main__':
    print("""=========================================
Welcome to Online Shopping Service!!
=========================================""")
    type_login()


