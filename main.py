import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a Pdf file that contains data about the
    flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay: str = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay: str = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit="pt", format="A4")
        pdf.add_page()

        # Add Icon
        pdf.image(name="./files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=160, h=40, txt=bill.period, border=0)
        pdf.cell(w=100, h=40, txt="Total bill:")
        pdf.cell(w=100, h=40, txt=str(bill.amount), ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=160, h=20, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=160, h=20, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open_new(self.filename)

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
