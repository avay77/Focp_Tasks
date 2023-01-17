import random

def generate_password():
    first_name=["Bruno","Cristiano","Lionel","Zinedine","Sergio","David","Roy","Marcus","Anthony","Kylian","Erling"]
    second_name=["Fernandes","Ronaldo","Messi","Zidane","Ramos","Beckham","Keane","Rashford","Martial","Mbappe","Haaland"]
    jersey_num=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven"]
    
    a=random.choice(first_name)
    b=random.choice(second_name)
    c=random.choice(jersey_num)
    password= a+b+c
    return password

print("Password Generator")
print("==================")
try:
    num_of_password=int(input("\nHow many passwords are needed?:"))

    if num_of_password>0 and num_of_password<25:

        for i in range(num_of_password):
            password = generate_password()
            print(i+1," --> ",password)
    else:
        print("Please enter a value between 1 and 24.")
except ValueError:
    print("Please enter a number.")
    
