import unittest
from sensor_module import *
class TestSensorManager(unittest.TestCase):
    def test_raise_alarm(self):
        self.assertEqual(water_sensor_1.raise_alarm(self,'1',200,300),'0')
        self.assertEqual(water_sensor_1.raise_alarm(self,'1',350, 300),'1')
        self.assertEqual(water_sensor_1.raise_alarm(self,'2',-250, 300), 'error')
        self.assertEqual(water_sensor_1.raise_alarm(self,'2',400, 300), '1')
        self.assertEqual(water_sensor_1.raise_alarm(self,'3',300, 300), '0')

    def test_get_address(self):
        water_sensor_1.set_address(self,'A')
        self.assertEqual(water_sensor_1.get_address(self),'A')

    def test_update_status(self):
        self.assertEqual(sensor_manager.update_status(self,'high'),"Status written in file as high")
        self.assertEqual(sensor_manager.update_status(self,'low'),"Status written in file as low")
    def test_control_net(self):
        self.assertEqual(sensor_manager.control_net(self,'raise net'),"Net Raised")
        self.assertEqual(sensor_manager.control_net(self, 'lower net'), "Net Lowered")

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestSensorManager('test_get_address'))
    suite.addTest(TestSensorManager('test_raise_alarm'))
    suite.addTest(TestSensorManager('test_update_status'))
    suite.addTest(TestSensorManager('test_control_net'))
    return suite

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())