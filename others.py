import pandas as pd
    
survey = pd.read_csv('survey.csv')

def replace(x):
    if x in {"Yes", 1}:
        return "1"
    if x in {"No", 2}:
        return "2"
    if x in {"Don't know", "Not sure", 3}:
        return "3"

survey['benefits'] = survey['benefits'].apply(replace)
survey['wellness_program'] = survey['wellness_program'].apply(replace)
survey['seek_help'] = survey['seek_help'].apply(replace)
survey['anonymity'] = survey['anonymity'].apply(replace)
survey['care_options'] = survey['care_options'].apply(replace)

print(survey['benefits'])
print(survey['wellness_program'])
print(survey['seek_help'])
print(survey['anonymity'])
print(survey['care_options'])

# commiting the changes to the file
survey.to_csv('survey.csv', index=False)