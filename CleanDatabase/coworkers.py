import pandas as pd
    
survey = pd.read_csv('survey.csv')

def replace(x):
    if x in {"Yes"}:
        return "1"
    if x in {"Some of them"}:
        return "2"
    if x in {"No"}:
        return "3"

survey['coworkers'] = survey['coworkers'].apply(replace)
survey['supervisor'] = survey['supervisor'].apply(replace)


print(survey['coworkers'])
print(survey['supervisor'])

# commiting the changes to the file
survey.to_csv('survey.csv', index=False)