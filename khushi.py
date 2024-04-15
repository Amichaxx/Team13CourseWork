import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

def culture():

    countries = ['United States', 'United Kingdom']
    
    sa_y = data[(data['Country'] ==  'United States') & (data['treatment'] == 'Yes')].shape[0]
    ja_y = data[(data['Country'] == 'United Kingdom') & (data['treatment'] == 'Yes')].shape[0]

    sa_n = data[(data['Country'] ==  'United States') & (data['treatment'] == 'No')].shape[0]
    ja_n = data[(data['Country'] == 'United Kingdom') & (data['treatment'] == 'No')].shape[0] 
    
    yes_labels = [sa_y, ja_y]
    no_labels = [sa_n, ja_n]
    
    x_length = range(len(countries))
    width = 0.25

    plt.bar(countries, yes_labels, width=width, color='blue', label='seeked help')
    plt.bar([x + width for x in x_length], no_labels, width=width, color='pink', label='not seeked help')
                                                                            
                                        
    plt.title('Effect of Cultural Distinction ')
    plt.xlabel('Country')
    plt.ylabel('Number of employees')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    print(data[data["Country"] == 'United Kingdom'])
    
culture()