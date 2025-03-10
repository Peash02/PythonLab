email_set = set()
def add_email(email):
    if email in email_set:
        print("Email Already Exists.")
    else:
        email_set.add(email)
        print("Email Succssfully Registered.")

if __name__ == "__main__":
    n = int(input("Enter Number of people to be registered:"))
    for i in range(n):
        email = input("Enter Your Email Address:")
        add_email(email)
    
