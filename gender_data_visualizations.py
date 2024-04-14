import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv("survey.csv")

def mental_health_by_gender():
# Filter data for each gender
    female_data = data[data['Gender'] == 'female']
    male_data = data[data['Gender'] == 'male']
    other_data = data[data['Gender'] == 'other']

    # Count responses for each supervisor level
    female_supervisor_counts = female_data['supervisor'].value_counts().sort_index()
    male_supervisor_counts = male_data['supervisor'].value_counts().sort_index()
    other_supervisor_counts = other_data['supervisor'].value_counts().sort_index()

    # Plot the results
    x_labels = ['Yes', 'Some of them', 'No']
    plt.figure(figsize=(8, 6))
    plt.bar(x_labels, female_supervisor_counts, color='purple', label='Female')
    plt.bar(x_labels, male_supervisor_counts, color='teal', label='Male', bottom=female_supervisor_counts)
    plt.bar(x_labels, other_supervisor_counts, color='turquoise', label='Other', bottom=male_supervisor_counts + female_supervisor_counts)
    

    plt.title('Supervisor Reports by Gender', fontname="Times New Roman", fontsize=18)
    plt.xlabel("Supervisor Reports", fontname="Times New Roman", fontsize=12) 
    plt.ylabel("Number of Responses", fontname="Times New Roman", fontsize=12) 
    plt.legend()
    plt.show()

def treatment_by_tech_gender():
    # Filter data for tech company employees receiving treatment
    tech_treatment_data = data[(data['tech_company'] == 'Yes') & (data['treatment'] == 'Yes')]

    # Group filtered tech_treatment_data by gender and count the number of individuals
    gender_counts = tech_treatment_data['Gender'].value_counts().sort_index()

    # Create a horizontal bar chart 
    # Custom colors for female, male, and other
    colors = ['#800080', '#4169E1', '#228B22'] 

    plt.figure(figsize=(10, 6))
    plt.barh(gender_counts.index, gender_counts.values, color=colors)
    plt.xlabel('Tech Employees Recieving Treatment', fontname="Times New Roman", fontsize=15)
    plt.ylabel('Gender', fontname="Times New Roman", fontsize=15, )
    plt.title('Treatment by Gender in Tech Companies', fontname="Times New Roman", fontsize=18)
    plt.tight_layout()

    # Show the plot
    plt.show()
        



