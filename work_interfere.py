import pandas as pd
    
survey = pd.read_csv('survey.csv')

# removes empty rows
survey.dropna(subset=['work_interfere'], inplace=True)

def replace(x):
    if x in {"Often", 1}:
        return "1"
    if x in {"Sometimes", 2}:
        return "2"
    if x in {"Rarely", 3}:
        return "3"
    if x in {"Never", 4}:
        return "4"

survey['work_interfere'] = survey['work_interfere'].apply(replace)

print(survey['work_interfere'])
survey.to_csv('survey.csv', index=False)








