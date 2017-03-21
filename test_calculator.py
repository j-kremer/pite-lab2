import unittest
import math
from calculator import calculator
from calculator import notANumber
from calculator import notAnInteger
from calculator import notAPositiveNumber
from calculator import divisionByZero
from calculator import notAFunction


class test_calculator(unittest.TestCase):
	def setUp(self):
		self._calc = calculator()

	#tests of method add
	def testNumber1PassedToMethodAddIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.add, "a", 2.4)

	def testNumber2PassedToMethodAddIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.add, 2.4, "a")

	def testAddingOfIntegersReturnsCorrectResult(self):
		self.assertEqual(8, self._calc.add(3,5))

	def testAddingOfFloatsReturnsCorrectResult(self):
		self.assertAlmostEqual(3.14, self._calc.add(0.56,2.58), places = 4)

	#tests of method divide
	def testNumber1PassedToMethodDivideIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.divide, "a", 2.4)

	def testNumber2PassedToMethodDivideIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.divide, 2.4, "a")

	def testNumber2PassedToMethodDivideIsZero(self):
		self.assertRaises(divisionByZero, self._calc.divide, 2.4, 0.)

	def testDividingOfIntegersReturnsCorrectResult(self):
		self.assertEqual(3, self._calc.divide(12,4))

	def testDividingOfFloatsReturnsCorrectResult(self):
		self.assertAlmostEqual(4., self._calc.divide(10.,2.5), places = 4)

	#tests of method logarithm
	def testNumberPassedToMethodLogarithmIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.logarithm, "a")

	def testNumberPassedToMethodLogarithmIsNotPositive(self):
		self.assertRaises(notAPositiveNumber, self._calc.logarithm, -2.4)

	def testLogartihmOfIntegerReturnsCorrectResult(self):
		self.assertAlmostEqual(2.302585093, self._calc.logarithm(10), places = 4)

	def testLogartihmOfFloatReturnsCorrectResult(self):
		self.assertAlmostEqual(1., self._calc.logarithm(math.e), places = 4)

	#tests of method derivative
	def testFuncPassedToMethodDerivativeIsNotAFunction(self):
		self.assertRaises(notAFunction, self._calc.derivative, "a", 1.)

	def testPointPassedToMethodDerivativeIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.derivative, math.exp, "a")

	def testOrderPassedToMethodDerivativeIsNotInt(self):
		self.assertRaises(notAnInteger, self._calc.derivative, math.exp, 0., 2.4)

	def testOrderPassedToMethodDerivativeIsNotPositive(self):
		self.assertRaises(notAPositiveNumber, self._calc.derivative, math.exp, 0., -2)


if __name__ == '__main__':
	unittest.main()
