from trainPriceCalc import train_fare_calc
import unittest


class TrainFareTest(unittest.TestCase):

    def test_discount(self):
        """
        Test if applying discounts to train ride gives the correct fare
        """
        self.assertEqual(train_fare_calc(10, True, 100), 56.0)
        self.assertEqual(train_fare_calc(20, True, 100), 48.0)
        self.assertEqual(train_fare_calc(80, True, 100), 56.0)

        self.assertEqual(train_fare_calc(10, False, 100), 52.0)
        self.assertEqual(train_fare_calc(20, False, 100), 80.0)
        self.assertEqual(train_fare_calc(80, False, 100), 52.0)

    def test_negative_distance(self):
        """
        Test for negative travel distance to not give a negative fare
        """
        self.assertEqual(train_fare_calc(10, True, -100), 0)
        self.assertEqual(train_fare_calc(20, True, -100), 0)
        self.assertEqual(train_fare_calc(80, True, -100), 0)

        self.assertEqual(train_fare_calc(10, False, -100), 0)
        self.assertEqual(train_fare_calc(20, False, -100), 0)
        self.assertEqual(train_fare_calc(80, False, -100), 0)


if __name__ == '__main__':
    unittest.main()



