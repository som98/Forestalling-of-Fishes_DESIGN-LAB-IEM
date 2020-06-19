import unittest
from sensor_module import *
class TestSensorManager(unittest.TestCase):
    def test_raise_alarm(self):
        self.assertEqual(sensor_manager.raise_alarm(self,'1',200,300),'0')
        self.assertEqual(sensor_manager.raise_alarm(self,'1',350, 300),'1')
        self.assertEqual(sensor_manager.raise_alarm(self,'2',-250, 300), 'error')
        self.assertEqual(sensor_manager.raise_alarm(self,'2',400, 300), '1')
        self.assertEqual(sensor_manager.raise_alarm(self,'3',300, 300), '0')

    def test_update_status(self):
        self.assertEqual(sensor_manager.update_status(self,'1','1'),"Status written in file as high")
        self.assertEqual(sensor_manager.update_status(self,'2','0'),"Status written in file as low")
    def test_control_net(self):
        self.assertEqual(sensor_manager.control_net(self,'raise net'),"Net Raised")
        self.assertEqual(sensor_manager.control_net(self, 'lower net'), "Net Lowered")

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestSensorManager('test_raise_alarm'))
    suite.addTest(TestSensorManager('test_update_status'))
    suite.addTest(TestSensorManager('test_control_net'))
    return suite

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())