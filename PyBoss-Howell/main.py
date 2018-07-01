import os
import csv 
from pandas import pandas as pd


#choose 1 or 2
file_num = 2

#creates file path as file
#file = os.path.join('employee_data1.csv')
file = os.path.join('employee_data2.csv')
#file = os.path.join("raw_data", input("Please input the entire file name: "))

# state abbr dictionary that was provided
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# empty lists for parsed data
emp_id = []
first_name = []
last_name = []
dob =[]
ssn = []
state = []

# opens csv file and reads in as dictionary
# no need to skip header row because it's the same as the dictonary key
with open(file, 'r') as csvfile:  
    reader = csv.DictReader(csvfile)
    # appends information to empty lists after being altered
    for row in reader:
        emp_id.append(row['Emp ID'])
        first_name.append(row['Name'].split(" ")[0])
        last_name.append(row['Name'].split(" ")[1])
        dob.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        ssn.append('***-**-' + row['SSN'].split('-')[2])
        state.append(us_state_abbrev[row['State']])


# zips lists together
new_data = zip(emp_id, first_name, last_name, dob, ssn, state)

# names output file as emp_data_clean
output_file = os.path.join('emp_data_clean' + str(file_num) + '.csv')

# Writes the results to a new CSV file
with open(output_file, 'w') as csvwrite:
    clean_file = csv.writer(csvwrite, delimiter = ",")
    clean_file.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    clean_file.writerows(new_data)

#print("Do you have another file? Y or N ")    