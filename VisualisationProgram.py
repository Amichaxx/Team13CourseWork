import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

def mental_health_by_gender():
# Filter data for each gender
    female_data = data[data['Gender'] == 'female']
    male_data = data[data['Gender'] == 'male']
    other_data = data[data['Gender'] == 'other']

    # Count responses for each supervisor report
    female_supervisor_counts = female_data['supervisor'].value_counts().sort_index()
    male_supervisor_counts = male_data['supervisor'].value_counts().sort_index()
    other_supervisor_counts = other_data['supervisor'].value_counts().sort_index()

    # Plot the results
    x_labels = ['Yes', 'Some of them', 'No']
    plt.figure(figsize=(8, 6))
    plt.bar(x_labels, female_supervisor_counts, color='purple', label='Female')
    plt.bar(x_labels, male_supervisor_counts, color='teal', label='Male', bottom=female_supervisor_counts)
    plt.bar(x_labels, other_supervisor_counts, color='turquoise', label='Other', bottom=male_supervisor_counts + female_supervisor_counts)
    

    plt.title('Supervisor Reports by Gender', fontname="Times New Roman", fontsize=18)
    plt.xlabel("Supervisor Reports", fontname="Times New Roman", fontsize=12) 
    plt.ylabel("Number of Responses", fontname="Times New Roman", fontsize=12) 
    plt.legend()
    plt.show()


def treatment_by_tech_gender():
    # Filter data for tech company employees receiving treatment
    tech_treatment_data = data[(data['tech_company'] == 'Yes') & (data['treatment'] == 'Yes')]

    # Group filtered tech_treatment_data by gender and count the number of individuals
    gender_counts = tech_treatment_data['Gender'].value_counts().sort_index()

    # Create a horizontal bar chart 
    # Custom colors for female, male, and other
    colors = ['#800080', '#4169E1', '#228B22'] 

    plt.figure(figsize=(10, 6))
    plt.barh(gender_counts.index, gender_counts.values, color=colors)
    plt.xlabel('Tech Employees Recieving Treatment', fontname="Times New Roman", fontsize=15)
    plt.ylabel('Gender', fontname="Times New Roman", fontsize=15, )
    plt.title('Treatment by Gender in Tech Companies', fontname="Times New Roman", fontsize=18)
    plt.tight_layout()

    # Show the plot
    plt.show()


def remoteWorking(): #hani q1
    # --- Does remote working have a positive/negative effect on mental health (compared to working in an office)? ---
    # answer columns: work_interfere

    remote_1 = data[(data['remote_work'] == 'Yes') & (data['work_interfere'] == 1)].shape[0]
    remote_2 = data[(data['remote_work'] == 'Yes') & (data['work_interfere'] == 2)].shape[0]
    remote_3 = data[(data['remote_work'] == 'Yes') & (data['work_interfere'] == 3)].shape[0]
    remote_4 = data[(data['remote_work'] == 'Yes') & (data['work_interfere'] == 4)].shape[0]
    
    office_1 = data[(data['remote_work'] == 'No') & (data['work_interfere'] == 1)].shape[0]
    office_2 = data[(data['remote_work'] == 'No') & (data['work_interfere'] == 2)].shape[0]
    office_3 = data[(data['remote_work'] == 'No') & (data['work_interfere'] == 3)].shape[0]
    office_4 = data[(data['remote_work'] == 'No') & (data['work_interfere'] == 4)].shape[0]

    x_labels = ['Often', 'Sometimes', 'Rarely', 'Never']
    y_labels = [remote_1, remote_2, remote_3,remote_4]
    y_labels_o = [office_1, office_2, office_3,office_4]

    plt.title('The Effects of Remote Working on Mental Health')
    plt.plot(x_labels, y_labels, color='green', label = 'Remote')
    plt.plot(x_labels, y_labels_o, color='mediumaquamarine', label = 'Office')
    
    plt.xlabel('Frequency of Work Interference')
    plt.ylabel('No. of Responses')
    
    plt.ylim(bottom = 0)
    
    plt.legend()
    plt.show()

   
def DiscussionInCompanies(): #hani q2
    # --- Are employees in larger companies more likely to discuss mental health related issues with co-workers and/or supervisors? ---
    # answer columns: coworkers, supervisor
    
    # Part 1: BAR CHARTS
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
    
    x_labels_bar = ['Yes', 'Some', 'No']
    
    y_labels_s_coworkers = [small_1_coworkers, small_2_coworkers, small_3_coworkers]
    y_labels_m_coworkers = [medium_1_coworkers, medium_2_coworkers, medium_3_coworkers]
    y_labels_l_coworkers = [large_1_coworkers, large_2_coworkers, large_3_coworkers]
    
    y_labels_s_supervisor = [small_1_supervisor, small_2_supervisor, small_3_supervisor]
    y_labels_m_supervisor  = [medium_1_supervisor, medium_2_supervisor, medium_3_supervisor]
    y_labels_l_supervisor  = [large_1_supervisor, large_2_supervisor, large_3_supervisor]
    
    x_length = range(len(x_labels_bar))
    width = 0.25
    
    fig, (l, r) = plt.subplots(1,2)
    fig.suptitle("Discussing Mental Health Related Issues in Various Sized Companies")
   
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
    
    plt.figure(1)
    plt.legend(title='Company Size')
    plt.tight_layout()
    plt.show()  
    
    # --- And does this have a positive/negative outcome? ---
    # answer columns: mental_health_consequence, phys_health_consequence
    
    # Part 2: PIE CHARTS
    small_1_mental = data[(data['no_employees']=='Small') & (data['mental_health_consequence']==1)].shape[0] # yes - 139 responses
    small_2_mental = data[(data['no_employees']=='Small') & (data['mental_health_consequence']==2)].shape[0] # no - 234 responses
    small_3_mental = data[(data['no_employees']=='Small') & (data['mental_health_consequence']==3)].shape[0] # maybe - 211 responses
    
    small_1_phys = data[(data['no_employees']=='Small') & (data['phys_health_consequence']==1)].shape[0] # yes
    small_2_phys = data[(data['no_employees']=='Small') & (data['phys_health_consequence']==2)].shape[0] # no
    small_3_phys = data[(data['no_employees']=='Small') & (data['phys_health_consequence']==3)].shape[0] # maybe
    
    medium_1_mental = data[(data['no_employees']=='Medium') & (data['mental_health_consequence']==1)].shape[0] # yes
    medium_2_mental = data[(data['no_employees']=='Medium') & (data['mental_health_consequence']==2)].shape[0] # no
    medium_3_mental = data[(data['no_employees']=='Medium') & (data['mental_health_consequence']==3)].shape[0] # maybe 
    
    medium_1_phys = data[(data['no_employees']=='Medium') & (data['phys_health_consequence']==1)].shape[0] # yes
    medium_2_phys = data[(data['no_employees']=='Medium') & (data['phys_health_consequence']==2)].shape[0] # no
    medium_3_phys = data[(data['no_employees']=='Medium') & (data['phys_health_consequence']==3)].shape[0] # maybe
    
    large_1_mental = data[(data['no_employees']=='Large') & (data['mental_health_consequence']==1)].shape[0] # yes
    large_2_mental = data[(data['no_employees']=='Large') & (data['mental_health_consequence']==2)].shape[0] # no
    large_3_mental = data[(data['no_employees']=='Large') & (data['mental_health_consequence']==3)].shape[0] # maybe 
    
    large_1_phys = data[(data['no_employees']=='Large') & (data['phys_health_consequence']==1)].shape[0] # yes
    large_2_phys = data[(data['no_employees']=='Large') & (data['phys_health_consequence']==2)].shape[0] # no
    large_3_phys = data[(data['no_employees']=='Large') & (data['phys_health_consequence']==3)].shape[0] # maybe
    
    x_labels_pie = ['Yes', 'No', 'Maybe']
    
    y_labels_s_mental = [small_1_mental, small_2_mental, small_3_mental]
    y_labels_s_phys = [small_1_phys, small_2_phys, small_3_phys]
    
    y_labels_m_mental = [medium_1_mental, medium_2_mental, medium_3_mental]
    y_labels_m_phys = [medium_1_phys, medium_2_phys, medium_3_phys]
    
    y_labels_l_mental = [large_1_mental, large_2_mental, large_3_mental]
    y_labels_l_phys = [large_1_phys, large_2_phys, large_3_phys]
    
    # figure 2: small
    plt.figure(2)
    plt.suptitle("Consquences of Discussing Mental Health Related Issues in a Small Sized Company")
            
    plt.subplot(1, 2, 1)
    plt.title('Mental Health Consequences')
    plt.pie(y_labels_s_mental, labels=x_labels_pie, autopct='%1.1f%%', colors=['powderblue','lightblue','skyblue'])

    plt.subplot(1, 2, 2)
    plt.title('Physical Health Consequenses')
    plt.pie(y_labels_s_phys, labels=x_labels_pie, autopct='%1.1f%%', colors=['powderblue','lightblue','skyblue'])
    
    plt.tight_layout()
    plt.show()
    
    # figure 3: medium
    plt.figure(3)
    plt.suptitle("Consquences of Discussing Mental Health Related Issues in a Medium Sized Company")
    
    plt.subplot(1, 2, 1)
    plt.title('Mental Health Consequences')
    plt.pie(y_labels_m_mental, labels=x_labels_pie, autopct='%1.1f%%', colors=['mediumpurple','purple','plum'])

    plt.subplot(1, 2, 2)
    plt.title('Physical Health Consequenses')
    plt.pie(y_labels_m_phys, labels=x_labels_pie, autopct='%1.1f%%', colors=['mediumpurple','purple','plum'])
    
    plt.tight_layout()
    plt.show()
    
    # figure 4: large
    plt.figure(4)
    plt.suptitle("Consquences of Discussing Mental Health Related Issues in a Large Sized Company")
    
    plt.subplot(1, 2, 1)
    plt.title('Mental Health Consequences')
    plt.pie(y_labels_l_mental, labels=x_labels_pie, autopct='%1.1f%%', colors=['pink','lightpink','hotpink'])

    plt.subplot(1, 2, 2)
    plt.title('Physical Health Consequenses')
    plt.pie(y_labels_l_phys, labels=x_labels_pie, autopct='%1.1f%%', colors=['pink','lightpink','hotpink'])
    
    plt.tight_layout()
    plt.show()

# def image(): # rida q1
def staffAttitude():
# Do the staff in tech companies have a good attitude towards mental health?
# Columns used: coworkers, supervisors, seek_help
    coworker_1 = data[(data['coworkers'] == 1) & (data['seek_help'] == 1)].shape[0] #yes
    coworker_2 = data[(data['coworkers'] == 1) & (data['seek_help'] == 2)].shape[0] #no
    coworker_3 = data[(data['coworkers'] == 1) & (data['seek_help'] == 3)].shape[0] #don't know

    supervisor_1 = data[(data['supervisor'] == 1) & (data['seek_help'] == 1)].shape[0] #yes
    supervisor_2 = data[(data['supervisor'] == 1) & (data['seek_help'] == 2)].shape[0] #no
    supervisor_3 = data[(data['supervisor'] == 1) & (data['seek_help'] == 3)].shape[0] #don't know

    x = ['Yes', 'No', 'Dont know']
    y = [coworker_1, coworker_2, coworker_3]
    z = [supervisor_1, supervisor_2, supervisor_3]

    fig, (coworkers, supervisor) = plt.subplots(1, 2, sharey=True, figsize=(8,8))
    coworkers.set_title("Staff seeking help from coworkers")
    supervisor.set_title("Staff seeking help from supervisors")


    coworkers.bar(x, y, color=['plum','pink','paleturquoise'])
    supervisor.bar(x, z, color=['lightsalmon', 'bisque', 'palegreen'])

    coworkers.set_xlabel('Frequency of coworkers')
    coworkers.set_ylabel('Responses')
    supervisor.set_xlabel('Frequency of supervisors')
    supervisor.set_ylabel('Responses')

    plt.ylim(bottom = 0)

    plt.legend()
    plt.show()
    

def selfEmployment(): # rida q2
# Does being self-employed increase the chances of mental health issues?
# Columns used: self_employed, work_interference

    self_employed_1 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 1)].shape[0] # often
    self_employed_2 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 2)].shape[0] # sometimes
    self_employed_3 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 3)].shape[0] # rarely
    self_employed_4 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 4)].shape[0] # never
    
    x = ['Often', 'Sometimes', 'Rarely', 'Never']
    y = [self_employed_1, self_employed_2, self_employed_3, self_employed_4]
    
    plt.title('How self - employment effects mental health')
    plt.bar(x, y, color= ['firebrick', 'darkorange', 'dimgray', 'midnightblue'])
    
    plt.xlabel('Frequency of Work Interference')
    plt.ylabel('Responses')
    
    plt.ylim(bottom = 0)
    
    plt.legend()
    plt.show()
    

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
        print("[c] Does the country provide any kind of support or resources for people dealing with mental health?")
        print("[d] In what ways do cultural distinctions affect how tech workers in Japan and the US see and handle mental health concerns?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Which country has the highest mental health issues? ---")
            # Your method call for the question here
        elif choice == 'b':
            print("--- Is there an increase in mental health awareness in higher income countries than lower income countries? ---")
            # Your method call for the question here
        elif choice == 'c':
            print("--- Does the country provide any kind of support or resources for people dealing with mental health? ---")
            # Your method call for the question here
        elif choice == 'd':
            print("--- In what ways do cultural distinctions affect how tech workers in Japan and the US see and handle mental health concerns? ---")
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
            treatment_by_tech_gender()
        elif choice == 'b':
            print("--- Which gender is more likely to report mental health related issues? ---")
            # Your method call for the question here
            mental_health_by_gender()
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
            seekYes = data[(data['seek_help'] == 1)]
            seekNo = data[(data['seek_help'] == 2)]
            seekUnsure = data[(data['seek_help'] == 3)]

            mao = seekYes['Age'].value_counts().sort_index()
            chikka = seekNo['Age'].value_counts().sort_index()
            maowow = seekUnsure['Age'].value_counts().sort_index()

            plt.plot(mao, color='pink', label='Experienced mental health')
            plt.plot(chikka, color='green', label='Not experienced mental health')
            plt.plot(maowow, color='blue', label='Unsure')

            plt.title('Most common age for experiencing mental health')
            plt.xlabel('Age')
            plt.ylabel('Number of employees')
            plt.grid(True)
            plt.legend()
            plt.show()
            plt.show()

        elif choice == 'b':
            print("--- Are younger employees more likely to seek help for mental health issues? ---")
            soughtTreatment = data[(data['treatment'] == 'Yes')]
            notSoughtTreatment = data[(data['treatment'] == 'No')]

            boo = soughtTreatment['Age'].value_counts().sort_index()
            bow = notSoughtTreatment['Age'].value_counts().sort_index()

            plt.plot(boo, color='pink', label='Sought treatment')
            plt.plot(bow, color='green', label='Not sought treatment')

            plt.title('Most common age for seeking treatment')
            plt.xlabel('Age')
            plt.ylabel('Number of employees')
            plt.grid(True)
            plt.legend()
            plt.show()

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
        print("[b] Do the staff in tech companies have a good attitude towards mental health?")
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
            print("--- Do the staff in tech companies have a good attitude towards mental health? ---")
            # Your method call for the question here - rida q1
            xy = staffAttitude()
            print(xy)

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
            # Your method call for the question here - rida q2
            staff = selfEmployment()
            print(staff)

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

