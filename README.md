# TDD Task
- create a new git hub repo and project in pycharm
  - DONE
- create tests for functions cm to inches, modular, Triangle calculation and calculate %.

- write the code to pass all the tests
- create 2 files 1 for tests and 1 for functional code
- apply OOP to achieve the desired results.

#### First iteration
- initial files
#### Second iteration  
- potential testing methods
```python
import pytest
import unittest

from TDD_Calc_Functions import Function_Calc

class Calc_Test(unittest.TestCase):  # helps us test

    calc_test = Function_Calc()

    def test_inches(self):
        # this naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter can recognise it so it can run
        self.assertEqual(self.calc_test.inches(10), 25.4)  # 10 * 2.54 = 25.4

    def test_modular(self):
        self.assertEqual(self.calc_test.modular(4, 2), 0)  # 4 % 2 = 0 | no remainder

    def test_triangle(self):
        self.assertEqual(self.calc_test.triangle(10, 10), 50)  # (height * base) / 2 = 50

    def test_percentage(self):
        self.assertEqual(self.calc_test.percentage(10, 50), 20)  # (10 / 50) * 100 = 20%
```
#### Third iteration
- Added functional code
- Returns 1 error, 3 passed
```python
class Function_Calc:

    def modular(self, value_1, value_2):  # divisible function
        if value_2 == 0:
            return False
        elif value_1 % value_2 == 0:  # if the value_1 can be divided by the value_2 with no remainder, then return True
            return True
        else:
            return False

    def triangle(self, height, base):  # area of a triangle function
        return (height * base) / 2

    def percentage(self, value_1, value_2):  # area of a triangle function
        return (value_1 / value_2) * 100

    def inches(self, value_1):
        return value_1 * 2.54  # multiplies the value by the length of an inch in centimeters

```

#### Fourth iteration
- had 0 instead of True on the modular function
- Four tests passed
```python
import pytest
import unittest

from TDD_Calc_Functions import Function_Calc

class Calc_Test(unittest.TestCase):  # helps us test

    calc_test = Function_Calc()

    def test_inches(self):
        # this naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter can recognise it so it can run
        self.assertEqual(self.calc_test.inches(10), 25.4)  # 10 * 2.54 = 25.4

    def test_modular(self):
        self.assertEqual(self.calc_test.modular(4, 2), True)  # 4 % 2 = 0 | no remainder

    def test_triangle(self):
        self.assertEqual(self.calc_test.triangle(10, 10), 50)  # (height * base) / 2 = 50

    def test_percentage(self):
        self.assertEqual(self.calc_test.percentage(10, 50), 20)  # (10 / 50) * 100 = 20%
```
## Notes
- at least two .py files, test.py and functional.py
  - test.py is for the test functions
  - functional.py is for the actual code
- test functions must start with 'test'
- assertEqual is a function from pytest(like .upper())
- must set the object to the class from the functional.py file
- the values in the test functions are (parameter1, parameter2, answer)
  - example: (10, 50), 60) = 10 + 50 = 60
  - can include hidden parameters
    - example for percentage: (10, 50), 20) = (10 / 50) * 100 = 20