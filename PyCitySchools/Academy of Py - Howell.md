

```python
<h1>Option 2: Academy of Py</h1>
<h3>Randi Howell<br>
Assignment 4 - Pandas</h3>

Well done! Having spent years analyzing financial records for big banks, you have finally scratched your idealistic itch and joined the education sector. In your latest role, you've become the Chief Data Scientist for your city's school district. In this capacity, you'll be helping the school board and mayor make strategic decisions regarding future school budgets and priorities.

As a first task, you haveve been asked to analyze the district-wide standardized test results. You will be given access to every student's math and reading scores, as well as various information on the schools they attend. Your responsibility is to aggregate the data to and showcase obvious trends in school performance.

Your final report should include each of the following:

District Summary

Create a high level snapshot (in table form) of the district's key metrics, including:

<ul>
    <li>Total Schools</li>
    <li>Total Students</li>
    <li>Total Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>School Summary</li>
</ul>


Create an overview table that summarizes key metrics about each school, including:
<ul>
    <li>School Name</li>
    <li>School Type</li>
    <li>Total Students</li>
    <li>Total School Budget</li>
    <li>Per Student Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>Top Performing Schools (By Passing Rate)</li>
</ul>

Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
<ul>
    <li>School Name</li>
    <li>School Type</li>
    <li>Total Students</li>
    <li>Total School Budget</li>
    <li>Per Student Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>Top Performing Schools (By Passing Rate)</li>
</ul>

Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.
<ul>
    <li>Math Scores by Grade</li>
</ul>

Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
<ul>
    <li>Reading Scores by Grade</li>
</ul>


Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
<ul>
    <li>Scores by School Spending</li>
</ul>


Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
<ul>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>Scores by School Size</li>
</ul>

Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).
<ul>
    <li>Scores by School Type</li>
</ul>

Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).


As final considerations:
<ul>
    <li>Scores by School Type</li>
    <li>Your script must work for both data-sets given.</li>
    <li>You must use the Pandas Library and the Jupyter Notebook.</li>
    <li>You must submit a link to your Jupyter Notebook with the viewable Data Frames.</li>
    <li>You must include an exported markdown version of your Notebook called  README.md in your GitHub repository.</li>
    <li>You must include a written description of three observable trends based on the data.</li>
    <li>See Example Solution for a reference on the expected format.</li>
</ul>



Hints and Considerations
<ul>
    <li>These are challenging activities for a number of reasons. For one, these activities will require you to analyze thousands of records. Hacking through the data to look for obvious trends in Excel is just not a feasible option. The size of the data may seem daunting, but Python Pandas will allow you to efficiently parse through it.</li>

    <li>Second, these activities will also challenge you by requiring you to learn on your feet. Don't fool yourself into thinking: "I need to study Pandas more closely before diving in." Get the basic gist of the library and then immediately get to work. When facing a daunting task, it's easy to think: "I'm just not ready to tackle it yet." But that's the surest way to never succeed. Learning to program requires one to constantly tinker, experiment, and learn on the fly. You are doing exactly the right thing, if you find yourself constantly practicing Google-Fu and diving into documentation. There is just no way (or reason) to try and memorize it all. 
        Online references are available for you to use when you need them. So use them!</li>

    <li>Take each of these tasks one at a time. Begin your work, answering the basic questions: "How do I import the data?" "How do I convert the data into a DataFrame?" "How do I build the first table?" Don't get intimidated by the number of asks. Many of them are repetitive in nature with just a few tweaks. Be persistent and creative!'</li>

    <li>Expect these exercises to take time! Don't get discouraged if you find yourself spending hours initially with little progress. Force yourself to deal with the discomfort of not knowing and forge ahead. This exercise is likely to take between 15-30 hours of your time. Consider these hours an investment in your future!'</li>

    <li>As always, feel encouraged to work in groups and get help from your TAs and Instructor. Just remember, true success comes from mastery and not a completed homework assignment. So challenge yourself to truly succeed!</li>
</ul>
```

<h4>Initial Set-Up: </h4>


```python
# Import Dependencies

import csv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
# Read in file 
school_file = "PyCitySchools/raw_data/schools_complete.csv"
student_file = "PyCitySchools/raw_data/students_complete.csv"

# Store imported files as new DFs
school_df = pd.read_csv(school_file)
student_df = pd.read_csv(student_file)

## Print statements are included for checking purposes - can be deleted if neccessary 
## Print rows of each DF:
# school_df
# student_df
```


```python
# Rename col "name" in school_df to "school name"
school_df.rename_axis({"name" : "school name"}, axis=1, inplace=True)

# Make a copy of school_df to manipulate and reuse later throughout the code
# Store renamed school_df as new df
copy_school_sum = school_df.copy()


## Print statements are included for checking purposes - can be deleted if neccessary 
## Print both DFs to verify that the columns are the same
#school_df.columns
#copy_school_sum.columns
```


```python
# Rename col "school" in student_df to "school name"
# Store renamed student_df as new df
renamed_student_df = student_df.rename(columns={"school" : "school name"})


## Print statements are included for checking purposes - can be deleted if neccessary 
## Print both DFs to verify that the columns are the same
#renamed_student_df.columns
```

<h4>Part One: District Summary</h4>

<ul>
    <li>Total Schools</li>
    <li>Total Students</li>
    <li>Total Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>School Summary</li>
</ul>


```python
## Total Schools
total_schools = school_df["school name"].count()
#print(total_schools)


## Total Students
total_students = renamed_student_df["school name"].count()
#print(total_students)

## Total Budget
total_budget = school_df["budget"].sum()

## Average Math Score
avg_math_score = renamed_student_df["math_score"].mean()

## Average Reading Score
avg_read_score = renamed_student_df["reading_score"].mean()
```


```python
## % Passing Math based on 70
math_pass = renamed_student_df.loc[(student_df["math_score"] >= 70)]

count_pass_math = math_pass["math_score"].count()
#print(count_pass_math)

per_math_pass = (count_pass_math/total_students)*100
#print(per_math_pass)
```


```python
## % Passing Reading based on 70
read_pass = renamed_student_df.loc[(student_df["reading_score"] >= 70)]

count_pass_read = read_pass["reading_score"].count()
#print(count_pass_read)

per_read_pass = (count_pass_read/total_students)*100
#print(per_read_pass)
```


```python
## Overall Passing Rate (Average of the above two)
overall_pass = (per_math_pass + per_read_pass)/2
#print(overall_pass)
```


```python
district_summary = {"Total Schools" : total_schools,
                   "Total Students" : total_students,
                   "Total Budget" : total_budget,
                   "Average Math Score" : avg_math_score,
                   "Average Reading Score" : avg_read_score,
                    "% Passing Math" : per_math_pass,
                   "% Passing Reading" : per_read_pass,
                   "% Overall Passing" : overall_pass
                  }


district_summary_df = pd.DataFrame([district_summary])                                              
                                   
district_summary_df = district_summary_df[["Total Schools",
                   "Total Students","Total Budget","Average Math Score", "Average Reading Score",
                   "% Passing Math", "% Passing Reading", "% Overall Passing" ]]


```

<h4>District Summary Table</h4>


```python
district_summary_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>74.980853</td>
      <td>85.805463</td>
      <td>80.393158</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Part Two: School Summary</h4>
<br>
Create an overview table that summarizes key metrics about each school, including:
<ul>
    <li>School Name</li>
    <li>School Type</li>
    <li>Total Students</li>
    <li>Total School Budget</li>
    <li>Per Student Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>Top Performing Schools (By Passing Rate)</li>
</ul>

<b>We will use copy_school_sum for this portion</b>
<br>


```python
# First, we will delete the School ID col from copy_school_sum because we will not need it for future use
del copy_school_sum['School ID']

# We can print copy_school_sum to verify the del
# copy_school_sum
```


```python
## Calculate the Per Student Budget
## We will pull the school budget and divide it by the school size to determine the budget per student
## Then, we will create a new col named 'Per Student Budget'

copy_school_sum['Per Student Budget'] = copy_school_sum['budget']/copy_school_sum['size']

# copy_school_sum
```


```python
## Average Math Score & Average Reading Score
## We will use a groupby function to group on school name and display both reading and math scores from above
## then reset the index

avg_math_read_tbl = renamed_student_df.groupby(['school name'])['reading_score', 'math_score'].mean().reset_index()

# avg_math_read_tbl
```


```python
## Now, we merge avg_math_read_tbl with copy_school_sum df
## We want to merge on School Name and by 'outer' to include everything

copy_school_sum = copy_school_sum.merge(avg_math_read_tbl, on='school name', how="outer")

#copy_school_sum
```


```python
## We will use conditionals to find the % Passing Math and % Passing Reading
## Then, we will store them as new variabels
## We are using a passrate of 70% or higher

# % Passing Reading
summary_passing_read = renamed_student_df[renamed_student_df['reading_score']>=70]

#% Passing Math
summary_passing_math = renamed_student_df[renamed_student_df['math_score']>=70]

#summary_passing_read
#summary_passing_math
```


```python
## Count the number of students passing in reading 
pass_read_count_sum = summary_passing_read.groupby(["school name"])['reading_score'].count().reset_index()

## Then, rename the column the 'reading_score' to 'Reading Count'
pass_read_count_sum.rename_axis({'reading_score' : 'Reading Count'}, axis=1, inplace=True)

#pass_read_count_sum
```


```python
## Count the number of students passing in math 
pass_math_count_sum = summary_passing_math.groupby(["school name"])['math_score'].count().reset_index()

## Then, rename the column the 'math_score' to 'Math Count'
pass_math_count_sum.rename_axis({'math_score' : 'Math Count'}, axis=1, inplace=True)

#pass_math_count_sum
```


```python
## Merge pass_math_count_sum with pass_read_count_sum
## We want to merge on School Name and by 'inner' to include only the contents found in both columns

pass_count = pass_math_count_sum.merge(pass_read_count_sum, on="school name", how='inner')

#pass_count
```


```python
## Merge copy_school_sum with pass_count we just created
## We want to merge on School Name and by 'outer' to include everything

copy_school_sum = copy_school_sum.merge(pass_count, on="school name", how='outer')

#copy_school_sum
```


```python
## Calc % passing math and reading
## Take the subject count and divide by the school size, then pmultiply by 100 to get percentage

# % Passing Math
copy_school_sum['% Passing Math'] = (copy_school_sum['Math Count']/copy_school_sum['size'])*100

# % Passing Reading
copy_school_sum['% Passing Reading'] = (copy_school_sum['Reading Count']/copy_school_sum['size'])*100

#copy_school_sum
```


```python
# Now, we will delete the Math Count and Reading Count cols from copy_school_sum 
# because we will not need the counts for future use

del copy_school_sum['Math Count']
del copy_school_sum['Reading Count']

#copy_school_sum
```


```python
## Calc % overall passing 
## Overall Passing Rate (Average of the above two)

copy_school_sum['% Overall Passing'] = (copy_school_sum['% Passing Math'] + copy_school_sum['% Passing Reading'])/2

#copy_school_sum
```


```python
# now, rename axis for reading and math scores to Avg. Reading Score and Avg. Math Score in copy_school_sum
copy_school_sum.rename_axis({'reading_score':'Avg. Reading Score',
                             'math_score':'Avg. Math Score'}, axis=1, inplace=True)
```

<h4>School Summary Table</h4>


```python
copy_school_sum
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>Avg. Reading Score</th>
      <th>Avg. Math Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>94.860875</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>73.807983</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>95.203679</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>95.586652</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>74.306672</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>94.379391</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>95.270270</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>94.972222</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>73.639992</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>73.804308</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>93.272171</td>
      <td>97.308869</td>
      <td>95.290520</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Part Three: Top 5 performing schools</h4>
    
Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
<ul>
    <li>School Name</li>
    <li>School Type</li>
    <li>Total Students</li>
    <li>Total School Budget</li>
    <li>Per Student Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
    <li>Top Performing Schools (By Passing Rate)</li>
</ul>


```python
## Create a table that highlights the top 5 performing schools based on Overall Passing Rate. 
## Found the top 5 performing by sorting copy_school_sum on the '% Overall Passing' col in copy_school_sum df 
## By sorting, we can find the five top performing

top_performing_by_pr_df = copy_school_sum.sort_values(by=['% Overall Passing'], ascending=False).head(5)
```

<h4>Top 5 performing schools based on Overall Passing Rate</h4>


```python
top_performing_by_pr_df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>Avg. Reading Score</th>
      <th>Avg. Math Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
      <th>Spending Level</th>
      <th>School Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>95.586652</td>
      <td>$570-$591</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>93.272171</td>
      <td>97.308869</td>
      <td>95.290520</td>
      <td>$628.01-$641.51</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>95.270270</td>
      <td>$591.51-$628.01</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
      <td>$591.51-$628.01</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>95.203679</td>
      <td>$570-$591</td>
      <td>Large</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Part Four: Bottom 5 performing schools</h4>
   
Include:
<ul>
    <li>School Name</li>
    <li>School Type</li>
    <li>Total Students</li>
    <li>Total School Budget</li>
    <li>Per Student Budget</li>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
</ul>


```python
## Create a table that highlights the 5 worst performing schools based on Overall Passing Rate. 
## Include all of the same metrics as above.
## Using the copy_school_sum df found the bottom 5 performing schools based on Overall Passing Rate col
worst_performing_by_pr_df = copy_school_sum.sort_values(by=['% Overall Passing']).head(5)

```

<h4>Bottom 5 performing schools</h4>


```python
worst_performing_by_pr_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>Avg. Reading Score</th>
      <th>Avg. Math Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
      <th>Spending Level</th>
      <th>School Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>73.293323</td>
      <td>$628.01-$641.51</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
      <td>$628.01-$641.51</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
      <td>$645-$675</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>73.639992</td>
      <td>$645-$675</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>73.804308</td>
      <td>$645-$675</td>
      <td>Large</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Part 5: Math Scores by Grade</h4>

Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


```python
# We will use the pivot table group to display the requested information
math_scores_by_grade_df = pd.pivot_table(student_df, values=['math_score'], index=['school'], 
                                         columns=['grade'])
math_scores_by_grade_df = math_scores_by_grade_df.reindex_axis(labels=['9th',
                                                                    '10th',
                                                                    '11th',
                                                                    '12th'], axis=1, level=1)
```

<h4>Math Scores by Grade</h4>


```python
math_scores_by_grade_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">math_score</th>
    </tr>
    <tr>
      <th>grade</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Part 6: Reading Scores by Grade</h4>

Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


```python
# will use the pivot table group to display
read_scores_by_grade_df = pd.pivot_table(student_df, values=['reading_score'], index=['school'], 
                                         columns=['grade'])
read_scores_by_grade_df = read_scores_by_grade_df.reindex_axis(labels=['9th',
                                                                    '10th',
                                                                    '11th',
                                                                    '12th'], axis=1, level=1)
```

<h4>Reading Scores by Grade</h4>



```python
read_scores_by_grade_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">reading_score</th>
    </tr>
    <tr>
      <th>grade</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Part 7: Scores by School Spending</h4>

Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:

<ul>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
</ul>


```python
# Copy the copy_school_sum and save as scores_by_school_spending
scores_by_school_spending = copy_school_sum.copy()

# Print columns of each to verify they're the same
# copy_school_sum
# scores_by_school_spending.columns
```


```python
# Create bins - we will need labels and bins
bins = [570, 591.51, 628.01, 641.51, 655.00]
spending_labels = ['$570-591', '$591.51-628.01', '$628.01-641.51', '$645-675']
```


```python
# Use bins and labels to sort through data and divide it up appropriately 
# save bined data as bins_school_spending variable 
bins_school_spending = pd.cut(scores_by_school_spending['Per Student Budget'], bins, labels=spending_labels)

# Convert bins_school_spending to df
bins_school_spending = pd.DataFrame(bins_school_spending)

# add Spending Level col 
copy_school_sum['Spending Level'] = bins_school_spending
```


```python
# Show cols for bins_school_spending to verify 
#bins_school_spending.columns
```


```python
# Do a groupby on Spending Level and school name
scores_by_school_spending = copy_school_sum.groupby(['Spending Level','school name'])['Avg. Reading Score',
                                                         'Avg. Math Score',
                                                         '% Passing Reading',
                                                         '% Passing Math',
                                                         '% Overall Passing'
                                                         ].mean()

```

<h4>Scores by School Spending</h4>



```python
scores_by_school_spending
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Avg. Reading Score</th>
      <th>Avg. Math Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>Spending Level</th>
      <th>school name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">$570-591</th>
      <th>Cabrera High School</th>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>97.039828</td>
      <td>94.133477</td>
      <td>95.586652</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>96.252927</td>
      <td>92.505855</td>
      <td>94.379391</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>96.539641</td>
      <td>93.867718</td>
      <td>95.203679</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>96.611111</td>
      <td>93.333333</td>
      <td>94.972222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">$591.51-628.01</th>
      <th>Bailey High School</th>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>81.933280</td>
      <td>66.680064</td>
      <td>74.306672</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>97.138965</td>
      <td>93.392371</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>95.945946</td>
      <td>94.594595</td>
      <td>95.270270</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>95.854628</td>
      <td>93.867121</td>
      <td>94.860875</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">$628.01-641.51</th>
      <th>Figueroa High School</th>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>80.739234</td>
      <td>65.988471</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>80.220055</td>
      <td>66.366592</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>97.308869</td>
      <td>93.272171</td>
      <td>95.290520</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">$645-675</th>
      <th>Ford High School</th>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>79.299014</td>
      <td>68.309602</td>
      <td>73.804308</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>80.862999</td>
      <td>66.752967</td>
      <td>73.807983</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>81.316421</td>
      <td>65.683922</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>81.222432</td>
      <td>66.057551</td>
      <td>73.639992</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Scores by School Size</h4>
This time group schools based on a reasonable approximation of school size (Small, Medium, Large).
<ul>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
</ul>



```python
# Create a copy of copy_school_sum and save as scores_by_school_size
scores_by_school_size = copy_school_sum.copy()

# Print scores_by_school_size to verify
# scores_by_school_size
```


```python
# Create bins - we will need labels and bins
bins = [0, 1000, 2000, 5000]
size_labels = ['Small', 'Medium', 'Large']
```


```python
# Use bins and labels to sort through data and divide it up appropriately 
# save bin data as bins_school_size variable 
bins_school_size = pd.cut(scores_by_school_size['size'], bins, labels = size_labels)

# Convert bins_school_spending to df
bins_school_size = pd.DataFrame(bins_school_size)

# add 'School Population' col 
copy_school_sum['School Population'] = bins_school_size
```


```python
# Show cols for bins_school_size to verify 
# bins_school_size.columns
```


```python
# Do a groupby on School Population and school name
scores_by_school_size = copy_school_sum.groupby(['School Population','school name'])['Avg. Reading Score',
                                                         'Avg. Math Score',
                                                         '% Passing Reading',
                                                         '% Passing Math',
                                                         '% Overall Passing'
                                                         ].mean()
```

<h4>Scores by School Size</h4>


```python
scores_by_school_size
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Avg. Reading Score</th>
      <th>Avg. Math Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School Population</th>
      <th>school name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">Large</th>
      <th>Bailey High School</th>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>81.933280</td>
      <td>66.680064</td>
      <td>74.306672</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>80.739234</td>
      <td>65.988471</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>79.299014</td>
      <td>68.309602</td>
      <td>73.804308</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>80.862999</td>
      <td>66.752967</td>
      <td>73.807983</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>81.316421</td>
      <td>65.683922</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>81.222432</td>
      <td>66.057551</td>
      <td>73.639992</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>80.220055</td>
      <td>66.366592</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>96.539641</td>
      <td>93.867718</td>
      <td>95.203679</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Medium</th>
      <th>Cabrera High School</th>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>97.039828</td>
      <td>94.133477</td>
      <td>95.586652</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>97.138965</td>
      <td>93.392371</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>95.854628</td>
      <td>93.867121</td>
      <td>94.860875</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>97.308869</td>
      <td>93.272171</td>
      <td>95.290520</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>96.611111</td>
      <td>93.333333</td>
      <td>94.972222</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Small</th>
      <th>Holden High School</th>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>96.252927</td>
      <td>92.505855</td>
      <td>94.379391</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>95.945946</td>
      <td>94.594595</td>
      <td>95.270270</td>
    </tr>
  </tbody>
</table>
</div>



<h4>Scores by School Type</h4>
This time group schools based on school type (Charter vs. District).
<ul>
    <li>Average Math Score</li>
    <li>Average Reading Score</li>
    <li>% Passing Math</li>
    <li>% Passing Reading</li>
    <li>Overall Passing Rate (Average of the above two)</li>
</ul>



```python
# Create a copy of copy_school_sum and save as scores_by_school_type
scores_by_school_type = copy_school_sum.copy()

# Convert scores_by_school_type to df
scores_by_school_type = pd.DataFrame(scores_by_school_type)

# Print scores_by_school_type cols to verify
# scores_by_school_type.columns
```


```python
# Do a groupby on School Type
scores_by_school_type = copy_school_sum.groupby(['type'])['Avg. Reading Score',
                                                         'Avg. Math Score',
                                                         '% Passing Reading',
                                                         '% Passing Math',
                                                         '% Overall Passing'
                                                         ].mean()

```

<h4>Scores by School Type</h4>


```python
scores_by_school_type.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg. Reading Score</th>
      <th>Avg. Math Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.896421</td>
      <td>83.473852</td>
      <td>96.586489</td>
      <td>93.620830</td>
      <td>95.103660</td>
    </tr>
    <tr>
      <th>District</th>
      <td>80.966636</td>
      <td>76.956733</td>
      <td>80.799062</td>
      <td>66.548453</td>
      <td>73.673757</td>
    </tr>
  </tbody>
</table>
</div>


