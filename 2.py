import re
pattern_name = "/^[a-z][^\W_]{7,14}$/i"
username = input("Username: ")
pattern = "/^(?=[^a-z]*[a-z])(?=\D*\d)[^:&.~\s]{5,20}$/g"
password = input("Password: ")
result = re.findall(pattern, password)
if (result):
    print("Valid password")
else:
    print("Password not valid")
