''' Exercício referente ao vídeo 04 
 André de Oliveira Águila Favoto - 11811EAU013''' 


#Manipulating strings
courses = ['History', 'Math', 'Physics', 'CompSci']

#Reading
""" print(courses)
print(courses[2])
print(courses[-1]) """
#Slicing
""" print(courses[0:2])
print(courses[:2])
print(courses[2:]) """

#Adding items
""" 
courses.append('Art')
print(courses)

courses.insert(0,'Engineering')
print(courses)

courses_2 = ['Design', 'Philosophy']
courses.extend(courses_2)
print(courses) """

#Removing items
""" removed_item = courses.pop()
print(removed_item)
 """
#reversing and sorting
""" courses.reverse()
print(courses)

nums = [1, 7, 3, 5, 8]
nums.sort()
print(nums)

nums.sort(reverse = True)
print(nums)

sorted_courses = sorted(courses) #not changing the original one
print(sorted_courses)
print(courses)
 """
#min max sum
""" print(min(nums))
print(max(nums))
print(sum(nums))
 """

#Locating items
""" print(courses.index('CompSci'))

for index, course in enumerate(courses):
    print(index, course) """

#Joining and splitting
""" courses_str = ', '.join(courses)
print(courses_str)
courses_list  = courses_str.split(', ')
print(courses_list) """

#Tuples and sets
    #declaring
tuple_1 = ('History', 'Math', 'Physics', 'CompSci') #unmutable
list_1 = ['History', 'Math', 'Physics', 'CompSci'] #mutable
set_1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'} #don't accept dupplicates, has no specific order
set_2 = {'Design', 'Math', 'Art', 'CompSci', 'Math'} #don't accept dupplicates, has no specific order

print(set_1)
print('Math' in set_1)
print(set_1.intersection(set_2)) #returns common items
print(set_1.difference(set_2)) #returns different items
print(set_1.union(set_2)) #returns the union of the sets