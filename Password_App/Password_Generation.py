import random
import string

def generate_password():
  """Generates a strong password."""
  charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
  length = 12
  password = ""
  for i in range(length):
    password += random.choice(charset)
  return password

def save_password(password, filename):
  """Saves the password to a text file."""
  with open(filename, "a") as f:
    f.write(password + "\n")

if __name__ == "__main__":
  password = generate_password()
  filename = "passwords.txt"
  save_password(password, filename)
