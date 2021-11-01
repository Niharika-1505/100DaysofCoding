# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedString= name1+name2
combinedString=combinedString.upper()
T=combinedString.count("T")
R=combinedString.count("R")
U=combinedString.count("U")
E=combinedString.count("E")
L=combinedString.count("L")
O=combinedString.count("O")
V=combinedString.count("V")
E=combinedString.count("E")
print("Your score is "+str(T+R+U+E)+str(L+O+V+E)+", you are alright together.")