
def culture_and_countries():
    while True:
        print()
        print("=== Culture & Countries ===")
        print("Questions:")
        print("[a] Which country has the highest mental health issues?")
        print("[b] Is there an increase in mental health awareness in higher income countries than lower income countries?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Which country has the highest mental health issues? ---")
            # Your method call for the question here
        elif choice == 'b':
            print("--- Is there an increase in mental health awareness in higher income countries than lower income countries? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def gender():
    while True:
        print()
        print("=== Gender ===")
        print("[a] Which gender is more likely to get treatment for mental related issues? (working specifically in tech companies)")
        print("[b] Which gender is more likely to report mental health related issues?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Which gender is more likely to get treatment for mental related issues? (working specifically in tech companies) ---")
            # Your method call for the question here
        elif choice == 'b':
            print("--- Which gender is more likely to report mental health related issues? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def age():
    while True:
        print()
        print("=== Age ===")
        print("Questions:")
        print("[a] Which age group of people is more likely to experience mental health issues?")
        print("[b] Are younger employees more likely to report experiencing mental health related issues and are they more likely to seek treatment for it?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Which age group of people is more likely to experience mental health issues? ---")
            # Your method call for the question here
        elif choice == 'b':
            print("--- Are younger employees more likely to report experiencing mental health related issues and are they more likely to seek treatment for it? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def company_culture():
    while True:
        print()
        print("=== Company Culture ===")
        print("Questions:")
        print("[a] Do employees in companies with wellness programs report lower levels of work interference because of their mental health?")
        print("[b] Does the staff in the company have a good or bad image on mental health?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Do employees in companies with wellness programs report lower levels of work interference because of their mental health? ---")
            # Your method call for the question here
        elif choice == 'b':
            print("--- Does the staff in the company have a good or bad image on mental health? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def work_environment():
    while True:
        print()
        print("=== Work Environment ===")
        print("Questions:")
        print("[a] Does remote working have a positive/negative effect on mental health (compared to working in an office)?")
        print("[b] Are employees in larger companies more likely to discuss mental health related issues with co-workers and/or supervisors? And does this have a positive/negative outcome?")
        print("[c] Are employees in tech companies more/less likely to seek help compared to those in non-tech companies?")
        print("[d] Does being self-employed increase the chances of mental health?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Does remote working have a positive/negative effect on mental health (compared to working in an office)? ---")
            # Your method call for the question here
        elif choice == 'b':
            print("--- Are employees in larger companies more likely to discuss mental health related issues with co-workers and/or supervisors? And does this have a positive/negative outcome? ---")
            # Your method call for the question here
        elif choice == 'c':
            print("--- Are employees in tech companies more/less likely to seek help compared to those in non-tech companies? ---")
            # Your method call for the question here
        elif choice == 'd':
            print("--- Does being self-employed increase the chances of mental health? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def main():
    while True:
        
        print()
        print("=== MENU ===")
        print("[1] Culture & Countries")
        print("[2] Gender")
        print("[3] Age")
        print("[4] Company Culture")
        print("[5] Work Environment")
        print("[0] Exit the program")
        
        option = input("Enter your option: ")
          
        if option == "0":
            print("Exiting the program...")
            break
        elif option == "1":
            culture_and_countries()
        elif option == "2":
            gender()
        elif option == "3":
            age()
        elif option == "4":
            company_culture()
        elif option == "5":
            work_environment()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()





