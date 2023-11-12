https://replit.com/join/gsqaseylzn-elisaramirez4

counter = 0
number_wands = 0
elder= 0
hawthorn=0
willow=0
holly=0 
sales=0
notsold=0
client = input("Did a client come in? (yes/no): ")

while client == "yes":
  counter+= 1
  wand= input("Did they buy a wand? (yes/no)")
  if wand == "yes":
    sales+= 1
    print("1. Elder wand")
    print("2. Hawthorn wand")
    print("3. Willow wand")
    print("4. Holly wand")

    type_of_wand = int(input("What type?"))
    if type_of_wand == 1:
      elder += 1
    elif type_of_wand == 2:
      hawthorn += 1
    elif type_of_wand == 3:
      willow += 1
    elif type_of_wand == 4:
      holly += 1
  elif wand == "no":
      notsold+=1 

  client=(input("Is there another client? (yes/no)"))

print("Today", counter, "clients came in")
print("of them ", sales, " bought a wand, and,", notsold, "didn´t")
print(elder, "elder wands were sold")
print(hawthorn, "happy wands were sold")
print(willow, "dragon wands were sold")
print(holly, "super wands were sold")
print("What a great day for Olivanders!")
