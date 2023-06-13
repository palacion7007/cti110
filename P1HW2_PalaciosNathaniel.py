#Program that calculates travel expenses
#6/13/2023
#CTI-110 P1HW2 - Travel Expense
#Nathaniel Palacios

print('This program calculates and displays travel expenses')
print()
budget = int(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = int(input('How much do you think you will spend on gas? '))
print()
hotel = int(input('Approximately, how much will you need for accomodation: '))
print()
food = int(input('Last, how much do you need for food? '))
print()
print('-'*12,'Travel Expenses','-'*12)
print('Location:', destination)
print('Initial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodaiton:', hotel)
print('Food:', food)
print()
print('Remaining Balance:', budget-(gas+hotel+food))
