import pandas as pd
    
survey = pd.read_csv('survey.csv')

def replace(x):
    if x in {"Very easy", 1}:
        return "1"
    if x in {"Somewhat easy", 2}:
        return "2"
    if x in {"Somewhat difficult", 3}:
        return "3"
    if x in {"Very difficult", 4}:
        return "4"
    if x in {"Don't know", 5}:
        return "5"

survey['leave'] = survey['leave'].apply(replace)

print(survey['leave'])
survey.to_csv('survey.csv', index=False)