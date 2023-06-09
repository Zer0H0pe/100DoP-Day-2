#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("How much was the total? "))
tip = float(input("What percentage would you like to tip? "))
party = int(input("What is the party size? "))

tipped = tip / 100 * bill + bill
final = tipped / party
split = round(final, 2)
split = "{:.2f}".format(split)

print(f"Each person should pay: ${split}.")
