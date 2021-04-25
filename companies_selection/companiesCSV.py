#!/usr/bin/python3
""" Module to create a file rating_companies.csv """
import csv
from  os import path

my_input = int(input("Select 1 - Add your Rating of all companies\n"
                     "Select 2 - See the Average of rating all companies: "))

my_companies = ["Bankity", "Bomberbot", "Valienta", "Torre Crawling", "Immigo",
                "Mowies", "Atomchat", "Techstars", "Torre Talent" , "Code_inspector",
                "Microsft", "Sorter Metrics", "Socialatom"]

def save_to_file_csv(my_companies):
    """ Function to create the rating of the company with your name and your
    rating """

    filename = "rating_companies.csv"
    my_dict = []
    my_list = []
    rating_dict= {}

    my_attr = ["Name", "Company", "Culture", "Tech Stack", "Product", "Industry", "Average"]
    print()
    rating_dict["Name"] = input("Enter Your Name: ")

    for company in my_companies:
        print("The company is {}".format(company))

        rating_dict["Company"] = company
        my_sum = 0

        print()

        for column in my_attr[2:-1]:
            rating_dict[column] = int(input(f"{column} = vote from 1-5 how is {company} for you? "))
            my_sum = my_sum + rating_dict[column]

        rating_dict["Average"] = float(my_sum / 4)
        my_dict.append(rating_dict.copy())
        my_list.append([rating_dict["Name"], rating_dict["Company"], rating_dict["Culture"],
                       rating_dict["Tech Stack"], rating_dict["Product"],
                       rating_dict["Industry"], rating_dict["Average"]])
        print()

    if (path.isfile(filename)):
        with open(filename, 'a', newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(my_list)
    else:
        with open(filename, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=my_attr)
            writer.writeheader()
            writer.writerows(my_dict)

def Average(my_companies):
    """Funcion that deserializes and read a file csv """
    results = []
    my_dict = {}
    temp_name = ""
    count = 0
    filename = "rating_companies.csv"
    print()
    try:
        with open(filename, "r") as File:
            reader = csv.DictReader(File)

            for row in reader:
                company = row["Company"]

                if temp_name == "" or temp_name != row["Name"]:
                    temp_name =  row["Name"]
                    count = count + 1
                    print()

                print(f"Name = {row['Name']}, Company = {row['Company']}, Average = {row['Average']}")

                if company in my_dict:
                    my_dict[company] = my_dict.get(company, 0 ) + float(row['Average'])

                else:
                    my_dict[company] = float(row['Average'])

        print()

        for company, Average in my_dict.items():
            print(f"This is the Average between {count} integrants")
            print(f"{company} == {round(Average/count, 2)}")

    except FileNotFoundError:
        print("The file is not created in this directory")


if my_input == 1:
    save_to_file_csv(my_companies)

if my_input == 2:
    Average(my_companies)
