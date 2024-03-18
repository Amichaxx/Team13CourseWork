import pandas as pd
    
survey = pd.read_csv('survey.csv')

def replace(x):
    if x in {"Very easy"}:
        return "1"
    if x in {"Somewhat easy"}:
        return "2"
    if x in {"Somewhat difficult"}:
        return "3"
    if x in {"Very difficult"}:
        return "4"
    if x in {"Don't know"}:
        return "5"

survey['leave'] = survey['leave'].apply(replace)

print(survey['leave'])
survey.to_csv('survey.csv', index=False)