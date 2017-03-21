import abc
import math
from scipy import misc as sp
import types


class abstractCalculator(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def add(self, number1, number2):
		"""add two numbers"""

	@abc.abstractmethod
	def divide(self, number1, number2):
		"""divide two numbers"""

	@abc.abstractmethod
	def logarithm(self, number):
		"""natural logarithm of given number"""

	@abc.abstractmethod
	def derivative(self, func, point, order):
		"""compute derivative of given function (and given order) at given point"""


class calculator(abstractCalculator):
	def __init__(self):
		pass

	def add(self, number1, number2):
		if not self._isNumber(number1):
			raise notANumber
		if not self._isNumber(number2):
			raise notANumber
		return number1 + number2

	def divide(self, number1, number2):
		if not self._isNumber(number1):
			raise notANumber
		if not self._isNumber(number2):
			raise notANumber
		if not number2:
			raise dividingByZero
		return number1 / number2

	def logarithm(self, number):
		if not self._isNumber(number):
			raise notANumber
		if not self._isPositiveNumber(number):
			raise notAPositiveNumber
		return math.log(number)

	def derivative(self, func, point, order = 1):
		if not self._isFunction(func):
			raise notAFunction
		if not self._isNumber(point):
			raise notANumber
		if not self._isInt(order):
			raise notAnInteger
		if not self._isPositiveNumber(order):
			raise notAPositiveNumber
		if order == 1:
			return sp.derivative(func, point, dx = 1e-4)
		else:
			if self._isOddNumber(order):
				return sp.derivative(func, point, dx = 1e-2, n = order, order = order+2)
			else:
				return sp.derivative(func, point, dx = 1e-2, n = order, order = order+1)

	def _isNumber(self, number):
		return (self._isInt(number) or self._isFloat(number))

	def _isInt(self, number):
		return isinstance(number, int)

	def _isFloat(self, number):
		return isinstance(number, float)

	def _isPositiveNumber(self, number):
		return number > 0.

	def _isOddNumber(self, number):
		return number % 2

	def _isFunction(self, func):
		return callable(func)


class notANumber(Exception):
	pass


class notAnInteger(Exception):
	pass


class notAPositiveNumber(Exception):
	pass


class dividingByZero(Exception):
	pass


class notAFunction(Exception):
	pass
