https://replit.com/join/tlyxrkoegv-elisaramirez4

counter = 0
total_savings = 0
amount_saved = int(input("What is the amount saved"))
number_withdrawals = int(input("What is the number of withdrawals you'd like to do? (Max 3)"))
while counter < number_withdrawals:
  counter += 1
  print(counter)
  savings = float(input("Enter the expense for each:"))
  total_savings += savings
  if total_savings > amount_saved:
    print("You have exceeded")
    break
  elif total_savings == amount_saved:
    print("You have withdrawn all your money")
    break
  balance = amount_saved - total_savings

print("The sum of all the withdrawals is:", total_savings)
print("The balance is:", balance)

counter = 0
total_expenses = 0
amount_expenses = int(input("What is the amount of expenses you've made?"))
while counter < amount_expenses:
  counter += 1
  print(counter)
  expenses = float(input("Enter the expense for each:"))
  total_expenses += expenses

print(total_expenses)

counter = 0
total_emissions = 0
number_activities = int(input("How many activities have you made?"))
while counter < number_activities:
  counter += 1
  print(counter)
  emissions = float(input("Enter the emissions for the activity:"))
  total_emissions += emissions

print(total_emissions)
