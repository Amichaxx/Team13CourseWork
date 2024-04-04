import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

def print_menu():
    print()
    print("=== MENU ===")
    print("[1] Culture & Countries")
    print("[2] Gender")
    print("[3] Age")
    print("[4] Company Culture")
    print("[5] Work Environment")
    print("[0] Exit the program")

def get_option():
    while True:
        try:
            option = int(input("Enter your option: "))
            if 0 <= option <= 5:
                return option
            else:
                print("Invalid option. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def culture_and_countries(): #Tsiko, Khushi
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

def gender(): #Lily, Zaakiyah
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

def age(): #Lily, Zaakiyah
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

def company_culture(): #Haaniah, Amina, Rida
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
            work_interference_map = {1: 'Often', 2: 'Sometimes', 3: 'Rarely', 4: 'Never'}
            with_wellness_program = data[data['wellness_program'] == 1]
            without_wellness_program = data[data['wellness_program'] == 2]
            
            with_work_interference_counts = with_wellness_program['work_interfere'].value_counts().sort_index()
            without_work_interference_counts = without_wellness_program['work_interfere'].value_counts().sort_index()
            
            with_work_interference_counts.index = with_work_interference_counts.index.map(work_interference_map)
            without_work_interference_counts.index = without_work_interference_counts.index.map(work_interference_map)
            
            work_interference_labels = with_work_interference_counts.index
            
            plt.figure(figsize=(10, 5))
            
            plt.subplot(1, 2, 1)
            plt.pie(with_work_interference_counts, labels=work_interference_labels, autopct='%1.1f%%', startangle=90)
            plt.title('Employee Work Interference With Wellness Program')

            plt.subplot(1, 2, 2)
            plt.pie(without_work_interference_counts, labels=work_interference_labels, autopct='%1.1f%%', startangle=90)
            plt.title('Employee Work Interference Without Wellness Program')
            
            plt.legend(work_interference_labels, loc='center left', bbox_to_anchor=(1, 0.5))
            
            plt.tight_layout()
            plt.show()

        elif choice == 'b':
            print("--- Does the staff in the company have a good or bad image on mental health? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def work_environment(): #Haaniah, Amina, Rida
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
            tech_yes_count = data[(data['tech_company'] == 'Yes') & (data['seek_help'] == 1)].shape[0]
            tech_no_count = data[(data['tech_company'] == 'Yes') & (data['seek_help'] == 2)].shape[0]
            non_tech_yes_count = data[(data['tech_company'] == 'No') & (data['seek_help'] == 1)].shape[0]
            non_tech_no_count = data[(data['tech_company'] == 'No') & (data['seek_help'] == 2)].shape[0]

            labels = ['Yes', 'No']
            tech_counts = [tech_yes_count, tech_no_count]
            non_tech_counts = [non_tech_yes_count, non_tech_no_count]
            x = range(len(labels))
            width = 0.35

            plt.bar(x, tech_counts, width=width, color='blue', label='Tech Company')
            plt.bar([pos + width for pos in x], non_tech_counts, width=width, color='red', label='Non-Tech Company')

            plt.xlabel('Seek Help')
            plt.ylabel('Responses')
            plt.title('Likelihood of Seeking Help by Company Type')
            plt.xticks([pos + width / 2 for pos in x], labels)
            plt.legend()
            plt.grid(True)
            plt.legend()
            plt.show()

        elif choice == 'd':
            print("--- Does being self-employed increase the chances of mental health? ---")
            # Your method call for the question here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please select a valid option.")

def main():
    while True:
        print_menu()
        option = get_option()

        if option == 0:
            print("Exiting the program...")
            break
        elif option == 1:
            culture_and_countries()
        elif option == 2:
            gender()
        elif option == 3:
            age()
        elif option == 4:
            company_culture()
        elif option == 5:
            work_environment()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

