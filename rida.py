import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv") # THIS IS THE SURVEY!! CALL 'DATA" TO ACCESS THE DATASET

# def image(): # rida q1
# Does the staff in the company have a good or bad image on mental health?





def selfEmployment(): # rida q2
# Does being self-employed increase the chances of mental health issues?
# answer columns: self_employed, work_interference

    self_employed_1 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 1)].shape[0] # often
    self_employed_2 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 2)].shape[0] # sometimes
    self_employed_3 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 3)].shape[0] # rarely
    self_employed_4 = data[(data['self_employed'] == 'Yes') & (data['work_interfere'] == 4)].shape[0] # never
    
    x = ['Often', 'Sometimes', 'Rarely', 'Never']
    y = [self_employed_1, self_employed_2, self_employed_3, self_employed_4]
    

    plt.title('How self - employment effects mental health')
    plt.plot(x, y, color='pink')
    
    
    plt.xlabel('Frequency of Work Interference')
    plt.ylabel('Responses')
    
    plt.ylim(bottom = 0)
    
    plt.legend()
    plt.show()
    
xy = selfEmployment()
print (xy)