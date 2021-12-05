from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("Now user, enter the bills period? E.g. December 2020: ")

name1 = input("What is your name? ")
flatmate2_dih = int(input(f"User, enter the amount of days {name1} was in the house: "))

name2 = input("What is the name of your flatmate? ")
flatmate1_dih = int(input(f"User, enter the amount of days {name2} was in the house: "))

print("This is a: ", amount)

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house=flatmate1_dih)
flatmate2 = Flatmate(name2, days_in_house=flatmate2_dih)

print(flatmate1.pays(the_bill, flatmate2=flatmate1))
print(flatmate2.pays(the_bill, flatmate2=flatmate2))

pdf_report = PdfReport(filename=f"{the_bill.period}_of_{name1}_and_{name2}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
