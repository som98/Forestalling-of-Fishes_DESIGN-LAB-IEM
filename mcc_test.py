import unittest
from mcc import *
class TestMcc(unittest.TestCase):

    def test_configure_threshold(self):
        self.assertEqual(main_control_center.configure_threshold(self),300)

    def test_send_signal(self):
        self.assertEqual(main_control_center.send_signal(self,'MAC'),1)
        self.assertEqual(main_control_center.send_signal(self,'null'),0)
        self.assertEqual(main_control_center.send_signal(self,''),0)

    def test_send_instruction(self):
        self.assertEqual(main_control_center.send_instruction(self,1),'raise net')
        self.assertEqual(main_control_center.send_instruction(self,0), 'lower net')

    def test_receive_status(self):
        self.assertEqual(main_control_center.receive_status(self,'high'), 1)
        self.assertEqual(main_control_center.receive_status(self, 'low'), 0)

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestMcc('test_configure_threshold'))
    suite.addTest(TestMcc('test_send_signal'))
    suite.addTest(TestMcc('test_send_instruction'))
    suite.addTest(TestMcc('test_receive_status'))
    return suite

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
