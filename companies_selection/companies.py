#!/usr/bin/python3
"""Module to create companies_selection class"""
import sys
from colors import *


class Company():
    """class companies to create instance of voting
    per each team member"""

    def __init__(self, member_name):
        """Instances attributes that will determine the result of each company according to the
        member in case"""
        self.comp_list = {"Immigo": None, "Bomberbot": None, "Valienta": None,
                     "Microsoft": None, "Mowies": None, "Torre_crawling": None,
                     "Atomchat": None, "Techstars": None, "Bankity": None,
                     "Code_inspector": None, "Torre_talent": None,
                     "Porter_Metrics": None,"Social_atom": None}
        self.member = member_name
        for a, b in self.comp_list.items():
            result = self.input_voting(a, self.member)
            self.comp_list[a] = result
            self.a = a
            print("Result for", self.a + ":", end="")
            sys.stdout.write(BLUE)
            print(f" {self.comp_list[a]}")
            sys.stdout.write(RESET)
        # Here it should return a list of the results in order but the idea is to return
        # the list of the names not just the number of the results
        print("--------------------")

    def input_voting(self, company, member_name):
        """Function used when instance is created to receive voting inputs per company per team member"""
        res = 0
        print(f"Member: ", end="")
        sys.stdout.write(RED)
        print(f"{member_name} ", end="")
        sys.stdout.write(RESET)
        print(f"Company: ", end="")
        sys.stdout.write(GREEN)
        print(f"{company}")
        sys.stdout.write(RESET)
        feat_list = {"culture": 0, "tech_stack": 0,
                     "product": 0, "industry": 0}

        for a, b in feat_list.items():
            try:
                feat_list[a] = int(input(f"From 1-5 how is the {a} for you? -> "))
            except ValueError:
                feat_list[a] = 0

            res += feat_list[a]
        return res / 4



#Adrian = Company("Adrian")
#print(Adrian.comp_list)
#Gonzales = Company("Gonzales")
#Campo = Company("Campo")
