import random


class Password_Generator():
  digits = '1234567890'
  aplphabets = 'qwertyuiopasdfghjklzxcvbnm'
  symbols = '!@#$%^&*()+><?'

  digits = list(digits)
  symbols = list(symbols)
  letters = list(aplphabets)
  letters.extend(list(aplphabets.upper()))

  def __init__(self):
    letters_c = random.randint(8, 10)
    digits_c = random.randint(1, 3)
    symbols_c = random.randint(1, 2)
    self.password = self.generate_pass(letters_c, symbols_c, digits_c)

  def generate_pass(self, letters_count, symbols_count, digits_count):
    password = ""
    for _ in range(letters_count):
      password += self.letters[random.randint(0, len(self.letters) - 1)]

    for _ in range(symbols_count):
      password += self.symbols[random.randint(0, len(self.symbols) - 1)]

    for _ in range(digits_count):
      password += self.digits[random.randint(0, len(self.digits) - 1)]

    password = self.randomizePass(password)
    return password

  def randomizePass(self, password):
    randomized_pass = ""
    password_chars = list(password)
    random.shuffle(password_chars)
    for char in password_chars:
      randomized_pass += char

    return randomized_pass

  def __repr__(self):
    return f"Password: {self.password}"
