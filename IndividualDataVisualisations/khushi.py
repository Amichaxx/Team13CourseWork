import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")
print("--- Which continent has the highest mental health issues? ---")

seekYes = data[(data['seek_help'] == 1)]
seekNo = data[(data['seek_help'] == 2)] 
seekUnsure = data[(data['seek_help'] == 3)]
            
        
northAmerica = (data['Country'] == 'United States') | (data['Country'] == 'Canada') | (data['Country'] == 'Mexico')
southAmerica = (data['Country'] == 'Brazil') | (data['Country'] == 'Colombia')
oceania = (data['Country'] == 'Australia') | (data['Country'] == 'New Zealand')
africa = (data['Country'] == 'South Africa')
asia= (data['Country'] == 'India') | (data['Country'] == 'Thailand') | (data['Country'] == 'Japan')| (data['Country'] == 'Philippines')| (data['Country'] == 'China')| (data['Country'] == 'Singapore')
europe = (data['Country'] == 'United Kingdom') | (data['Country'] == 'Bulgaria') | (data['Country'] == 'Netherland')| (data['Country'] == 'Poland')| (data['Country'] == 'France')| (data['Country'] == 'Germany')| (data['Country'] == 'Slovenia')| (data['Country'] == 'Ireland')| (data['Country'] == 'Russia')| (data['Country'] == 'Italy')| (data['Country'] == 'Portugal')| (data['Country'] == 'Switzerland')| (data['Country'] == 'Belgium')| (data['Country'] == 'Sweden')| (data['Country'] == 'Finland')| (data['Country'] == 'Bosnia and Herzegovina')| (data['Country'] == 'Austria')| (data['Country'] == 'Hungary')| (data['Country'] == 'Crotia')| (data['Country'] == 'Denmark')| (data['Country'] == 'Moldova')| (data['Country'] == 'Georgia')| (data['Country'] == 'Czech Republic')                               
x_labels=['North America', 'South America', 'Oceania', 'Africa', 'Asia', 'europe']
           
na_y = data[(northAmerica) & (data['seek_help'] == 1)].shape[0]
sa_y = data[(southAmerica) & (data['seek_help'] == 1)].shape[0]
oc_y = data[(oceania) & (data['seek_help'] == 1)].shape[0] # 10
af_y = data[(africa) & (data['seek_help'] == 1)].shape[0] # 0
as_y = data[(asia) & (data['seek_help'] == 1)].shape[0]
eu_y = data[(europe) & (data['seek_help'] == 1)].shape[0]
            
na_n = data[(northAmerica) & (data['seek_help'] == 2)].shape[0]
sa_n = data[(southAmerica) & (data['seek_help'] == 2)].shape[0]
oc_n = data[(oceania) & (data['seek_help'] == 2)].shape[0] # 10
af_n = data[(africa) & (data['seek_help'] == 2)].shape[0] # 0
as_n = data[(asia) & (data['seek_help'] == 2)].shape[0]
eu_n = data[(europe) & (data['seek_help'] == 2)].shape[0]

na_us = data[(northAmerica) & (data['seek_help'] == 3)].shape[0]
sa_us = data[(southAmerica) & (data['seek_help'] == 3)].shape[0]
oc_us = data[(oceania) & (data['seek_help'] == 3)].shape[0] # 10
af_us = data[(africa) & (data['seek_help'] == 3)].shape[0] # 0
as_us = data[(asia) & (data['seek_help'] == 3)].shape[0]
eu_us = data[(europe) & (data['seek_help'] == 3)].shape[0]
            
yes_labels=[na_y, sa_y, oc_y, af_y, as_y, eu_y]
no_labels=[na_n, sa_n, oc_n, af_n, as_n, eu_n]
unsure_labels=[na_us, sa_us, oc_us, af_us, as_us, eu_us]
    
plt.plot(x_labels, yes_labels, color='red', label='Experienced mental health')
plt.plot(x_labels, no_labels, color='green', label='Not experienced mental health')
plt.plot(x_labels, unsure_labels, color='purple', label='Unsure ')
        
#plt.plot(country_ref3, color='green', label='Unsure')

plt.title('Most common country for experiencing mental health')
plt.xlabel('Country')
plt.ylabel('Number of employees')
plt.grid(True)
plt.legend()
plt.show()

def treatment():

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
                                                                            
                                        
    plt.title('sought treatment for mental health')
    plt.xlabel('Country')
    plt.ylabel('Number of responses')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    print(data[data["Country"] == 'United Kingdom'])
    
treatment()