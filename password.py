password="your sample password"
inp=""
while inp!=password:
    inp=input("Enter the password : ")
    if inp!=password:
        print("Invalid password. Try Again!")
print("Login Successfull!")