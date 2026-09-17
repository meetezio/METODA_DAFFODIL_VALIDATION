
try:
    price = float (input("What is the price? "))
    print(f"The price is: {price}")
    if price > 0:
        print ("Price is VALID!")
    else: 
        print ("Price is INVALID")

except ValueError:
    print("Invalid Input! Please enter a valid decimal number! ")




#allowed = ["Spring", "Summer", "Autumn" "Winter"]
#fs = input (f"What's your favourite season? ")
#if fs in allowed:
   # print (f"Your favourite season is {fs}")
#else:
    #print ("Invalid Season! ")