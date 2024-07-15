import random
import string

# Loop 7 times to generate 7 email addresses
random_char = random.choice(string.ascii_letters)
rands = random.choice(string.hexdigits)
email = "piyush" + random_char+rands
print(email)
