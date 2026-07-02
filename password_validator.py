def length(password):
  if len(password)>8:
    print("Valid password for length")
  else:
    print("Invalid Password because of length")
def digits(password):
  if any(ch.isdigit() for ch in password):
    print("Valid password for digits")
  else:
    print("Invalid Password because of digits")
def uppercase(password):
  if any(ch.isupper() for ch in password):
    print('Valid Password for uppercase')
  else:
    print("Invalid Password becase of uppercase")
def lowercase(password):
  if any(ch.islower() for ch in password):
    print("Valid password for lowercase")
  else:
    print("Invalid password because of lowercase ")
def special_characters(password):
 special= "@ # $ % & * ! ^ _ -"
 if any(ch in special for ch in password):
   print("Valid Password for special characters")
 else:
   print("Invalid password because of special_characters")

def main():
  password=input("Enter your password: ")
  if len(password)<8:
    length(password)
  if not password.isdigit():
    digits(password)
  if not password.isupper():
    uppercase(password)
  if not password.islower():
    lowercase(password)
  if "@ # $ % & * ! ^ _ -" not in password:
    special_characters(password)
  return 

print(main())
   

  