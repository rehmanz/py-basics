'''
Created on Jul 7, 2014

@author: zrehman
'''
import unittest

from task_runner_app.task.task_status import TaskStatus
from task_runner_app.command.command import Command

""" Task Class """
class Task(object):
    def __init__(self, commands, capture_output=False, exclusive=False):
        """Creates a task object
        Args:
          commands: a list of shell commands
          capture_output: true if the stdout / stderr of the commands needs to be recorded
          exclusive: true if the task cannot run concurrently with other tasks
        """
        self.commands = commands
        self.capture_output = capture_output
        self.exclusive = exclusive
        self.results_l = [] # Stores a list of results dictionaries
    
    def execute(self):
        """Executes the task and populate the TaskStatus
        """
        # Execute individual commands within the task and store results
        for command in self.commands:
            command = Command(command=command)
            self.results_l.append(command.execute())
        
        self.__report_results()
        
    def get_task_status_object(self):
        return self.status_o
    
    def __report_results(self):
        status = 0
        result = 0  # We will assume all tasks will be completed for now
        stdout = ''
        stderr = ''
        
        # Accumalate task status from the executed commands
        for result in self.results_l:
            # 0 is SUCCESS, non-zero for num of fails
            status += result['status']
            
            if self.capture_output:
                stdout += result['stdout']
                stderr += result['stderr']
        
        # Task status object for this task
        self.status_o = TaskStatus(status=status,
                                   result=result,
                                   stdout=stdout,
                                   stderr=stderr,
                                   info=None) 
        #print self.status_o
    
""" Unit Tests """
class TaskUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.task_o = Task(commands=['ls', 'ps -ef', 'whoami', 
                                     'I think therefore I am'],
                           capture_output=True)
    
    def test_it(self):
        self.task_o.execute()
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def TaskUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(TaskUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='TaskUnitTestRunner',
                  verbosity=2)
