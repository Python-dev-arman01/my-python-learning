#------------------Day 1 practis code
def symballs():
    symball = input("Enter a symball : ")
    for i in range(10, 0, -1):
        print(symball * i)

# without symball call function
symballs()


#----------------------------------------------------
#----------Day2 practise code---------
#----Dat2 --function whith calculator code-------
def jarvish ():
	num1=int(input("Enter a num :"))
	num2=int(input("Enter a nym :"))
	print(num1+num2)
	print(num1- num2)
	print(num2- num1)
	print(num1* num2)
	print(num1/num2)
	print(num2/num1)
	
jarvish()

#----------------------------------------
#------Day 3 practise code---------------
#---Day 3 function in loos & conditional statement and methods in calculator-----
def jarvish():
    print("\n⚡ Jarvis System Ready ⚡")
    
    # Error Handling: कोड क्रैश होने से बचाने के लिए
    try:
        num1 = int(input("Enter first num: "))
        num2 = int(input("Enter second num: "))
        
        # सारे कैलकुलेशन एक साथ
        print(f"➕ Addition:       {num1 + num2}")
        print(f"➖ Subtraction 1:  {num1 - num2}")
        print(f"➖ Subtraction 2:  {num2 - num1}")
        print(f"✖️ Multiplication: {num1 * num2}")
        print(f"POVER == {num1**num2}")
        # Zero से भाग (Divide) होने से बचाना
        if num2 != 0:
            print(f"➗ Division 1:     {num1 / num2}")
        else:
            num2 +=1
            print(f"Division1 : {num1/num2}")
        print("Division1 sucsessfull")
            
        if num1 != 0:
            print(f"➗ Division 2:     {num2 / num1}")
        else:
            num1 +=1
            print(f"Division2 : {num2/num1}")
        print("Division2 sucsessfull")
            
    except ValueError:
        print("❌ Error: pleaseEnter only numbers! :")

# MAIN LOOP: जो प्रोग्राम को लगातार चलाएगा
while True:
    jarvish()
    
    # यूजर से पूछना कि आगे चलाना है या बंद करना है
    choice = input("\nक्या आप फिर से चलाना चाहते हैं? (yes/no): ").lower()
    if choice == 'no':
        print("👋 Goodbye! Jarvis shutting down.")
        break  # लूप को तुरंत रोक देगा


