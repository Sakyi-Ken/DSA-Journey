# Problem1: Simple word frequency analyzer
def word_frequency(words):
  ''' list -> dict
  This function counts the frequency of each word in a list and returns a dictionary with words as keys and their frequencies as values.
  '''
  frequency = {}
  for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
  return frequency

def frequent_word_finder(text):
  ''' str -> dict 
  This function takes a string of text, splits it into words, amd returns a dictionary with the frequency of each word.
  '''
  from collections import defaultdict
  text = text.lower()
  word_counts = defaultdict(int)
  word_list = text.split()
  for word in word_list:
    word_counts[word] += 1
  top_three = sorted(word_counts.items(), key=lambda x:x[1], reverse=True)[:3]
  return top_three

#example usage
if __name__ == "__main__":
  words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
  print(word_frequency(words))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

  text = "This is a test. This test is only a test."
  print(frequent_word_finder(text))  # Output: [('test.', 3), ('this', 2), ('is', 2)]

# Problem2: Simple word frequency analyzer with punctuation handling
def word_frequency_with_punctuation(text):
    ''' str -> dict
    This function counts the frequency of each word in a string, handling punctuation by removing it before counting.
    '''
    import string
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    return word_frequency(words)
# Example usage
if __name__ == "__main__":
    text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(word_frequency_with_punctuation(text))  # Output: {'hello': 2, 'world': 2, 'everyone': 1, 'welcome': 1, 'to': 1, 'the': 1, 'of': 1, 'python': 1}

# Problem3: Password Strength Counter
def password_strength_counter(password):
  ''' str -> dict 
  This function checks the strength of a password and returns a dictionary with the strength level and a message.
  '''
  strength = {
    'length': False,
    'digit': False,
    'lowercase': False,
    'uppercase': False
  }
  if len(password) >= 8:
    strength['length'] = True
  for char in password:
    if char.isdigit():
      strength['digit'] = True
    elif char.islower():
      strength['lowercase'] = True
    elif char.isupper():
      strength['uppercase'] = True
  if all(strength.values()):
    return {'strength': 'strong', 'message': 'Your password is strong.'}
  elif any(strength.values()):
    return {'strength': 'weak', 'message': 'Your password is weak. Consider adding more characters or symbols.'}
  else:
    return {'strength': 'very weak', 'message': 'Your password is very weak. Please choose a stronger password.'}
# Example usage
if __name__ == "__main__":
    password = "Password123"
    print(password_strength_counter(password))  # Output: {'strength': 'strong', 'message': 'Your password is strong.'}

    password = "pass"
    print(password_strength_counter(password))  # Output: {'strength': 'very weak', 'message': 'Your password is very weak. Please choose a stronger password.'}

# Problem4: Bonus Calculator
def bonus_calculator(employees):
  ''' list -> dict
  This function calculates the bonus for each employee based on their performance rating and returns a dictionary with employee
  names as keys and their bonuses as values.
  '''
  for employee in employees:
    bonus = 0
    if employee['role'] == 'developer':
      bonus = employee['salary'] * 0.1
      employee['bonus'] = bonus
  return employees
# Example usage
if __name__ == "__main__":
    employees = [
        {'name': 'Alice', 'role': 'developer', 'salary': 60000},
        {'name': 'Bob', 'role': 'manager', 'salary': 80000},
        {'name': 'Charlie', 'role': 'developer', 'salary': 70000}
    ]
    print(bonus_calculator(employees))  # Output: [{'name': 'Alice', 'role': 'developer', 'salary': 60000, 'bonus': 6000.0}, {'name': 'Bob', 'role': 'manager', 'salary': 80000, 'bonus': 0}, {'name': 'Charlie', 'role': 'developer', 'salary': 70000, 'bonus': 7000.0}]

def multi_password_strength_counter(passwords):
  special_characters = "!@#$%^&*()-+"
  strength_list = []

  for password in passwords:
    strength = {
      "length": False,
      "digit": False,
      "lower": False,
      "upper": False,
      "special_char": False
    }
    if len(password) >= 8:
      strength["length"] = True
    for passkey in password:
      if passkey.isdigit():
        strength["digit"] = True
      elif passkey.islower():
        strength["lower"] = True
      elif passkey.isupper():
        strength["upper"] = True
      elif passkey in special_characters:
        strength["special_char"] = True
    strength_list.append(strength)
  return strength_list

# Alternative for strength checking
from collections import defaultdict
def alternative_password_strength_counter(passwords):
  strength_list = []
  for password in passwords:
    strength = defaultdict(bool)
    if len(password) >= 8:
      strength['length'] = True
    for char in password:
      if char.isdigit():
        strength['digit'] = True
      elif char.islower():
        strength['lowercase'] = True
      elif char.isupper():
        strength['uppercase'] = True
      elif char in "!@#$%^&*()-+":
        strength['special_char'] = True
    strength_list.append(dict(strength))
  return strength_list
  
passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
  print(result)