# Exercise 3

Personal_info = {}
Personal_info ["first_name"] = input("Enter your first_name: ")
Personal_info ["second_name"] = input("Enter your second_name: ")
Personal_info ["hometown"] = input("Enter your hometown: ")

print(Personal_info)

while True:
      age_info = input("Enter your age: ")

      try:
        Personal_info["age"] = int(age_info)
        break
      
      except ValueError:
        print("Sorry!" " Enter a number please")
        
print(f"First Name: {Personal_info["first_name"]}\vSecond Name: {Personal_info["second_name"]}\vHometown: {Personal_info["hometown"]}\v{Personal_info:}")
        


 









