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
    while True:
        user_choice_main = int(input("Your choice: "))

        if user_choice_main==1:
            print("""Product Categories:-
[1] Technology
[2] Food
[3] Clothing
[4] Home Decor""")

            while True:
                catg_choice = int(input("Your choice: "))

                if catg_choice==1:
                    print("""Products Available:- 
[1] TVs
[2] Laptops
[3] Smartphones
[4] Home Appliances""")

                    tech_choice = int(input("Your choice: "))
                    
                    if tech_choice==1:               
                        print("TV Models Available:-")
                        tv_choice_query = "SELECT * FROM TV"
                        cursor_obj.execute(tv_choice_query)
                        tv_data_tup = cursor_obj.fetchall()
                        
                        for i in tv_data_tup:
                            print(i)
                        
                        while True:
                            tv_model_num = int(input("Enter model number: "))
                            
                            if tv_model_num in range(1,9):
                                break

                            else:
                                print("Invalid Model Number")

                        display_specs = "SELECT * FROM TV WHERE MODELNO={}".format(tv_model_num)
                        cursor_obj.execute(display_specs)
                        specs_tup = cursor_obj.fetchall()
                        
                        print("\n--------------------------")
                        print("Your selected model:-")
                        for i in specs_tup:
                            print(f"""Model No: {i[0]}
Brand: {i[1]}
Resolution: {i[2]}
Display Size: {i[3]}
Price: {i[4]}
--------------------------""")

                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        tv_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if tv_next_option==1:
                            pass

                        elif tv_next_option==2:
                            transaction()

                    #Under development
                    elif tech_choice==2:
                        print("Laptop Models Available:-")
                        laptop_choice_query = "SELECT * FROM LAPTOPS"
                        cursor_obj.execute(laptop_choice_query)
                        laptop_data_tup = cursor_obj.fetchall()

                        for lap_mod in laptop_data_tup:
                            print(lap_mod)
                        
                        while True:
                            lap_model_num = int(input("Enter model number: "))
                            
                            if lap_model_num in range(1,9):
                                break

                            else:
                                print("Invalid Model Number")

                        lap_display_specs = "SELECT * FROM LAPTOPS WHERE MODELNO={}".format(lap_model_num)
                        cursor_obj.execute(lap_display_specs)
                        lap_specs_tup = cursor_obj.fetchall()
                        
                        print("\n--------------------------")
                        print("Your selected model:-")
                        for i in lap_specs_tup:
                            print(f"""Model No: {i[0]}
Brand: {i[1]}
Type: {i[2]}
Processor: {i[3]}
Ram: {i[4]}
GPU: {i[5]}
Display Size: {i[6]}
Price: {i[7]}
--------------------------""")

                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        lap_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if lap_next_option==1:
                            pass

                        elif lap_next_option==2:
                            transaction()

                    #Under development
                    elif tech_choice==3:
                        print("Smartphone Models Available:-")
                        phone_choice_query = "SELECT * FROM SMARTPHONES"
                        cursor_obj.execute(phone_choice_query)
                        phone_data_tup = cursor_obj.fetchall()

                        for phone_mod in phone_data_tup:
                            print(phone_mod)
                        
                        while True:
                            phone_model_num = int(input("Enter model number: "))
                            
                            if phone_model_num in range(1,11):
                                break

                            else:
                                print("Invalid Model Number")

                        phone_display_specs = "SELECT * FROM SMARTPHONES WHERE MODELNO={}".format(phone_model_num)
                        cursor_obj.execute(phone_display_specs)
                        phone_specs_tup = cursor_obj.fetchall()
                        
                        print("\n--------------------------")
                        print("Your selected model:-")
                        for i in phone_specs_tup:
                            print(f"""Model No: {i[0]}
Brand: {i[1]}
Name: {i[2]}
Storage: {i[3]}
Colour: {i[4]}
Camera: {i[5]}
Price Size: {i[6]}
--------------------------""")

                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        phone_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if phone_next_option==1:
                            pass

                        elif phone_next_option==2:
                            transaction()


                    elif tech_choice==4:
                        print("Home Appliances Products Available:-")
                        appl_choice_query = "SELECT * FROM APPLIANCES"
                        cursor_obj.execute(appl_choice_query)
                        appl_data_tup = cursor_obj.fetchall()

                        for appl_mod in appl_data_tup:
                            print(appl_mod)

                        while True:
                            appl_model_num = int(input("Enter model number: "))
                            
                            if appl_model_num in range(1,9):
                                break

                            else:
                                print("Invalid Model Number")

                        appl_specs = "SELECT * FROM APPLIANCES WHERE MODELNO={}".format(appl_model_num)
                        cursor_obj.execute(appl_specs)
                        appl_specs_tup = cursor_obj.fetchall()

                        print("\n--------------------------")
                        print("Your selected model:-")
                        for i in appl_specs_tup:
                            print(f"""Model No: {i[0]}
Brand: {i[1]}
Type: {i[2]}
Price: {i[3]}
--------------------------""")

                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")

                        appl_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if appl_next_option==1:
                            pass

                        elif appl_next_option==2:
                            transaction()

                    else:
                        print("Invalid Choice!")
            
                #Under development
                elif catg_choice==2:
                    print("""Products Available:- 
[1] Groceries
[2] Beverages
[3] Dairy Products
[4] Snacks""")

                    food_choice = int(input("Enter your choice: "))
                    
                    if food_choice==1:
                        pass

                    elif food_choice==2:
                        pass

                    elif food_choice==3:
                        pass

                    elif food_choice==4:
                        pass

                    else:
                        print("Invalid choice!")

                #Under development
                elif catg_choice==3:
                    pass
                
                #Under development
                elif catg_choice==4:
                    pass

                else:
                    print("Invalid Choice!")

        #Under development
        elif user_choice_main==2:
            pass
        
        #Under development
        elif user_choice_main==3:
            pass

        elif user_choice_main==4:
            log_in()

        elif user_choice_main==5:
            exit()

        else:
            print("Invalid choice!")

#Working as intended
def transaction():
    print("""Mode of Transaction:-
[1] Credit Card
[2] Cash On Delivery""")

    while True:
        transaction_mode = int(input("Your choice: "))
        
        if transaction_mode==1:
            credit_card()

        elif transaction_mode==2:
            cash_delivery()

#Working as intended
def cash_delivery():
    print("""Payment Method: Cash-On-Delivery

Additional charges(for cash on delivery mode): 10 AED
-------------------------------------------------------------------------

[1] Continue Shopping
[2] Exit""")

    while True:
        trans_next = int(input("Your choice: "))

        if trans_next==1:
            success_login()
        
        elif trans_next==2:
            print("Thank you for using our shopping service!!\nHave a great day ahead!")
            print("-------------------------------------------------------------------------")
            exit()

#Working as intended
def credit_card():
    while True:
        card_num = input("Enter card number: ")
        card_exp = input("Enter card expiry date: ")
        card_cvv = int(input("Enter card CVV: "))

        check_card_validity = "select exists(select * from credit_card_details where card_num='{}' and card_exp='{}' and card_cvv={})".format(card_num, card_exp, card_cvv)
        cursor_obj.execute(check_card_validity)
        validity = cursor_obj.fetchone()

        for i in validity:
            if i==1:
                print("\nPayment has been successfully made!\nThank you for shopping with us!\n")
                print("""---------------------------------
[1] Continue Shopping
[2] Exit""")    
                while True:
                    trans_next = int(input("Your choice: "))

                    if trans_next==1:
                        success_login()
                    
                    elif trans_next==2:
                        print("Thank you for using our shopping service!!\nHave a great day ahead!")
                        print("-------------------------------------------------------------------------")
                        exit()
                    
                    else:
                        print("Invalid choice!")
            else:
                print("Invalid card information!")


if __name__ == '__main__':
    print("""=========================================
Welcome to Online Shopping Service!!
=========================================""")
    type_login()


