'''
Created on Jul 7, 2014

@author: zrehman
'''
import unittest

""" TaskStatus Class """
class TaskStatus(object):
    STATUS_COMPLETE = "complete"
    STATUS_QUEUED = "queued"
    STATUS_RUNNING = "running"
    RESULT_OK = "ok"
    RESULT_FAIL = "fail"
    def __init__(self, status, result=None, stdout=None, stderr=None, info=None):
        """Create the TaskStatus
        Args:
          status: the status of the given task (use constants)
          result: the result of the given task if completed (use constants)
          stdout: the stdout if output was requested
          stderr: the stderr if output was requested
          info: a string of returncode and command that failed if result is failed
        """
        self.status = status
        self.result = result
        self.stdout = stdout
        self.stderr = stderr
        self.info   = info
    
    """Set task status.
    Args:
        status: the status of the given task. 0 for SUCCESS, non-zero otherwise
    """
    def set_status(self, status):
        self.status = int(status)
    
    """Set task result if completed. 
    Args:
        result: the result of the given task if completed. 0 for SUCCESS, non-zero otherwise
    """
    def set_result(self, result):
        self.result = int(result)
    
    """Set stdandard output
    Args:
        stdout: the stdout
    """
    def set_stdout(self, stdout):
        self.stdout = 0
    
    """Set stdandard error output
    Args:
        stderr: the stderr
    """
    def set_stderr(self):
        return self.stderr
    
    """Return task status. 0 for SUCCESS, non-zero otherwise
    """
    def get_status(self):
        return self.status
    
    """Return task result if completed. 0 for SUCCESS, non-zero otherwise
    """
    def get_result(self):
        return self.result
    
    """Return stdandard output
    """
    def get_stdout(self):
        return self.stdout
    
    """Return stdandard error output
    """
    def get_stderr(self):
        return self.stderr
    
    """Return a string of returncode and command that failed if result is failed
    """
    def get_info(self):
        raise NotImplementedError('TaskStatusExcpetion: get_info')
    
    def __str__(self):
        out = "\n"
        out += "status         : %s\n" %(self.status)  
        out += "result         : %s\n" %(self.result)
        out += "Standard Output: %s\n" %(self.stdout)
        out += "Standard  Error: %s\n" %(self.stderr)
        if self.stderr:
            out += "Task Info.     : %s\n" %(self.info)
        return out
    
""" Unit Tests """
class TaskStatusUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.task_status_o = TaskStatus(status="complete",
                                        result="0",
                                        stdout="Result Output",
                                        stderr=None)
    
    def test_print_task(self):
        self.assertEquals(str(self.task_status_o), str(self.task_status_o))
        
    def test_get_status(self):
        self.assertEquals(self.task_status_o.get_status(), "complete")
    
    def test_get_result(self):
        self.task_status_o.set_result(result=0)
        self.assertEquals(self.task_status_o.get_result(), 0)
    
    def test_get_stdout(self):
        self.assertEquals(self.task_status_o.get_stdout(), "Result Output")
    
    def test_get_stderr(self):
        self.assertEquals(self.task_status_o.get_stderr(), None)
    
    def test_get_info(self):
        pass
    #    self.assertEquals(self.task_status_o.get_info(), "complete")
    
    #TODO: Add tests for setter methods as well!
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def TaskStatusUnitTestRunner():
    tests = ['test_print_task',
             'test_get_status',
             'test_get_result',
             'test_get_stdout',
             'test_get_stderr',
             'test_get_info']
    
    return unittest.TestSuite(map(TaskStatusUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='TaskStatusUnitTestRunner',
                  verbosity=2)
