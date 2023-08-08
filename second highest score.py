# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:27:08 2022

@author: HP
"""

"""
#concept used:nested list @Hackerank
student_marks=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    student_marks.append([name,score])
sorted_marks=sorted(list(set([x[1] for x in student_marks])))

second_lowest=sorted_marks[1]
low_final_list=[]
for student in student_marks:
    if second_lowest==student[1]:
        low_final_list.append(student[0])
for student in sorted(low_final_list):
    print(student)
        
"""

print(“abcabcab”.split(‘c’))