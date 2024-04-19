import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

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
    
    # displaying some stats
    office = office_1 + office_2 + office_3 + office_4
    remote = remote_1 + remote_2 + remote_3 + remote_4
    
    print()
    print("Number of Office Workers: ", office)
    print("Number of Remote Workers: ", remote)
    print()
    
    print()
    

   
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

# displays the graphs with questions
print()
print("--- Does remote working have a positive/negative effect on mental health (compared to working in an office)? --- ")
remoteWorking()
print()
#print("--- Are employees in larger companies more likely to discuss mental health related issues with co-workers and/or supervisors? And does this have a positive/negative outcome?---")
#DiscussionInCompanies()
#print()