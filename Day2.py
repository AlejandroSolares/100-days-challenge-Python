#Excersice instructions

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

TipOptions = [10,15,20]
TipPOptions = [1,2,3]

print("Welcome to the tip calculator \n")
bill = float(input("What was the total bill? $"))

#Validate the user input
loop = False
while loop == False:
    tip = input("How much tip would you like to give? \n 1) " + str(TipOptions[0]) + "% \n 2) " + str(TipOptions[1]) + "%  \n 3) " + str(TipOptions[2]) + "% \n")   
    try:
        int(tip)
        integer = True

        i = 0
        valid = False

        while i < len(TipPOptions):
            if int(tip) == TipPOptions[i]:
                valid = True
            i += 1
        if valid:
            tip = TipPOptions.index(int(tip))
            tip = TipOptions[int(tip)]
            loop = True
        else:
            print(tip + " is not an option, please pick one from the options")
    except ValueError:
        integer = False

people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")