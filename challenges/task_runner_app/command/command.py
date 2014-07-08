'''
Created on Jul 7, 2014

@author: zrehman
'''
import unittest

from subprocess import Popen, PIPE

""" Command Class """
class Command(object):
    def __init__(self, command):
        """Creates a command object
        Args:
          command: the shell command to execute
          
        """
        self.command = command

    def execute(self):
        """Executes the command and populates the results dictionary. Catches all the exceptions and wraps it in a nice results dictionary!
        """
        try:
            #TODO: We need a timeout logic for command that run forever!
            # Execute the command 
            p = Popen(self.command, shell=True, stdin=PIPE, stdout=PIPE,
                      stderr=PIPE, close_fds=True)
            
            # Set stdout, stderr and status
            self.stdout, self.stderr = p.communicate()
            if self.stderr:
                self.status = 1
            else:
                self.status = 0
        except Exception as e:
            self.status = 1
            self.stderr = 'CommandException: ' + str(e)
            self.stdout = None
        
        # Populate and return the results dictionary
        return {'status' : self.status,
                'stderr' : self.stderr,
                'stdout' : self.stdout}
            
""" Unit Tests """
class CommandUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_valid_command(self):
        self.cmd_o = Command(command='pwd')
        expected_d = {'status': 0, 
                      'stderr': '', 
                      'stdout': '/Users/zrehman/python-algorithms/challenges/instart_logic/task_runner_app/command\n'}
        self.assertDictEqual(self.cmd_o.execute(), expected_d)
    
    def test_invalid_command(self):
        self.cmd_o = Command(command='not a valid command')
        expected_d = {'status': 1, 
                      'stderr': '/bin/sh: not: command not found\n', 
                      'stdout': ''}
        self.assertDictEqual(self.cmd_o.execute(), expected_d)
    
    def test_complicated_command(self):
        self.cmd_o = Command(command="cat command.py | grep \'class Command(object)\'")
        actual_d = self.cmd_o.execute()
        self.assertEqual(actual_d['status'], 0)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def CommandUnitTestRunner():
    tests = ['test_valid_command',
             'test_invalid_command',
             'test_complicated_command']
    
    return unittest.TestSuite(map(CommandUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='CommandUnitTestRunner',
                  verbosity=2)
