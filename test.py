import unittest
import main

class testCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(main.add(10, 5), 15)
		self.assertEqual(main.add(-5, 5), 0)
		self.assertEqual(main.add(-5, -5), -10)

	def test_sub(self):
		self.assertEqual(main.sub(10, 5), 5)
		self.assertEqual(main.sub(-5, 5), -10)
		self.assertEqual(main.sub(-5, -5), 0)
		
	def test_mult(self):
		self.assertEqual(main.mult(10, 5), 50)
		self.assertEqual(main.mult(-5, 5), -25)
		self.assertEqual(main.mult(-5, -5), 25)

	def test_div(self):
		self.assertEqual(main.div(10, 5), 2)
		self.assertEqual(main.div(-5, 5), -1)
		self.assertEqual(main.div(-5, -5), 1)

if __name__ == '__main__':
	unittest.main()