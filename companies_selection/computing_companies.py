#!/usr/bin/python3
"""Module to create function computing"""
import companies
#from companies import Company



team_members = int(input("How many team members do you have?"))
members_results_dict = {}

for instances in range(team_members):
    #we don't know how many members will be in the team so
    #that's why I suggested a loop here, at the end we should have the results of the
    #team members accordin to the number
    member_name = input(f"What is team member #{instances} name?")
    members_results_dict[member_name] = companies.Company(member_name)


#after above loop we should compute the results and give an ordered list of the companies names we should apply for
x = 4
for a in members_results_dict:
    members_results_dict[a] = int(x)
    x += 1
    print(members_results_dict[a])

print(members_results_dict)
