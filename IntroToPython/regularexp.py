import re
email = input("Whats your email? ").strip()

if re.search("@",email):
    print("Valid")
else:
    print("In Valid") 