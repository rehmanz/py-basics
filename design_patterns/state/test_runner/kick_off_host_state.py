'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" KickOffHostState Class """
class KickOffHostState:
    def __init__(self, state, host):
        self.state = state
        self.host  = host
        
    def get_current_state(self):
        return self.state
        
    def kick_off_host_state(self):
        print '##'
        print '# KickOffHostState: %s' %self.host
        print '##'
        print '1: Kicked off %s' %self.host
        print '2: Got a HELLO from %s' %self.host
        print '3: Sent an ACK to %s' %self.host
        self.state.set_runner_state(state=self.state.get_configure_host_state())
        print '4: Transitioned to ConfigureHostState'
        return 'Kicked off %s' %self.host
    
    def configure_host_state(self):
        print 'Cannot configure %s from KickOffHostState' %self.host
        
    def cleanup_host_state(self):
        print 'Cannot cleanup %s from KickOffHostState' %self.host
    
""" Unit Tests """
class KickOffHostStateUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def KickOffHostStateUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(KickOffHostStateUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='KickOffHostStateUnitTestRunner',
                  verbosity=2)