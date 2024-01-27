from src.helpers.Calculator import Calculator


def test_npi1():
  s = "5.5 + 3*(10 + 30 - 13.7) "
  total = Calculator(s).npi()

  assert total == 84.4

# def test_npi2():
#   s = "10 - (10 * 5 / 2)"
#   total = Calculator(s).npi()

#   assert total == -15

# def test_npi3():
#   s = "62 - (10 * 5 + 2)"
#   total = Calculator(s).npi()

#   assert total == 10