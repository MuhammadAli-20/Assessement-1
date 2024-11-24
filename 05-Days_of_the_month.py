# Take keys as month numbers and values as the number of days.
Days = {1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31}
# Asking the user to enter the month number.
user_input = int(input("Enter the month number: "))
if 1 <= user_input <= 12:
# Checking for leap year
   if user_input == 2:
    leap = input("Searching for leap year: ")

    if leap == "yes":
     print("The month has 29 days.")
    else:
     print("The month has 28 days.")
     
# Adjusting the number of days.
   else:
    print(f"The entered month has {Days[user_input]} days.")










        





 
        
    

              
