import pandas as pd
    
survey = pd.read_csv('survey.csv')

# hani: cleaned benefits, wellness_program, seek_help, anonymity, care_options columns
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

# hani: cleaned coworkers and supervisor columns
def change(x):
    if x in {"Yes", 1}:
        return "1"
    if x in {"Some of them", 2}:
        return "2"
    if x in {"No", 3}:
        return "3"

survey['coworkers'] = survey['coworkers'].apply(change)
survey['supervisor'] = survey['supervisor'].apply(change)

# hani: cleaned leave column
def leave(x):
    if x in {"Very easy", 1}:
        return "1"
    if x in {"Somewhat easy", 2}:
        return "2"
    if x in {"Somewhat difficult", 3}:
        return "3"
    if x in {"Very difficult", 4}:
        return "4"
    if x in {"Don't know",5}:
        return "5"

survey['leave'] = survey['leave'].apply(leave)

# removes empty rows
survey.dropna(subset=['work_interfere'], inplace=True)

# hani: cleaned work_interfere column
def interfere(x):
    if x in {"Often", 1}:
        return "1"
    if x in {"Sometimes", 2}:
        return "2"
    if x in {"Rarely", 3}:
        return "3"
    if x in {"Never", 4}:
        return "4"

survey['work_interfere'] = survey['work_interfere'].apply(interfere)

# amina: cleaned gender column
def categorize_gender(gender):
    if gender.lower() in {'m', 'male', 'man', 'guy', 'cis male'}:
        return 'male'
    elif gender.lower() in {'f', 'female', 'woman', 'w', 'cis female'}:
        return 'female'
    else:
        return 'other'

survey['Gender'] = survey['Gender'].apply(categorize_gender)

# amina: cleaned age column
survey = survey[(survey['Age'] >= 18) & (survey['Age'] <= 70)]

# commiting the changes to the file
survey.to_csv('survey.csv', index=False)