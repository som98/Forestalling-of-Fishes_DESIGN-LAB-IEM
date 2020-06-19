import unittest
from sensor_manager import *
class TestSensorManager(unittest.TestCase):

    def test_update_status(self):
        self.assertEqual(sensor_manager.update_status(self,'high'),"Status written in file as high")
        self.assertEqual(sensor_manager.update_status(self,'low'),"Status written in file as low")
    def test_control_net(self):
        self.assertEqual(sensor_manager.control_net(self,'raise net'),"Net Raised")
        self.assertEqual(sensor_manager.control_net(self, 'lower net'), "Net Lowered")

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestSensorManager('test_update_status'))
    suite.addTest(TestSensorManager('test_control_net'))
    return suite

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())