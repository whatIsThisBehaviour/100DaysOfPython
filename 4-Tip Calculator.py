print("Expense Calculator : Calculate per head expenses quickly !")
bill = int(input("Enter the bill amount : "))
number_of_people = int(input("Enter number of people dividing the bill : "))
percentage_tip = int(input("Enter the percentage of tip you want to give : "))
bill_with_tip_added = round(bill + bill * (percentage_tip/100), 2)
print(f"Total Bill with tip is {bill_with_tip_added}.")
each_person_pays = round(bill_with_tip_added/number_of_people, 2)
print(f"Each person pays {each_person_pays}")