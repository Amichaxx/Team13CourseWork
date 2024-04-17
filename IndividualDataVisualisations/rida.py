import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv") # THIS IS THE SURVEY!! CALL 'DATA" TO ACCESS THE DATASET

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
    
staff = staffAttitude()
print (staff)



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
    
xy = selfEmployment()
print (xy)
