'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" ConfigureHostState Class """
class ConfigureHostState:
    def __init__(self, state, host):
        self.state = state
        self.host  = host
    
    def get_current_state(self):
        return self.state
        
    def kick_off_host_state(self):
        print 'Cannot kick off %s from ConfigureHostState' %self.host
    
    def configure_host_state(self):
        print '##'
        print '# ConfigureHostState: %s' %self.host
        print '##'
        print '1: Got a CONFIG_REQUEST from %s' %self.host
        print '2: Sent <HOST_CONFIG> to %s' %self.host
        print '3: Got an ACK from %s' %self.host
        self.state.set_runner_state(state=self.state.get_cleanup_host_state())
        print '4: Transitioned to CleanupHostState'
        return 'Configured %s' %self.host
        
    def cleanup_host_state(self):
        print 'Cannot clean up %s from ConfigureHostState' %self.host
    
""" Unit Tests """
class ConfigureHostStateUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def ConfigureHostStateUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(ConfigureHostStateUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='ConfigureHostStateUnitTestRunner',
                  verbosity=2)