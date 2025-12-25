import re
# name = input("What is your name? ")
# matches = re.search(r"^(.+),(.+)$", name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"hello, {name}")


# name = input("What is your name? ")
# matches = re.search(r"^(.+),(.+)$", name)
# if matches: 
#     name = matches.group(2)+" "+matches.group(1)
# print(f"hello, {name}")


# name = input("What is your name? ")
# if matches := re.search(r"^(.+),(.+)$", name): #volrus operator
#     name = matches.group(2)+" "+matches.group(1)
# print(f"hello, {name}")

url = input("URL: ").strip()
print(url)
# username = url.replace("https://twitter.com/","")
username = re.sub("^https://twitter.com/","",url)
print(f"Username: {username}")