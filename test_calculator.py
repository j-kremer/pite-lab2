import unittest
import mock
import math
from calculator import calculator
from calculator import notANumber
from calculator import notAnInteger
from calculator import notAPositiveNumber
from calculator import dividingByZero
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
		input1 = 3
		input2 = 5
		expected_output = 8
		self.assertEqual(expected_output, self._calc.add(input1, input2))

	def testAddingOfFloatsReturnsCorrectResult(self):
		input1 = 0.56
		input2 = 2.58
		expected_output = 3.14
		self.assertAlmostEqual(expected_output, self._calc.add(input1, input2), places = 4)

	#tests of method divide
	def testNumber1PassedToMethodDivideIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.divide, "a", 2.4)

	def testNumber2PassedToMethodDivideIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.divide, 2.4, "a")

	def testNumber2PassedToMethodDivideIsZero(self):
		self.assertRaises(dividingByZero, self._calc.divide, 2.4, 0.)

	def testDividingOfIntegersReturnsCorrectResult(self):
		input1 = 12
		input2 = 4
		expected_output = 3
		self.assertEqual(expected_output, self._calc.divide(input1, input2))

	def testDividingOfFloatsReturnsCorrectResult(self):
		input1 = 10.
		input2 = 2.5
		expected_output = 4.
		self.assertAlmostEqual(expected_output, self._calc.divide(input1, input2), places = 4)

	#tests of method logarithm
	def testNumberPassedToMethodLogarithmIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.logarithm, "a")

	def testNumberPassedToMethodLogarithmIsNotPositive(self):
		self.assertRaises(notAPositiveNumber, self._calc.logarithm, -2.4)

	def testLogartihmOfIntegerReturnsCorrectResult(self):
		input = 10
		expected_output = 2.302585093
		self.assertAlmostEqual(expected_output, self._calc.logarithm(input), places = 4)

	def testLogartihmOfFloatReturnsCorrectResult(self):
		input = math.e
		expected_output = 1.
		self.assertAlmostEqual(expected_output, self._calc.logarithm(input), places = 4)

	#tests of method derivative
	def testFuncPassedToMethodDerivativeIsNotAFunction(self):
		self.assertRaises(notAFunction, self._calc.derivative, "a", 1.)

	def testPointPassedToMethodDerivativeIsNotANumber(self):
		self.assertRaises(notANumber, self._calc.derivative, math.exp, "a")

	def testOrderPassedToMethodDerivativeIsNotInt(self):
		self.assertRaises(notAnInteger, self._calc.derivative, math.exp, 0., 2.4)

	def testOrderPassedToMethodDerivativeIsNotPositive(self):
		self.assertRaises(notAPositiveNumber, self._calc.derivative, math.exp, 0., -2)

	def testDerivativeReturnsCorrectResultWithDefaultOrder(self):
		inputFunc = math.exp
		inputPoint = 0.
		expected_output = 1.
		self.assertAlmostEqual(1., self._calc.derivative(inputFunc, inputPoint), places = 4)

	@mock.patch('calculator.calculator.derivative')
	def testDerivativeReturnsCorrectResultWithHigherOrder(self, mock_derivative):
		mock_derivative.return_value = 0.
		expected_output = 0.
		self.assertAlmostEqual(expected_output, mock_derivative(math.sin, 0., 100), places = 4)


if __name__ == '__main__':
	unittest.main()
