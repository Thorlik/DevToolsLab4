import unittest
import calc


class CalculatorTestCase(unittest.TestCase):

    def test_zero_summ(self):
        res = calc.summ(0, 19)
        self.assertEqual(res, 19)

    def test_big_summ(self):
        res = calc.summ(4564546545645, 465456412312131231246523213131)
        self.assertEqual(res, 465456412312131235811069758776)

    def test_negatives_summ(self):
        res = calc.summ(-50, -6)
        self.assertEqual(res, -56)

    def test_floats_summ(self):
        res = calc.summ(6.06, 5.34)
        self.assertEqual(res, 11.4)



    def test_poz_sub(self):
        res = calc.sub(2, 25)
        self.assertEqual(res, -23)

    def test_big_sub(self):
        res = calc.sub(478798121354978, 12312465498742679865)
        self.assertEqual(res, -12311986700621324887)

    def test_zero_sub(self):
        res = calc.sub(0, 25)
        self.assertEqual(res, -25)

    def test_floats_sub(self):
        res = calc.sub(1000.345, 499.2)
        self.assertEqual(res, 501.15)



    def test_zero_mul(self):
        res = calc.mul(0, 60530)
        self.assertEqual(res, 0)

    def test_big_mul(self):
        res = calc.mul(564561321, 789756451321)
        self.assertEqual(res, 445865945426055955041)

    def test_negatives_mul(self):
        res = calc.mul(-5, -60)
        self.assertEqual(res, 300)

    def test_floats_mul(self):
        res = calc.mul(50.26, 34.523)
        self.assertEqual(res, 1735.13)



    def test_negatives_div(self):
        res = calc.div(56233, 294)
        self.assertEqual(res, 191.27)

    def test_big_div(self):
        res = calc.div(8979456112398, 976541346)
        self.assertEqual(res, 9195.16)

    def test_zero_div(self):
        res = calc.div(36, 0)
        self.assertEqual(res, 'На ноль делить нельзя')

    def test_floats_div(self):
        res = calc.div(36.5465, 5.4564)
        self.assertEqual(res, 6.7)



    def test_wrong_operation(self):
        res = calc.calculate(5, 5, 'd')
        self.assertEqual(res, 'Неизвестная операция')