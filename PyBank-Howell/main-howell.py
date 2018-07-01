# import dependencies 
from pandas import pandas
import os
import csv
import sys


#Read in files with names budget_one and budget_two
budget_one_path = os.path.join('budget_data_1.csv')
budget_two_path = os.path.join('budget_data_2.csv')

df1 = pandas.read_csv(budget_one_path)
df2 = pandas.read_csv(budget_two_path)

#print (df1)
#print (df2)

#Use column attribut for two files
df1.columns
df2.columns
#print (df1.columns, df2.columns)

#The total number of months included in the datasets one and two
months1 = df1["Date"].count()
months2 = df2["Date"].count()
#print (months1)
#print (months2)

#The total amount of revenue gained over both periods one and two
total_rev1 = df1["Revenue"].sum()
total_rev2 = df2["Revenue"].sum()
#print (total_rev1)
#print (total_rev2)


#The average change in revenue between months over both periods one and two
avg_rev1 = df1["Revenue"].mean()
avg_rev2 = df2["Revenue"].mean()
#print(avg_rev1)
#print(avg_rev2)

#The greatest decrease in revenue (date and amount) over tboth periods one and twod
max_rev1 = df1["Revenue"].max()
max_rev2 = df2["Revenue"].max()
#print(max_rev1)
#print(max_rev2)

#locates the date that corresponds to the max revenue for budget one and two respectively
date1 = df1.loc[df1["Revenue"] == max_rev1, "Date"]
max_date1 = date1.iloc[0]
#print(max_date1)

date2 = df2.loc[df2["Revenue"] == max_rev2, "Date"]
max_date2 = date2.iloc[0]
#print(max_date2)

#The greatest increase in revenue (date and amount) over both periods one and two
min_rev1 = df1["Revenue"].min()
min_rev2 = df2["Revenue"].min()
#print(min_rev1)
#print(min_rev2)

#locates the date that corresponds to the min revenue for budget one and two respectively
min_date1 = df1.loc[df1["Revenue"] == min_rev1, "Date"]
min_date1_loc = date1.iloc[0]
#print(min_date1_loc)

min_date2 = df2.loc[df2["Revenue"] == min_rev2, "Date"]
min_date2_loc = date2.iloc[0]
#print(min_date2_loc)

#print statements in terminal
print("Financial Analysis for Data Set 1\n ---------------------------- \n")
print(f" Total Months: {months1}\n Total Revenue: {total_rev1}\n Average Revenue Change: {avg_rev1}\n Greatest Increase in Revenue: {max_date1} {max_rev1}\n Greatest Decrease in Revenue: {min_date1_loc} {min_rev1}")

print(" ")
print(" ")

print("Financial Analysis for Data Set 2\n ---------------------------- \n")
print(f" Total Months: {months2}\n Total Revenue: {total_rev2}\n Average Revenue Change: {avg_rev2}\n Greatest Increase in Revenue: {max_date2} {max_rev2}\n Greatest Decrease in Revenue: {min_date2_loc} {min_rev2}")


#print statements in seperate text file within the same directory
analysis = sys.stdout
sys.stdout = open('financial-analysis.txt', 'w')
print("Financial Analysis for Data Set 1\n ---------------------------- \n")
print(f" Total Months: {months1}\n Total Revenue: {total_rev1}\n Average Revenue Change: {avg_rev1}\n Greatest Increase in Revenue: {max_date1} {max_rev1}\n Greatest Decrease in Revenue: {min_date1_loc} {min_rev1}")

print(" ")
print(" ")

print("Financial Analysis for Data Set 2\n ---------------------------- \n")
print(f" Total Months: {months2}\n Total Revenue: {total_rev2}\n Average Revenue Change: {avg_rev2}\n Greatest Increase in Revenue: {max_date2} {max_rev2}\n Greatest Decrease in Revenue: {min_date2_loc} {min_rev2}")
sys.stdout.close() 
sys.stdout = analysis  