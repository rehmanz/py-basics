'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" CleanupHostState Class """
class CleanupHostState:
    def __init__(self, state, host):
        self.state = state
        self.host  = host
    
    def get_current_state(self):
        return self.state
        
    def kick_off_host_state(self):
        print '##'
        print '# CleanupHostState: %s' %self.host
        print '##'
        print '1: Send Cleanup command to %s' %self.host
        print '2: Got SUCCESS from %s' %self.host
        print '3: Send Exit command to %s' %self.host
        self.state.set_runner_state(state=self.state.get_kick_off_host_state())
        print '4: Transitioned to KickOffHostState'
        return 'Cleaned up %s' %self.host
    
    def configure_host_state(self):
        print 'Cannot configure %s from CleanupHostState' %self.host
        
    def cleanup_host_state(self):
        pass
    
""" Unit Tests """
class CleanupHostStateUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def CleanupHostStateUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(CleanupHostStateUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='CleanupHostStateUnitTestRunner',
                  verbosity=2)