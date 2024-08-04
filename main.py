import random
import string
import time

def generate_key():
    prefix = "key"
    unique_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=14))
    numeric_part = str(int(time.time()))  # Using a timestamp for uniqueness
    return f"{prefix}{unique_part}.{numeric_part}"

# Generate a key
print(generate_key())