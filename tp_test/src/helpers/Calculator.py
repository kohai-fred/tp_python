import re

class Calculator:

  def __init__(self, sentence):
    self.sentence = sentence

  def add(self):
    arr = self.sentence.split("+")
    total = sum([float(x) for x in arr])
    return total

  def calculSwitchCase(self, num1, num2, operator):
    if operator == "+":
      return num1 + num2
    elif operator == "-":
      return num1 - num2
    elif operator == "*":
      return num1 * num2
    elif operator == "/":
      return num1 / num2
    else : False


  # Cette fonction rempli la condition de test.
  # Mais elle ne rempli pas la condition de NPI
  def npi(self):
    digitStack = re.findall(r'\d+\.\d+|\d+',self.sentence)
    operatorsStack = re.findall(r'[+\-*/]',self.sentence)
    total = 0
    while len(digitStack)>1:
      # print(digitStack, "op ==> ", operatorsStack, "total = ", total)
      digits = digitStack[-2:]
      operator = operatorsStack.pop()
      del digitStack[-2:]
      total = self.calculSwitchCase(float(digits[0]), float(digits[1]),operator)
      digitStack.append(total)

    return total

#s = "5.5 + 3*(10 + 30 - 13.7) === 84.4"