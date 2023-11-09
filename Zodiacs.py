https://replit.com/join/dhanazbvzv-elisaramirez4

print("On what day were you born?")
day = int(input())

print("On what month were you born?")
month = input()

if month == "january":
  zodiac = 'Capricorn' if day < 20 else 'Aquarius'
  print(zodiac)
elif month == "february":
  zodiac = 'Aquarius' if day < 19 else 'Pisces'
  print(zodiac)
elif month == "march":
  zodiac = 'Pisces' if day < 21 else 'Aries'
  print(zodiac)
elif month == "april":
  zodiac = 'Aries' if day < 20 else 'Taurus'
  print(zodiac)
elif month == "may":
  zodiac = 'Taurus' if day < 21 else 'Gemini'
  print(zodiac)
elif month == "june":
  zodiac = 'Gemini' if day < 21 else 'Cancer'
  print(zodiac)
elif month == "july":
  zodiac = 'Cancer' if day < 23 else 'Leo'
  print(zodiac)
elif month == "august":
  zodiac = 'Leo' if day < 23 else 'Virgo'
  print(zodiac)
elif month == "september":
  zodiac = 'Virgo' if day < 23 else 'Libra'
  print(zodiac)
elif month == "october":
  zodiac = 'Libra' if day < 23 else 'Scorpio'
  print(zodiac)
elif month == "november":
  zodiac = 'Scorpio' if day < 22 else 'Saggitarius'
  print(zodiac)
elif month == "december":
  zodiac = 'Saggitarius' if day < 22 else 'Capricorn'
  print(zodiac)
else:
  print("Invalid answers, try again.")
