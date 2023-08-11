print("Pizza Villa ! Welcomes you to the Pizza Order Portal")
print("MENU LIST:-\n1-Cheese Pizza\n2-Spicy Pizza\n3-Onion Pizza\n4-Corn Pizza\n5-Chicken Pizza\n6-Crusty Pizza\n7-Combo Pizza")
bill = 0
select_type = input("Please select pizza from menu list and type the corresponding number here or pizza name here : ").upper()
confirm_selection = input(f"You have chosen {select_type}. Type 'Y' to confirm. 'N' to change your selection.").upper()
if confirm_selection == "Y" and select_type == "CHEESE PIZZA" or select_type == "1":
    bill+=60
elif confirm_selection == "Y" and select_type == "SPICY PIZZA" or select_type == "2":
    bill+=70
elif confirm_selection == "Y" and select_type == "ONION PIZZA" or select_type == "3":
    bill += 50
elif confirm_selection == "Y" and select_type == "CORN PIZZA" or select_type == "4":
    bill += 80
elif confirm_selection == "Y" and select_type == "CHICKEN PIZZA" or select_type == "5":
    bill += 170
elif confirm_selection == "Y" and select_type == "CRUSTY PIZZA" or select_type == "6":
    bill += 110
elif confirm_selection == "Y" and select_type == "COMBO PIZZA" or select_type == "7":
    bill += 150

select_size = input("Type L for Large, M for Medium, S for Small and EL for Extra Large")
if select_size == "EL":
    bill += 100
elif select_size == "L":
    bill += 80
elif select_size == "M":
    bill += 60
elif select_size == "S":
    bill += 50
add_on_ask = input("Do you want add-ons on your Pizza? Press 'Y' or 'N' ").upper()
if add_on_ask == "Y":
    select_adds = input("1-Extra Cheese-20\n2-Extra Chilly Flakes-10\n3-Extra Dip-10\n4-Cold Drink Can-40\n5-Extra Ketchup-05\n").upper()
    if select_adds == "1" or select_adds == "EXTRA CHEESE":
        bill+=20

    elif select_adds == "2" or select_adds == "EXTRA CHILLY FLAKES":
        bill+=10
    elif select_adds == "3" or select_adds == "EXTRA DIP":
        bill += 10
    elif select_adds == "4" or select_adds == "COLD DRINK":
        bill += 40
    elif select_adds == "5" or select_adds == "EXTRA KETCHUP":
        bill += 5

    print(f"Your selected Pizza {select_type} is ready with your add on {select_adds}. Please pay {bill}")
elif add_on_ask=="N":
    print(f"Thank You for ordering ! Your final bill is {bill}")



