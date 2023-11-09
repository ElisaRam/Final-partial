https://replit.com/join/tosrfpxnwd-elisaramirez4

print("This code helps you to know if you're healthy depending on your weight and height (only for women)")

print("What is your weight in kilograms?")
weight = int(input())

print("What is your height in centimeters?")
height = int(input())

if weight >= 45 and height < 160:
  classification = " You are Underweight"
elif 45 <= weight < 60 and 160 <= height < 170:
  classification = "You are in your perfect weight"
elif 60 <= weight < 70 and 160 <= height < 170:
  classification = "You are overweight"
else:
  classification = "You are obese"

print("Classification:", classification)
