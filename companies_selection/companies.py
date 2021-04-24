#!/usr/bin/python3
"""Module to create companies_selection class"""


class companies():
    """class companies to create instance of voting
    per each team member"""

    def __init__(self, member_name):
        """Instances attributes that will determine the result of each company according to the
        member in case"""
        result_list = []
        result_list.append(self.bankity = input_voting("Bankity", member_name))
        result_list.append(self.bomberbot = input_voting("Bomberbot", member_name))
        result_list.append(self.valienta = input_voting("Valienta", member_name))
        result_list.append(self.torre_crawling = input_voting("Torre_crawling", member_name))
        result_list.append(self.immigo = input_voting("immigo", member_name))
        result_list.append(self.mowies = input_voting("mowies", member_name))
        result_list.append(self.atomchat = input_voting("atomchat", member_name))
        result_list.append(self.techstars = input_voting("techstars", member_name))
        result_list.append(self.torre_talent = input_voting("torre_talent", member_name))
        result_list.append(self.code_inspector = input_voting("code_inspector", member_name))
        result_list.append(self.microsoft = input_voting("microsoft", member_name))
        result_list.append(self.sorter_metrics = input_voting("sorter_metrics", member_name))
        result_list.append(self.socialatom = input_voting("socialatom", member_name))
        result_list.sort()

        # Here it should return a list of the results in order but the idea is to return
        # the list of the names not just the number of the results
        return

    def input_voting(company, member_name):
        """Function used when instance is created to receive voting inputs per company per team member"""
        culture = int(input(f"**{member_name} vote**\nFrom 1-5 how is {company} culture for you?:"))
        tech_stack = int(input(f"**{member_name} vote**\nFrom 1-5 how is {company} tech_stack for you?:"))
        product = int(input(f"**{member_name} vote**\nFrom 1-5 how is {company} product for you?:"))
        industry = int(input(f"**{member_name} vote**\nFrom 1-5 how is {company} industry for you?:"))

        result = (culture + tech_stack + product + industry) / 4
        return result