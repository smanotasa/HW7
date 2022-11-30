# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.

def car_at_light(light):
    if light == 'red':
        return str("stop")
    if light == 'yellow':
        return str("wait")
    else:
        if light == 'green':
            return str("go")
        else: raise Exception("Undefined instruction for color: " + str(light))

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 

def safe_subtract(a,b):
  if type(a)==float or type(a)==int and type (b)==float or type(b)==int:
    return a-b 
  else: return str("None")

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def retrieve_age_lbyl(dict):
  if 'birth' in dict:
    print(2022 - dict['birth'])
  else: print("Some keys are missing")

def retrieve_age_eafp(dict):
  try:
    print(2022 - dict['birth'])
  except KeyError:
    print("Some keys are missing")

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 

def read_data(file):
  try:
    csvreader = csv.reader(file)
  except NameError:
    print('There is no such file')

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them

### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

#It is doing the sum of the elements instead of the sum of the elements doubled

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings += str(string +"_")
strings = strings[:-1]
print(strings)

# It is producing three different strings where it sums each given string two times separated by "_" like "I_I", "am_am" and "Groot_Groot" 
# and giving as an output only the last one. It is not combining the three strings from the list onto one string.

### (c) Careful!
j=10
while j < 20:
    print(j)
    j+= 1

#A while loop executes a statement given set conditions. Here, the problem is not setting a limit for the loop, since we have
#j>0 no limit is set for the loop. It will continously run with no end. Also, a print is missing in the while loop, which means
#that the loop won't show results either given that j+=1 is not indented after a print.

### (d)
productory = 1
for elem in [1, 5, 25]:
    productory *= elem

print(productory)

#Given it is a multiplication, productory should be equal to 1 instead of 0.

################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 


list=[]
def count_simba(x):
  return str(x).count('Simba')

print(sum(map(lambda x: count_simba(x), list)))

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.

import pandas as pd
import datetime

def get_day_month_year(dates: list):
    df_dates = pd.DataFrame(dates, columns=['date'])
    m_date = df_dates.date.apply(lambda x: (x.year, x.month, x.day))
    year, month, day = [], [], []
    for i in m_date:
        year.append(i[0])
        month.append(i[1]) 
        day.append(i[2]) 
    df = pd.DataFrame(zip(day, month, year), columns = ['day', 'month', 'year'])
    return df

# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance

from geopy.distance import geodesic as GD

def compute_distance(a,b): 
  return round(GD(a,b).km,2)

print(list(map(compute_distance, ((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8)))))

# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13

def sum_general_int_list(list) :
    total = 0
    for item in list:
        try:
            total += item
        except TypeError:
            total += sum_general_int_list(item)
    return total