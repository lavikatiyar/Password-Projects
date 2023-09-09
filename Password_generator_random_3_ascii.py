import secrets
import string


def create_password(pass_length=12):
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation

  alphabet = letters + digits + special_chars
  password = ''
  pass_strong = False

  while not pass_strong:
    password = ''
    for i in range(pass_length):
      password += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in password)
        and sum(char in digits for char in password) >= 2):
      pass_strong = True

  return password


if __name__ == '__main__':
  print(create_password())
