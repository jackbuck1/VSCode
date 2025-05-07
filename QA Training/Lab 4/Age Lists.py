# Record the length of the ages List in a variable (you'll need it later) Display the length. Test your code.
#2. Display these ages one on each line: Tip: Use a for loop to read each number.
#3. Add one year to every age!
#4. Our code only takes into account those people in the age range of 16-65 (inclusively) Please delete all ages which are outside this range.
#5. Display the count of 16-25 year olds.
#6. Invoke the sort method on the ages List.
#7. What proportion of ages fall between 16-25? Test your code by displaying this value.

#2
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
length_of_ages = len(ages)
print("The length of ages is: ", length_of_ages)

#3
#for x in ages:
 #   print(x + 1)

#4
#working_ages = [age for age in ages if 16 <= age <= 65]
#for y in working_ages:
 #   print(y)

#5
teen_adult = [age for age in ages if 16 <= age <=25]
length_of_teen_adults = len(teen_adult)
print(length_of_teen_adults)

#6
ages.sort()
print(ages)