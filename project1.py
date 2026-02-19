# Fundamental Booster Project 
# interactive Personal Data Collector

# Step1 : Welcome Message
print("welcome to the interactive Personal data Collector !")
print("This program will collect and Process your personal information")

#Step2: Collect User Information
My_name = input("enter your name :")
my_age = int(input("enter your age :"))
My_height = float(input("enter your height in meter :"))
fav_Num = int(input("enter your favourite number:"))

# Thank you ! here is the information we collected :

#Step3: Data Processing
currrent_Year = 2026
age_year = int(input("age year :")) 
Birth_Year = currrent_Year - age_year
print(Birth_Year)

print("\n--- Data Summary ---")
print(f"Name: {My_name}  | Type: {type(My_name)} | Memory address: {id(My_name)}")
print(f"Age: {my_age} | Type: {type(my_age)} | Memory address: {id(my_age)}") 
print(f"height: {My_height} | Type: {type(My_height)} | Memory address: {id(My_height)}")
print(f"favourite_number : {fav_Num} |Type: {type(My_name)} | Memory address: {id(My_name)}")
print(f"Estimated birth year: {Birth_Year}")