import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv("survey.csv")
#2[b] Which gender is more likely to report mental health related issues?
def reports_by_gender():
# Filter data for each supervisor reports 
#'Yes' to 1, 'Some of them' to 2, 'No' to 3 
    supervisor_1 = data[data['supervisor'] == 1]
    supervisor_2 = data[data['supervisor'] == 2]
    supervisor_3 = data[data['supervisor'] == 3]

    yes_gender_counts = supervisor_1['Gender'].value_counts().sort_index()
    some_gender_counts = supervisor_2['Gender'].value_counts().sort_index()
    no_gender_counts = supervisor_3['Gender'].value_counts().sort_index()

# Create the figure and the axes
    fig, ax = plt.subplots()
# Since the genders read female, male and other the same across all three categories
    genders = no_gender_counts.index
# Generate the bars for each category
    bar1 = ax.bar([i - 0.2 for i in range(len(yes_gender_counts))], yes_gender_counts.values, width=0.2, color=['purple'],label='Yes')
    bar2 = ax.bar([i for i in range(len(some_gender_counts))], some_gender_counts.values, width=0.2, color=['teal'],label='Some of them')
    bar3 = ax.bar([i + 0.2 for i in range(len(no_gender_counts))], no_gender_counts.values, width=0.2, color=['turquoise'], label='No')
# Add values on top of the bars
    for bar in bar1 + bar2 + bar3:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
        textcoords="offset points", ha='center', va='bottom')
# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Gender', fontsize=15)
    ax.set_ylabel('Supervisor Reports Count', fontsize=15)
    ax.set_title('Supervisor Reports Count by gender', fontsize=18)
    ax.set_xticks(range(len(genders)))
    ax.set_xticklabels(genders)
    ax.legend()
# Show the plot
    plt.show()

#2[a] Which gender is more likely to get treatment for mental related issues? (working specifically in tech companies)
def treatment_by_tech_gender():
    # Filter data for tech company employees receiving treatment
    tech_treatment_data = data[(data['tech_company'] == 'Yes') & (data['treatment'] == 'Yes')]

    # Group filtered tech_treatment_data by gender and count the number of individuals
    gender_counts = tech_treatment_data['Gender'].value_counts().sort_index()
    # Custom colors for female, male, and other
    colors = ['#800080', '#4169E1', '#228B22'] 
    # Create a horizontal bar chart 
    plt.figure(figsize=(10, 6))
    plt.barh(gender_counts.index, gender_counts.values, color=colors)
    # Add values at the top of each bar
    for index, value in enumerate(gender_counts.values):
        plt.text(value, index, str(value), ha='left', va='center')

    plt.xlabel('Tech Employees Recieving Treatment', fontsize=15)
    plt.ylabel('Gender', fontsize=15, )
    plt.title('Treatment by Gender in Tech Companies', fontsize=18)
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
    plt.pie(y_labels_s_mental, labels=x_labels_pie, autopct='%1.1f%%', colors=['skyblue','steelblue','powderblue'])

    plt.subplot(1, 2, 2)
    plt.title('Physical Health Consequenses')
    plt.pie(y_labels_s_phys, labels=x_labels_pie, autopct='%1.1f%%', colors=['skyblue','steelblue','powderblue'])
    
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
    plt.pie(y_labels_l_mental, labels=x_labels_pie, autopct='%1.1f%%', colors=['hotpink','deeppink','pink'])

    plt.subplot(1, 2, 2)
    plt.title('Physical Health Consequenses')
    plt.pie(y_labels_l_phys, labels=x_labels_pie, autopct='%1.1f%%', colors=['hotpink','deeppink','pink'])
    
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

def treatment():

    countries = ['United States', 'United Kingdom']
    
    sa_y = data[(data['Country'] ==  'United States') & (data['treatment'] == 'Yes')].shape[0]
    ja_y = data[(data['Country'] == 'United Kingdom') & (data['treatment'] == 'Yes')].shape[0]

    sa_n = data[(data['Country'] ==  'United States') & (data['treatment'] == 'No')].shape[0]
    ja_n = data[(data['Country'] == 'United Kingdom') & (data['treatment'] == 'No')].shape[0] 
    
    yes_labels = [sa_y, ja_y]
    no_labels = [sa_n, ja_n]
    
    x_length = range(len(countries))
    width = 0.25

    plt.bar(countries, yes_labels, width=width, color='blue', label='seeked help')
    plt.bar([x + width for x in x_length], no_labels, width=width, color='pink', label='not seeked help')
                                                                            
                                        
    plt.title('sought treatment for mental health')
    plt.xlabel('Country')
    plt.ylabel('Number of responses')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    print(data[data["Country"] == 'United Kingdom'])
    

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
#Tsiko Mashau - Countries and Culture         
catName = ['Yes', 'No','Don\'t Know/No'] #Category names for the responses given related to whether the company provides benefits for people dealing with mental health issues
results = {
        'Switzerland': [2,1,2], #each of these values was determined by the .shape(0), code below and the results were printed onto the console, before they were added here
        'Canada': [24,19,20],
        'Netherlands': [3, 10, 6],
        'United Kingdom': [17, 67, 56],
        'France': [1,3,0],
        'Belgium': [2,1,1],
        'Sweden': [2,1,2],
        'Austria': [1,0,0],
        'Denmark': [0,2,0],
        'Australia': [4,12,4],
        'Finland': [0,2,0],
        'Norway': [0,0,0],
        'United States': [338, 98, 167],
        'Japan': [0,1,0],
        'Italy': [0,3,3],
        'Singapore': [0,1,3],
        'New Zealand': [1,6,1],
        'South Africa': [0,4,1],
        'Czech Republic': [0,1,0],
        'Portugal': [0,1,0],
        'Hungary': [0,1,0],
        'Poland': [0,5,2],
        'Slovakia': [0,0,0],
        'Slovenia': [0,0,1],
        'Croatia': [1,1,0],
        'Bulgaria': [0,2,1],
        'Bosnia and Herzegovina': [0,0,1],
        'Moldova': [0,1,0],
        'Georgia': [0,1,0],
        'Russia': [0,2,0],
        'India': [0,2,3],
        'Thailand': [0,1,0],
        'Philippines': [0,0,1],
        'China': [0,1,0],
        'Germany': [3,17,13],
        'Mexico': [0,2,1],
        }



def country_mental_Benefits(): #Tsiko, question 1b
    

    BenefitsSwi1 = data[(data['Country'] == 'Switzerland') & (data['benefits'] == 1)].shape[0] #Yes 2
    BenefitsSwi2 = data[(data['Country'] == 'Switzerland') & (data['benefits'] == 2)].shape[0] #No 1
    BenefitsSwi3 = data[(data['Country'] == 'Switzerland') & (data['benefits'] == 3)].shape[0] #Dont know/Not sure 2
    
    BenefitsCan1 = data[(data['Country']=='Canada') & (data['benefits'] == 1)].shape[0] #Yes 24
    BenefitsCan2 = data[(data['Country']=='Canada') & (data['benefits'] == 2)].shape[0] #No 19
    BenefitsCan3 = data[(data['Country']=='Canada') & (data['benefits'] == 3)].shape[0]#Dont know/Not sure 20
    
    BenefitsNet1 = data[(data['Country']=='Netherlands') & (data['benefits'] == 1)].shape[0]#Yes 3
    BenefitsNet2 = data[(data['Country']=='Netherlands') & (data['benefits'] == 2)].shape[0] #No 10
    BenefitsNet3 = data[(data['Country']=='Netherlands') & (data['benefits'] == 3)].shape[0]#Dont know/Not sure 6

    BenefitsUK1 = data[(data['Country']=='United Kingdom') & (data['benefits'] == 1)].shape[0]#Yes 17
    BenefitsUK2 = data[(data['Country']=='United Kingdom') & (data['benefits'] == 2)].shape[0]#No 67
    BenefitsUK3 = data[(data['Country']=='United Kingdom') & (data['benefits'] == 3)].shape[0]#Dont know/Not sure 56

    BenefitsFra1 = data[(data['Country']=='France') & (data['benefits'] == 1)].shape[0]
    BenefitsFra2 = data[(data['Country']=='France') & (data['benefits'] == 2)].shape[0]
    BenefitsFra3= data[(data['Country']=='France') & (data['benefits'] == 3)].shape[0]

    BenefitsBel1 = data[(data['Country']=='Belgium') & (data['benefits'] == 1)].shape[0]
    BenefitsBel2 = data[(data['Country']=='Belgium') & (data['benefits'] == 2)].shape[0]
    BenefitsBel3 = data[(data['Country']=='Belgium') & (data['benefits'] == 3)].shape[0]

    BenefitsSwe1 = data[(data['Country']=='Sweden') & (data['benefits'] == 1)].shape[0]
    BenefitsSwe2 = data[(data['Country']=='Sweden') & (data['benefits'] == 2)].shape[0]
    BenefitsSwe3 = data[(data['Country']=='Sweden') & (data['benefits'] == 3)].shape[0]

    BenefitsAustria1 = data[(data['Country']=='Austria') & (data['benefits'] == 1)].shape[0]
    BenefitsAustria2 = data[(data['Country']=='Austria') & (data['benefits'] == 2)].shape[0]
    BenefitsAustria3 = data[(data['Country']=='Austria') & (data['benefits'] == 3)].shape[0]

    BenefitsDen1 = data[(data['Country']=='Denmark') & (data['benefits'] == 1)].shape[0]
    BenefitsDen2 = data[(data['Country']=='Denmark') & (data['benefits'] == 2)].shape[0]
    BenefitsDen3 = data[(data['Country']=='Denmark') & (data['benefits'] == 3)].shape[0]

    BenefitsAus1 = data[(data['Country']=='Australia') & (data['benefits'] == 1)].shape[0]
    BenefitsAus2 = data[(data['Country']=='Australia') & (data['benefits'] == 2)].shape[0]
    BenefitsAus3 = data[(data['Country']=='Australia') & (data['benefits'] == 3)].shape[0]

    BenefitsFin1 = data[(data['Country']=='Finland') & (data['benefits'] == 1)].shape[0]
    BenefitsFin2 = data[(data['Country']=='Finland') & (data['benefits'] == 2)].shape[0]
    BenefitsFin3 = data[(data['Country']=='Finland') & (data['benefits'] == 3)].shape[0]

    BenefitsNor1 = data[(data['Country']=='Norway') & (data['benefits'] == 1)].shape[0]
    BenefitsNor2 = data[(data['Country']=='Norway') & (data['benefits'] == 2)].shape[0]
    BenefitsNor3 = data[(data['Country']=='Norway') & (data['benefits'] == 3)].shape[0]

    BenefitsUS1 = data[(data['Country']=='United States') & (data['benefits'] == 1)].shape[0]
    BenefitsUS2 = data[(data['Country']=='United States') & (data['benefits'] == 2)].shape[0]
    BenefitsUS3 = data[(data['Country']=='United States') & (data['benefits'] == 3)].shape[0]

    BenefitsJap1 = data[(data['Country']=='Japan') & (data['benefits'] == 1)].shape[0]
    BenefitsJap2 = data[(data['Country']=='Japan') & (data['benefits'] == 2)].shape[0]
    BenefitsJap3 = data[(data['Country']=='Japan') & (data['benefits'] == 3)].shape[0]

    BenefitsIta1 = data[(data['Country']=='Italy') & (data['benefits'] == 1)].shape[0]
    BenefitsIta2 = data[(data['Country']=='Italy') & (data['benefits'] == 2)].shape[0]
    BenefitsIta3 = data[(data['Country']=='Italy') & (data['benefits'] == 3)].shape[0]

    BenefitsSin1 = data[(data['Country']=='Singapore') & (data['benefits'] == 1)].shape[0]
    BenefitsSin2 = data[(data['Country']=='Singapore') & (data['benefits'] == 2)].shape[0]
    BenefitsSin3 = data[(data['Country']=='Singapore') & (data['benefits'] == 3)].shape[0]

    BenefitsNZ1 = data[(data['Country']=='New Zealand') & (data['benefits'] == 1)].shape[0]
    BenefitsNZ2 = data[(data['Country']=='New Zealand') & (data['benefits'] == 2)].shape[0]
    BenefitsNZ3 = data[(data['Country']=='New Zealand') & (data['benefits'] == 3)].shape[0]

    BenefitsSA1 = data[(data['Country']=='South Africa') & (data['benefits'] == 1)].shape[0]
    BenefitsSA2 = data[(data['Country']=='South Africa') & (data['benefits'] == 2)].shape[0]
    BenefitsSA3 = data[(data['Country']=='South Africa') & (data['benefits'] == 3)].shape[0]

    BenefitsCR1 = data[(data['Country']=='Czech Republic') & (data['benefits'] == 1)].shape[0]
    BenefitsCR2 = data[(data['Country']=='Czech Republic') & (data['benefits'] == 2)].shape[0]
    BenefitsCR3 = data[(data['Country']=='Czech Republic') & (data['benefits'] == 3)].shape[0]

    BenefitsPor1 = data[(data['Country']=='Portugal') & (data['benefits'] == 1)].shape[0]
    BenefitsPor2 = data[(data['Country']=='Portugal') & (data['benefits'] == 2)].shape[0]
    BenefitsPor3 = data[(data['Country']=='Portugal') & (data['benefits'] == 3)].shape[0]

    BenefitsHun1 = data[(data['Country']=='Hungary') & (data['benefits'] == 1)].shape[0]
    BenefitsHun2 = data[(data['Country']=='Hungary') & (data['benefits'] == 2)].shape[0]
    BenefitsHun3 = data[(data['Country']=='Hungary') & (data['benefits'] == 3)].shape[0]

    BenefitsPol1 = data[(data['Country']=='Poland') & (data['benefits'] == 1)].shape[0]
    BenefitsPol2 = data[(data['Country']=='Poland') & (data['benefits'] == 2)].shape[0]
    BenefitsPol3 = data[(data['Country']=='Poland') & (data['benefits'] == 3)].shape[0]

    BenefitsSlok1 = data[(data['Country']=='Slovakia') & (data['benefits'] == 1)].shape[0]
    BenefitsSlok2 = data[(data['Country']=='Slovakia') & (data['benefits'] == 2)].shape[0]
    BenefitsSlok3= data[(data['Country']=='Slovakia') & (data['benefits'] == 3)].shape[0]

    BenefitsSlo1 = data[(data['Country']=='Slovenia') & (data['benefits'] == 1)].shape[0]
    BenefitsSlo2 = data[(data['Country']=='Slovenia') & (data['benefits'] == 2)].shape[0]
    BenefitsSlo3 = data[(data['Country']=='Slovenia') & (data['benefits'] == 3)].shape[0]

    BenefitsBnH1 = data[(data['Country']=='Bosnia and Herzegovina') & (data['benefits'] == 1)].shape[0]
    BenefitsBnH2 = data[(data['Country']=='Bosnia and Herzegovina') & (data['benefits'] == 2)].shape[0]
    BenefitsBnH3 = data[(data['Country']=='Bosnia and Herzegovina') & (data['benefits'] == 3)].shape[0]

    BenefitsMol1 = data[(data['Country']=='Moldova') & (data['benefits'] == 1)].shape[0]
    BenefitsMol2 = data[(data['Country']=='Moldova') & (data['benefits'] == 2)].shape[0]
    BenefitsMol3 = data[(data['Country']=='Moldova') & (data['benefits'] == 3)].shape[0]

    BenefitsGeo1 = data[(data['Country']=='Georgia') & (data['benefits'] == 1)].shape[0]
    BenefitsGeo2 = data[(data['Country']=='Georgia') & (data['benefits'] == 2)].shape[0]
    BenefitsGeo3 = data[(data['Country']=='Georgia') & (data['benefits'] == 3)].shape[0]
    
    BenefitsRus1 = data[(data['Country']=='Russia') & (data['benefits'] == 1)].shape[0]
    BenefitsRus2 = data[(data['Country']=='Russia') & (data['benefits'] == 2)].shape[0]
    BenefitsRus3 = data[(data['Country']=='Russia') & (data['benefits'] == 3)].shape[0]

    BenefitsInd1 = data[(data['Country']=='India') & (data['benefits'] == 1)].shape[0]
    BenefitsInd2 = data[(data['Country']=='India') & (data['benefits'] == 2)].shape[0]
    BenefitsInd3 = data[(data['Country']=='India') & (data['benefits'] == 3)].shape[0]

    BenefitsThai1 = data[(data['Country']=='Thailand') & (data['benefits'] == 1)].shape[0]
    BenefitsThai2 = data[(data['Country']=='Thailand') & (data['benefits'] == 2)].shape[0]
    BenefitsThai3 = data[(data['Country']=='Thailand') & (data['benefits'] == 3)].shape[0]

    BenefitsPhil1 = data[(data['Country']=='Philippines') & (data['benefits'] == 1)].shape[0]
    BenefitsPhil2 = data[(data['Country']=='Philippines') & (data['benefits'] == 2)].shape[0]
    BenefitsPhil3 = data[(data['Country']=='Philippines') & (data['benefits'] == 3)].shape[0]

    BenefitsChi1 = data[(data['Country']=='China') & (data['benefits'] == 1)].shape[0]
    BenefitsChi2 = data[(data['Country']=='China') & (data['benefits'] == 2)].shape[0]
    BenefitsChi3 = data[(data['Country']=='China') & (data['benefits'] == 3)].shape[0]

    BenefitsMex1 = data[(data['Country']=='Mexico') & (data['benefits'] == 1)].shape[0]
    BenefitsMex2 = data[(data['Country']=='Mexico') & (data['benefits'] == 2)].shape[0]
    BenefitsMex3 = data[(data['Country']=='Mexico') & (data['benefits'] == 3)].shape[0]

    BenefitsGer1 = data[(data['Country']=='Germany') & (data['benefits'] == 1)].shape[0]
    BenefitsGer2 = data[(data['Country']=='Germany') & (data['benefits'] == 2)].shape[0]
    BenefitsGer3 = data[(data['Country']=='Germany') & (data['benefits'] == 3)].shape[0]

    BenefitsCro1 = data[(data['Country']=='Croatia') & (data['benefits'] == 1)].shape[0]
    BenefitsCro2 = data[(data['Country']=='Croatia') & (data['benefits'] == 2)].shape[0]
    BenefitsCro3 = data[(data['Country']=='Croatia') & (data['benefits'] == 3)].shape[0]

    BenefitsBul1 = data[(data['Country']=='Bulgaria') & (data['benefits'] == 1)].shape[0]
    BenefitsBul2 = data[(data['Country']=='Bulgaria') & (data['benefits'] == 2)].shape[0]
    BenefitsBul3 = data[(data['Country']=='Bulgaria') & (data['benefits'] == 3)].shape[0]



# Extracting data for each category
yes = [results[country][0] for country in results]
no = [results[country][1] for country in results]
dontKnow = [results[country][2] for country in results]

# Creating scatter plots
plt.scatter(list(results.keys()), yes, color='red', label='Yes')
plt.scatter(list(results.keys()), no, color='green', label='No')
plt.scatter(list(results.keys()), dontKnow, color='lightblue', label='Don\'t Know/No')

# Adding labels and title
plt.title('Countries with companies providing Benefits for Mental Health')
plt.xlabel('Countries')
plt.ylabel('Companies')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()

def culture_and_countries(): #Tsiko, Khushi
    while True:
        print()
        print("=== Culture & Countries ===")
        print("Questions:")
        print("[a] Which country has the highest mental health issues?")
        print("[b] Which country has the most companies that provide benefits to workers with mental health issues?")
        print("[c] Whether or not people from United States and United Kingdom seek treatment for mental health issues?")
        print("[0] Back to main menu")

        choice = input("Enter your option: ").strip().lower()
        if choice == 'a':
            print("--- Which continent has the highest mental health issues? ---")
            # Your method call for the question here
            print("--- Which continent has the highest mental health issues? ---")
            seekYes = data[(data['seek_help'] == 1)]
            seekNo = data[(data['seek_help'] == 2)] 
            seekUnsure = data[(data['seek_help'] == 3)]
            
        
            northAmerica = (data['Country'] == 'United States') | (data['Country'] == 'Canada') | (data['Country'] == 'Mexico')
            southAmerica = (data['Country'] == 'Brazil') | (data['Country'] == 'Colombia')
            oceania = (data['Country'] == 'Australia') | (data['Country'] == 'New Zealand')
            africa = (data['Country'] == 'South Africa')
            asia= (data['Country'] == 'India') | (data['Country'] == 'Thailand') | (data['Country'] == 'Japan')| (data['Country'] == 'Philippines')| (data['Country'] == 'China')| (data['Country'] == 'Singapore')
            europe = (data['Country'] == 'United Kingdom') | (data['Country'] == 'Bulgaria') | (data['Country'] == 'Netherland')| (data['Country'] == 'Poland')| (data['Country'] == 'France')| (data['Country'] == 'Germany')| (data['Country'] == 'Slovenia')| (data['Country'] == 'Ireland')| (data['Country'] == 'Russia')| (data['Country'] == 'Italy')| (data['Country'] == 'Portugal')| (data['Country'] == 'Switzerland')| (data['Country'] == 'Belgium')| (data['Country'] == 'Sweden')| (data['Country'] == 'Finland')| (data['Country'] == 'Bosnia and Herzegovina')| (data['Country'] == 'Austria')| (data['Country'] == 'Hungary')| (data['Country'] == 'Crotia')| (data['Country'] == 'Denmark')| (data['Country'] == 'Moldova')| (data['Country'] == 'Georgia')| (data['Country'] == 'Czech Republic')                               
            x_labels=['North America', 'South America', 'Oceania', 'Africa', 'Asia', 'europe']
           
            na_y = data[(northAmerica) & (data['seek_help'] == 1)].shape[0]
            sa_y = data[(southAmerica) & (data['seek_help'] == 1)].shape[0]
            oc_y = data[(oceania) & (data['seek_help'] == 1)].shape[0] # 10
            af_y = data[(africa) & (data['seek_help'] == 1)].shape[0] # 0
            as_y = data[(asia) & (data['seek_help'] == 1)].shape[0]
            eu_y = data[(europe) & (data['seek_help'] == 1)].shape[0]
            
            na_n = data[(northAmerica) & (data['seek_help'] == 2)].shape[0]
            sa_n = data[(southAmerica) & (data['seek_help'] == 2)].shape[0]
            oc_n = data[(oceania) & (data['seek_help'] == 2)].shape[0] # 10
            af_n = data[(africa) & (data['seek_help'] == 2)].shape[0] # 0
            as_n = data[(asia) & (data['seek_help'] == 2)].shape[0]
            eu_n = data[(europe) & (data['seek_help'] == 2)].shape[0]

            na_us = data[(northAmerica) & (data['seek_help'] == 3)].shape[0]
            sa_us = data[(southAmerica) & (data['seek_help'] == 3)].shape[0]
            oc_us = data[(oceania) & (data['seek_help'] == 3)].shape[0] # 10
            af_us = data[(africa) & (data['seek_help'] == 3)].shape[0] # 0
            as_us = data[(asia) & (data['seek_help'] == 3)].shape[0]
            eu_us = data[(europe) & (data['seek_help'] == 3)].shape[0]
            
            yes_labels=[na_y, sa_y, oc_y, af_y, as_y, eu_y]
            no_labels=[na_n, sa_n, oc_n, af_n, as_n, eu_n]
            unsure_labels=[na_us, sa_us, oc_us, af_us, as_us, eu_us]
    
            plt.plot(x_labels, yes_labels, color='red', label='Experienced mental health')
            plt.plot(x_labels, no_labels, color='green', label='Not experienced mental health')
            plt.plot(x_labels, unsure_labels, color='purple', label='Unsure ')
        
            #plt.plot(country_ref3, color='green', label='Unsure')

            plt.title('Most common country for experiencing mental health')
            plt.xlabel('Country')
            plt.ylabel('Number of employees')
            plt.grid(True)
            plt.legend()
            plt.show()
        elif choice == 'b':
            print("--- Is there an increase in mental health awareness in higher income countries than lower income countries? ---")
            # Your method call for the question here
            country_mental_Benefits()
            # shows the graph
            plt.show()
        elif choice == 'c':
            print("--- Whether or not people from United States and United Kingdom seek treatment for mental health issues?​ ---")
            # Your method call for the question here
            treatment()
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
            reports_by_gender()
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
            staffAttitude()
            

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
            selfEmployment()
            
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

