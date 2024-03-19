import pandas as pd  
# Load the dataset  
survey = pd.read_csv('survey.csv')
# Create a function to categorize company size
def categorize_company_size(employee_count):
    if employee_count in {"1-5", "6-25", "26-100"}:
        return "Small"
    elif employee_count in {"100-500"}:
        return "Medium"
    else:
        return "Large"
    
survey['no_employees'] = survey['no_employees'].apply(categorize_company_size)

survey.to_csv('cleaned_csv_file.csv', index=False)