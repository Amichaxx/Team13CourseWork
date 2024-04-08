import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

def remoteWorking(): #hani q1
    # --- Does remote working have a positive/negative effect on mental health (compared to working in an office)? ---

    remote = (data[data['remote_work']=='Yes'].shape[0])/100 # 299 responses
    office = (data[data['remote_work']=='No'].shape[0])/100 # 689 repsonses
    
    fig, ax = plt.subplots()
    ax.set_title("The Effects of Remote Working on Mental Health")

    x_labels = ['Remote', 'Office']
    y_labels = [remote, office]

    ax.bar(x_labels, y_labels, color=['hotpink', 'pink'])
   
    plt.xlabel('Work Area')
    plt.ylabel('No. of Responses (hundreds)')

    plt.show()
   
def DiscussionInCompanies(): #hani q2
    # --- Are employees in larger companies more likely to discuss mental health related issues with co-workers and/or supervisors? And does this have a positive/negative outcome? ---
    # answer columns: coworkers, supervisors, mental_health_consequence, phys_health_consequence
    
    # Figure 2: PIE CHART
    small_1_mental = data[(data['no_employees']=='Small') & (data['mental_health_consequence']==1)] # yes - 139 responses
    small_2_mental = data[(data['no_employees']=='Small') & (data['mental_health_consequence']==2)] # no - 234 responses
    small_3_mental = data[(data['no_employees']=='Small') & (data['mental_health_consequence']==3)] # maybe - 211 responses
    
    small_1_phys = data[(data['no_employees']=='Small') & (data['phys_health_consequence']==1)] # yes
    small_2_phys = data[(data['no_employees']=='Small') & (data['phys_health_consequence']==2)] # no
    small_3_phys = data[(data['no_employees']=='Small') & (data['phys_health_consequence']==3)] # maybe
    
    # Figure 1: BAR CHART
    small_1_coworkers = data[(data['no_employees']=='Small') & (data['coworkers']==1)].shape[0] # yes - 118
    small_2_coworkers = data[(data['no_employees']=='Small') & (data['coworkers']==2)].shape[0] # some of them - 360
    small_3_coworkers = data[(data['no_employees']=='Small') & (data['coworkers']==3)].shape[0] # no - 106 
    
    small_1_supervisor = data[(data['no_employees']=='Small') & (data['supervisor']==1)].shape[0] # yes
    small_2_supervisor = data[(data['no_employees']=='Small') & (data['supervisor']==2)].shape[0] # some of them 
    small_3_supervisor = data[(data['no_employees']=='Small') & (data['supervisor']==3)].shape[0] # no 
    
    medium_1_coworkers = data[(data['no_employees']=='Medium') & (data['coworkers']==1)].shape[0] # yes - 24
    medium_2_coworkers = data[(data['no_employees']=='Medium') & (data['coworkers']==2)].shape[0] # some of them - 94
    medium_3_coworkers = data[(data['no_employees']=='Medium') & (data['coworkers']==3)].shape[0] # no - 22
    
    medium_1_supervisor = data[(data['no_employees']=='Medium') & (data['supervisor']==1)].shape[0] # yes
    medium_2_supervisor = data[(data['no_employees']=='Medium') & (data['supervisor']==2)].shape[0] # some of them 
    medium_3_supervisor = data[(data['no_employees']=='Medium') & (data['supervisor']==3)].shape[0] # no 
    
    large_1_coworkers = data[(data['no_employees']=='Large') & (data['coworkers']==1)].shape[0] # yes - 35
    large_2_coworkers = data[(data['no_employees']=='Large') & (data['coworkers']==2)].shape[0] # some of them - 154
    large_3_coworkers = data[(data['no_employees']=='Large') & (data['coworkers']==3)].shape[0] # no - 75
    
    large_1_supervisor = data[(data['no_employees']=='Large') & (data['supervisor']==1)].shape[0] # yes
    large_2_supervisor = data[(data['no_employees']=='Large') & (data['supervisor']==2)].shape[0] # some of them 
    large_3_supervisor = data[(data['no_employees']=='Large') & (data['supervisor']==3)].shape[0] # no 
    
    
    x_labels_pie = ['Yes', 'No', 'Maybe']
    x_labels_bar = ['Yes', 'Some', 'No']
    
    y_labels_s_mental = [small_1_mental, small_2_mental, small_3_mental]
    y_labels_s_phys = [small_1_phys, small_2_phys, small_3_phys]
    
    y_labels_s_coworkers = [small_1_coworkers, small_2_coworkers, small_3_coworkers]
    y_labels_m_coworkers = [medium_1_coworkers, medium_2_coworkers, medium_3_coworkers]
    y_labels_l_coworkers = [large_1_coworkers, large_2_coworkers, large_3_coworkers]
    
    y_labels_s_supervisor = [small_1_supervisor, small_2_supervisor, small_3_supervisor]
    y_labels_m_supervisor  = [medium_1_supervisor, medium_2_supervisor, medium_3_supervisor]
    y_labels_l_supervisor  = [large_1_supervisor, large_2_supervisor, large_3_supervisor]
    
    
    x_length = range(len(x_labels_bar))
    width = 0.25
    
    fig1, (l, r) = plt.subplots(1,2)
    fig1.suptitle("Discussing Mental Health Related Issues in Various Sized Companies")
   
    l.set_title("Coworkers")
    l.bar(x_labels_bar, y_labels_s_coworkers, width=width, color=['powderblue'], label='Small')
    l.bar([x + width for x in x_length], y_labels_m_coworkers, width=width, color=['plum'], label='Medium')
    l.bar([x + width * 2 for x in x_length], y_labels_l_coworkers, width=width, color=['pink'], label='Large')
    
    l.set_xlabel('Types of Responses')
    l.set_ylabel('No. of Responses')
    l.set_xticks([x + width for x in x_length], x_labels_bar)
    
    r.set_title("Supervisor")
    r.bar(x_labels_bar, y_labels_s_supervisor, width=width, color=['powderblue'], label='Small')
    r.bar([x + width for x in x_length], y_labels_m_supervisor, width=width, color=['plum'], label='Medium')
    r.bar([x + width * 2 for x in x_length], y_labels_l_supervisor, width=width, color=['pink'], label='Large')
    
    r.set_xlabel('Types of Responses')
    r.set_ylabel('No. of Responses')
    r.set_xticks([x + width for x in x_length], x_labels_bar)
    plt.legend()
    
    
    
    

    plt.tight_layout()
    fig1.show()  
    
    
  
    

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
            # Your method call for the question here - hani q1
            remoteWorking()
        elif choice == 'b':
            print("--- Are employees in larger companies more likely to discuss mental health related issues with co-workers and/or supervisors? And does this have a positive/negative outcome? ---")
            # Your method call for the question here - hani q2
            DiscussionInCompanies()
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

