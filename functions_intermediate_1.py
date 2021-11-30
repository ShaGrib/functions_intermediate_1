# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def new_vals():
    x[1][0] = 15
    students[0]['last_name'] = 'Bryant'
    sports_directory['soccer'][0] = 'Andres'
    z[0]['y'] = 30

new_vals()
print(x)
print(students)
print(sports_directory)
print(z)

#2. Create a function iterateDictionary(some_list) that, given a list of dictionaries,
# the function loops through each dictionary in the list and prints each key and the
# associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterate_dictionary():
    for i in range(len(students)):
        print(students[i])
    
iterate_dictionary()

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
#the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students)
# should output:
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

def iterate_dictionary2(keys, students):
# a = students[0]['first_name']
# b = students[0]['last_name']
    for x in students:
        print(x[keys])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name
# of each key along with the size of its list, and then prints the associated values within each key's list.
# For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dojo, keystat):
        print(len(dojo[keystat]),keystat)
        print(*dojo[keystat],sep='\n')

print('----------------------')
print_info(dojo, 'locations')
print('----------------------')
print_info(dojo, 'instructors')


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

