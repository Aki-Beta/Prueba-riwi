from funcions import *

def menu_show():
   
    menu = True
    while menu:
        
        print("\n" + "="*30)
        print("SCHOOL RIWI")
        print("="*30)
        print("1. Register student")
        print("2. Consult list of student")
        print("3. Search student (ID or name)")
        print("4. Update information")
        print("5. Delete student")
        print("6. Exit")
        print("—"*30)
    
        try:
            option = int(input("Elige una opción: "))
        except ValueError:
            print("Option invalidate. Choice a number between 1 and 6")
            continue     
        
        if option == 1:
            student_register()
        elif option == 2:
            consult_list ()
        elif option == 3:
           search_student ()
        elif option == 4:
            update_information()
        elif option == 5:
            delete_student()
        elif option == 6:
            print ("See you later! Good day.")
            break
        else: 
            print("Select a valid option")
            
menu_show()
            
                
    
        
            
            
        
                
