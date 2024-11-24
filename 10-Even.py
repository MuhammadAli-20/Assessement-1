# Exercise 10

# To check whether the number is Even or Odd
def Even_Odd(num):
    return f'The entered number {num} is even.' if num%2 == 0 else f'The entered number {num} is odd.'

def main():
    user_number = int(input("Enter a number: ")) 
    print(Even_Odd(user_number))
    
if __name__=="__main__":
 main()
     





    
        
    

     