'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest
import re

from kick_off_host_state import KickOffHostState
from configure_host_state import ConfigureHostState
from cleanup_host_state import CleanupHostState

""" TestRunnerStateMachine Class """
class TestRunnerStateMachine:
    def __init__(self, host):
        self.host  = host
        self.kick_off_host_state_o  = KickOffHostState(state=self,
                                                       host=self.host)
        self.configure_host_state_o = ConfigureHostState(state=self,
                                                         host=self.host)
        self.cleanup_host_state_o   = CleanupHostState(state=self,
                                                       host=self.host)
        self.state = self.kick_off_host_state_o
        
    """ Mutator Methods """
    def set_runner_state(self, state):
        self.state = state
        
    def kick_off_host_state(self):
        self.state.kick_off_host_state()
    
    def configure_host_state(self):
        self.state.configure_host_state()
        
    def cleanup_host_state(self):
        self.state.cleanup_host_state()
    
    """ Accessor Methods """
    def get_current_state(self):
        return self.state
    
    def get_kick_off_host_state(self):
        return self.kick_off_host_state_o
    
    def get_configure_host_state(self):
        return self.configure_host_state_o
    
    def get_cleanup_host_state(self):
        return self.cleanup_host_state_o
    
""" Unit Tests """
class TestRunnerStateMachineUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tr = TestRunnerStateMachine(host='Host1')
        
    def test_kick_off_host_state(self):
        # Verify current state
        current_state = str(self.tr.get_current_state())
        expr = re.compile('^<\w+\.KickOffHostState instance.*')
        self.assertTrue(bool(expr.match(current_state)))
        
        self.tr.kick_off_host_state()
        
        # Verify transitioned state
        current_state = str(self.tr.get_current_state())
        expr = re.compile('^<\w+\.ConfigureHostState instance.*')
        self.assertTrue(bool(expr.match(current_state)))
    
    def test_configure_host_state(self):
        # Verify current state
        current_state = str(self.tr.get_current_state())
        expr = re.compile('^<\w+\.ConfigureHostState instance.*')
        self.assertTrue(bool(expr.match(current_state)))
        
        self.tr.configure_host_state()
        
        # Verify transitioned state
        current_state = str(self.tr.get_current_state())
        expr = re.compile('^<\w+\.CleanupHostState instance.*')
        self.assertTrue(bool(expr.match(current_state)))
    
    def test_cleanup_host_state(self):
        # Verify current state
        current_state = str(self.tr.get_current_state())
        expr = re.compile('^<\w+\.CleanupHostState instance.*')
        self.assertTrue(bool(expr.match(current_state)))
        
        self.tr.cleanup_host_state()
        
        # Verify transitioned state
        current_state = str(self.tr.get_current_state())
        expr = re.compile('^<\w+\.KickOffHostState instance.*')
        self.assertTrue(bool(expr.match(current_state)))
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def TestRunnerStateMachineUnitTestRunner():
    tests = ['test_kick_off_host_state',
             'test_configure_host_state',
             'test_cleanup_host_state']
    
    return unittest.TestSuite(map(TestRunnerStateMachineUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='TestRunnerStateMachineUnitTestRunner',
                  verbosity=2)