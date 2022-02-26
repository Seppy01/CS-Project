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

def admin_login_screen():
    cursor_obj.execute("SELECT * FROM ADMIN")
    adm_data_tup = cursor_obj.fetchall()

    while True:
        adm_user = input("Enter username: ")
        adm_user_list = []
        adm_pass_list = []

        for data_sets in adm_data_tup:
            adm_user_list.append(data_sets[1])
            
        
        if adm_user in adm_user_list:
            adm_pass = input("Enter your password: ")
            valid_us_index = adm_user_list.index(adm_user)

            for pw_data in adm_data_tup:
                adm_pass_list.append(pw_data[2])
            
            if adm_pass==adm_pass_list[valid_us_index]:
                print("Successfully logged in!")
                adm_success()                

            else:
                print("Invalid password!")
        else:
            print("Username not found!")

def adm_success():
    print("""Admin Control Panel
[1] See Complaints
[2] Add Product
[3] Remove Product
""")

    while True:
        adm_choice = int(input("\nYour choice: "))

        if adm_choice==1:
            comp_query = "SELECT * FROM COMPLAINTS"
            cursor_obj.execute(comp_query)
            comp_data = cursor_obj.fetchall()

            print("\nComplaints:-")
            for com_tup in comp_data:
                for com_rec in com_tup:                    
                    print(com_rec)

        elif adm_choice==2:
            print("""Select category:-
[1] Technology
[2] Clothing
[3] Furniture & Home Decor""")
            adm_ctg = int(input("Your choice: "))

            if adm_ctg==1:
                print(""" Choose Tech Type:- 
[1] TV
[2] Laptops
[3] Smartphones
[4] Home Appliances""")
                dec_add_tech = int(input("Your choice: "))

                if dec_add_tech==1:
                    tv_num = int(input("Enter model num: "))
                    tv_brand = input("Enter brand: ")
                    tv_res = input("Enter resolution: ")
                    tv_disp = input("Enter display size(w/unit): ")
                    tv_prize = input("Enter price: ")
                    
                    tv_query = "INSERT INTO TV VALUES({},'{}','{}','{}','{}')".format(tv_num, tv_brand, tv_res, tv_disp, tv_prize)
                    cursor_obj.execute(tv_query)
                    con_obj.commit()

                if dec_add_tech==2:
                    laptop_num = int(input("Enter model num: "))
                    laptop_brand = input("Enter brand: ")
                    laptop_type = input("Enter type: ")
                    laptop_prcs = input("Enter processor: ")
                    laptop_ram = input("Enter ram: ")
                    laptop_gpu = input("Enter gpu: ")
                    laptop_size = input("Enter display size: ")
                    laptop_price = input("Enter price: ")

                    laptop_query = "INSERT INTO LAPTOPS VALUES({},'{}','{}','{}','{}','{}','{}','{}')".format(laptop_num,
                                                                                                        laptop_brand,
                                                                                                        laptop_type,
                                                                                                        laptop_prcs,
                                                                                                        laptop_ram,
                                                                                                        laptop_gpu,
                                                                                                        laptop_size,
                                                                                                        laptop_price)
                    cursor_obj.execute(laptop_query)
                    con_obj.commit()

                if dec_add_tech==3:
                    phone_num = int(input("Enter model num: "))
                    phone_brand = input("Enter brand: ")
                    phone_name = input("Enter name: ")
                    phone_storage = input("Enter storage: ")
                    phone_colour = input("Enter colour: ")
                    phone_cam = input("Enter camera quality: ")
                    phone_price = input("Enter price: ")

                    phone_query = "INSERT INTO SMARTPHONES VALUES({},'{}','{}','{}','{}','{}','{}')".format(phone_num,
                                                                                                            phone_brand,
                                                                                                            phone_name,
                                                                                                            phone_storage,
                                                                                                            phone_colour,
                                                                                                            phone_cam,                                                                
                                                                                                            phone_price)
                    cursor_obj.execute(phone_query)
                    con_obj.commit()

                if dec_add_tech==4:
                    app_num = int(input("Enter model num: "))
                    app_brand = input("Enter brand: ")
                    app_type = input("Enter type of appliance: ")
                    app_prize = input("Enter price: ")
                    
                    app_query = "INSERT INTO APPLIANCES VALUES({},'{}','{}','{}')".format(app_num, app_brand, app_type, app_prize)
                    cursor_obj.execute(app_query)
                    con_obj.commit()

            elif adm_ctg==2:
                print("""Choose clothing type:-
[1] Men's Fashion
[2] Women's Fashion""")
                dec_add_fsh = int(input("Your choice: "))

                if dec_add_fsh==1:
                    men_num = int(input("Enter model num: "))
                    men_type = input("Enter brand: ")
                    men_colour = input("Enter colour: ")
                    men_size = input("Enter size available: ")
                    men_price = input("Enter price: ")
                    
                    men_query = "INSERT INTO MEN_FASHION VALUES({},'{}','{}','{}','{}')".format(men_num, men_type, men_colour, men_size, men_price)
                    cursor_obj.execute(men_query)
                    con_obj.commit()

                if dec_add_fsh==2:
                    women_num = int(input("Enter model num: "))
                    women_type = input("Enter brand: ")
                    women_colour = input("Enter colour: ")
                    women_size = input("Enter size available: ")
                    women_price = input("Enter price: ")
                    
                    women_query = "INSERT INTO WOMEN_FASHION VALUES({},'{}','{}','{}','{}')".format(women_num, women_type, women_colour, women_size, women_price)
                    cursor_obj.execute(women_query)
                    con_obj.commit()

            elif adm_ctg==3:
                furn_num = int(input("Enter model num: "))
                furn_type = input("Enter brand: ")
                furn_colour = input("Enter colour: ")
                furn_price = input("Enter price: ")
                
                furn_query = "INSERT INTO FURNDECOR VALUES({},'{}','{}','{}','{}')".format(furn_num, furn_type, furn_colour, furn_price)
                cursor_obj.execute(furn_query)
                con_obj.commit()

        elif adm_choice==3:
            pass

        else:
            print("Invalid Choice!")


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
[4] Furniture & Home Decor""")

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
            
                elif catg_choice==2:
                    print("""Products Available:- 
[1] Fruits
[2] Vegetables
[3] Beverages
[4] Dairy Products
""")

                    food_choice = int(input("Enter your choice: "))
                    
                    if food_choice==1:
                        fruits_query = "SELECT FRUITS FROM FOOD"
                        cursor_obj.execute(fruits_query)
                        fruits_data = cursor_obj.fetchall()

                        print("Fruits Available:-")
                        for i in fruits_data:
                            print(i[0])

                        fruit_purchase = input("Enter fruit for purchase: ")
                        print(f"Fruit to be purchased: {fruit_purchase}")
                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        fruit_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if fruit_next_option==1:
                            pass

                        elif fruit_next_option==2:
                            transaction()

                    elif food_choice==2:
                        vegs_query = "SELECT VEGETABLES FROM FOOD"
                        cursor_obj.execute(vegs_query)
                        vegs_data = cursor_obj.fetchall()

                        print("Vegetables Available:-")
                        for i in vegs_data:
                            print(i[0])

                        vegs_purchase = input("Enter vegetables for purchase: ")
                        print(f"Vegetables to be purchased: {vegs_purchase}")
                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        vegs_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if vegs_next_option==1:
                            pass

                        elif vegs_next_option==2:
                            transaction()

                    elif food_choice==3:
                        bvgs_query = "SELECT BEVERAGES FROM FOOD"
                        cursor_obj.execute(bvgs_query)
                        bvgs_data = cursor_obj.fetchall()

                        print("Beverages Available:-")
                        for i in bvgs_data:
                            print(i[0])

                        bvgs_purchase = input("Enter beverages for purchase: ")
                        print(f"Beverages to be purchased: {bvgs_purchase}")
                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        bvgs_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if bvgs_next_option==1:
                            pass

                        elif bvgs_next_option==2:
                            transaction()

                    elif food_choice==4:
                        dairy_query = "SELECT DAIRY_PRODUCTS FROM FOOD"
                        cursor_obj.execute(dairy_query)
                        dairy_data = cursor_obj.fetchall()

                        print("Dairy Products Available:-")
                        for i in dairy_data:
                            print(i[0])

                        dairy_purchase = input("Enter dairy products for purchase: ")
                        print(f"Dairy Products to be purchased: {dairy_purchase}")
                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        dairy_next_option = int(input("Your choice: "))

                        #Add to cart under development
                        if dairy_next_option==1:
                            pass

                        elif dairy_next_option==2:
                            transaction()

                    else:
                        print("Invalid choice!")

                elif catg_choice==3:
                    print("""Clothing Categories:- 
[1] Men's Fashion
[2] Women's Fashion
""")
                
                    cl_catg = int(input("Your choice: "))
                    
                    if cl_catg==1:
                        men_query = "SELECT * FROM MEN_FASHION"
                        cursor_obj.execute(men_query)
                        men_data = cursor_obj.fetchall()

                        print("Men's Clothings Available:-")
                        for i in men_data:
                            print(i)

                        while True:
                            men_sr_num = int(input("Enter number: "))
                            
                            if men_sr_num in range(1,9):
                                break

                            else:
                                print("Invalid Model Number")

                        cloth_details = "SELECT * FROM MEN_FASHION WHERE SRNO={}".format(men_sr_num)
                        cursor_obj.execute(cloth_details)
                        cloth_tup = cursor_obj.fetchall()
                        
                        print("\n--------------------------")
                        print("Your selected clothing:-")
                        for i in cloth_tup:
                            print(f"""Sr No: {i[0]}
Type: {i[1]}
Colour: {i[2]}
Size Available: {i[3]}
Price: {i[4]}
--------------------------""")

                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        men_clth_next = int(input("Your choice: "))

                        #Add to cart under development
                        if men_clth_next==1:
                            pass

                        elif men_clth_next==2:
                            transaction()

                    elif cl_catg==2:
                        women_query = "SELECT * FROM WOMEN_FASHION"
                        cursor_obj.execute(women_query)
                        women_data = cursor_obj.fetchall()

                        print("Women's Clothings Available:-")
                        for i in women_data:
                            print(i)

                        while True:
                            women_sr_num = int(input("Enter number: "))
                            
                            if women_sr_num in range(1,9):
                                break

                            else:
                                print("Invalid Model Number")

                        wocloth_details = "SELECT * FROM WOMEN_FASHION WHERE SRNO={}".format(men_sr_num)
                        cursor_obj.execute(wocloth_details)
                        wocloth_tup = cursor_obj.fetchall()
                        
                        print("\n--------------------------")
                        print("Your selected clothing:-")
                        for i in wocloth_tup:
                            print(f"""Sr No: {i[0]}
Type: {i[1]}
Colour: {i[2]}
Size Available: {i[3]}
Price: {i[4]}
--------------------------""")

                        print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                        women_clth_next = int(input("Your choice: "))

                        #Add to cart under development
                        if women_clth_next==1:
                            pass

                        elif women_clth_next==2:
                            transaction()

                    else:
                        print("Invalid choice!")

                elif catg_choice==4:
                    furn_query = "SELECT * FROM FURNDECOR"
                    cursor_obj.execute(furn_query)
                    furn_data = cursor_obj.fetchall()
                    
                    for products in furn_data:
                        print(products)
                    
                    while True:
                            furn_choice = int(input("Enter number: "))
                            
                            if furn_choice in range(1,9):
                                break

                            else:
                                print("Invalid Model Number")

                    furn_details = "SELECT * FROM FURNDECOR WHERE SRNO={}".format(furn_choice)
                    cursor_obj.execute(furn_details)
                    furn_tup = cursor_obj.fetchall()
                    
                    print("\n--------------------------")
                    print("Your selected furniture:-")
                    for i in furn_tup:
                        print(f"""Sr No: {i[0]}
Type: {i[1]}
Colour: {i[2]}
Price: {i[3]}
--------------------------""")

                    print("""\n[1] Add to cart
[2] Buy
[3] Exit""")
                    furn_next = int(input("Your choice: "))

                    #Add to cart under development
                    if furn_next==1:
                        pass

                    elif furn_next==2:
                        transaction()

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
        card_num = input("Enter card number(XXXX-XXXX-XXXX): ")
        card_exp = input("Enter card expiry date(MM/YY): ")
        card_cvv = int(input("Enter card CVV(XXX): "))

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


