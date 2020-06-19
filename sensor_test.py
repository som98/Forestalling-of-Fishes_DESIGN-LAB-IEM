import unittest
from sensor import *
class TestSensor(unittest.TestCase):
    def test_raise_alarm(self):
        self.assertEqual(water_sensor_1.raise_alarm(self,'1',200,300),'0')
        self.assertEqual(water_sensor_1.raise_alarm(self,'1',350, 300),'1')
        self.assertEqual(water_sensor_1.raise_alarm(self,'2',-250, 300), 'error')
        self.assertEqual(water_sensor_1.raise_alarm(self,'2',400, 300), '1')
        self.assertEqual(water_sensor_1.raise_alarm(self,'3',300, 300), '0')

    def test_get_address(self):
        water_sensor_1.set_address(self,'A')
        self.assertEqual(water_sensor_1.get_address(self),'A')

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestSensor('test_get_address'))
    suite.addTest(TestSensor('test_raise_alarm'))
    return suite

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())