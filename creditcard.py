#  VISA TEST CASES CARDS FROM PAYPAL =>

# 4111111111111111
# 4012888888881881
# 4999991111111113
# 4999992222222229
# 4003600000000014 ~ David Visa Card (Harvard CS50x)

def creditCardName(creditCardNumber):
    if creditCardNumber[0] == "4":
        return "Visa Card: Valid!"
    elif creditCardNumber[0] == "5":
        return "MasterCard: Valid!"
    else:
        return ("Unknown card type!")
 
creditCardNumber = input("Please enter a 16 digit card number: ")

if " " in creditCardNumber:
    print("There's a unknown character in digits")
    
elif not creditCardNumber.isdigit():
    print("The credit card number must be a digit!")
    
elif len(creditCardNumber) != 16:
    print("The credit card number must be 16 digits!")
        
        
else:
    total = 0
        # Iterating over every other digit, starting from the second-to-last digit
    for i in range(-2, -(len(creditCardNumber)+1), -2):
                # Mutiplying by 2
        multipliedDigits = int(creditCardNumber[i]) * 2
                # Converting int to str so I can iterate
        strMultipliedDigits = str(multipliedDigits)
        tempTotal = 0
        for char in strMultipliedDigits:
            tempTotal += int(char)
                # Now lastly add into total
        total += tempTotal
        
        for i in range(-1, -(len(creditCardNumber)+1), -2):
            total += int(creditCardNumber[i])
    
            # Checking if the total modulo 10 is congruent to 0, if true -> Valid, else Invalid.
    if total % 10 == 0:
        print(creditCardName(creditCardNumber))
    else:
        print(creditCardName(creditCardNumber))




          
