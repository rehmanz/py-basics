'''
Created on Jul 7, 2014

@author: zrehman
'''
import unittest

from Queue import Queue
from threading import Thread
from task_runner_app.task.task import Task

""" TaskRunner Class """
class TaskRunner(object):
    def __init__(self, concurrency):
        """Create the task runner.
        Args:
          concurrency: the maximum number of tasks that can run in parallel
        """
        self.concurrancy = concurrency
        self.task_d      = {}       # Used to query task status
        self.workers_l   = []
        self.task_q      = Queue()
        self.stop_flag   = False    # Used to stop the task pool
        self.task_id     = 1
        
        # Setup a thread pool of size concurrency
        for i in range(self.concurrancy):
            self.thread = Thread(target=self.__worker)
            self.thread.setDaemon(True)
            self.workers_l.append(self.thread)
    
    def add_task(self, task):
        """Adds a task to the task pool.
        This may be called whether or not the task pool is currently running.
        Args:
          task: a Task object
        Returns:
          the task id associated with the task
        """
        # Add task to task dictionary so we can query status later
        self.task_d[self.task_id] = task
        self.task_id += 1
        
        # Places into task queue, asynchronously
        self.task_q.put(task)
        
        return self.task_id-1
    
    def start(self):
        """Asynchronously starts the task pool.
        This should cause the TaskRunner to begin executing tasks, however, it does
        not need to wait for execution to begin in order to return.
        """
        self.thread.start()
    
    def stop(self):
        """Synchronously stops the task pool.
        This function should wait until all running (but not queued) tasks have
        completed before returning.
        """
        self.stop_flag = True
    
    def status(self, task_id):
        """Get the status of a given task.
        Args:
          task_id: the task id returned by add_task
        Returns:
          TaskStatus object for the given task
        """
        if task_id in self.task_d:
            task = self.task_d[task_id]
            return task.get_task_status_object()
    
    def cleanup(self, task_id):
        """Removes the task status from the task runner if the task has completed
        Args:
          task_id: the task id returned by add_task
        """
        #TODO: Not sure what this method is trying to do?
        self.task_q.quit()
    
    def tasks(self, state=None):
        """Returns metadata regarding tasks currently added to the task pool.
        Args:
          state: a task state (see TaskStatus for enum defs) to filter for if
            specified, if not specified, return data regarding all tasks
        Returns:
          a list of (task_id, state, queue_position, task) defined as:
            task_id: the task id returned by add_task
            state: the state of the task (queued, running, complete)
            queue_position: the position of the task in the queue
            task: the task object
        """
        pass
    
    # OPTIONAL - you may skip implementation of this function
    def wait(self):
        """OPTIONAL) Wait for all tasks added to the task pool to execute.
        """
        # Wait for all tasks to be completed
        self.task_q.join()
    
    # OPTIONAL - you may skip implementation of this function
    def cancel_task(self, task_id):
        """Cancels the task with the given task ID if it has not yet been started.
        Args:
          task_id: the task id returned by add_task
        Returns:
          True if the task was canceled successfully, false otherwise
        """
        raise NotImplementedError('TaskRunnerExcpetion: cancel_task')
    
    def __worker(self):
        """Worker fetches tasks one by one from queue & executes them
        """
        while not self.stop_flag:
            task = self.task_q.get()
            task.execute()
            print 'Successfully complted task %s' %(task)
            self.task_q.task_done()
    
""" Unit Tests """
class TaskRunnerUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_failed_task(self):
        tr_o = TaskRunner(concurrency=2)
        task_o = Task(commands=['ls', 'ps -ef', 'whoami', 
                                'I think therefore I am'],
                           capture_output=True)
        task_id = tr_o.add_task(task_o)
        tr_o.start()
        tr_o.wait()
        tr_o.stop()
        
        task_status_o = tr_o.status(task_id=task_id)
        self.assertEqual(task_status_o.get_status(), 1)
        
    def test_passed_task(self):
        tr_o = TaskRunner(concurrency=2)
        task_o = Task(commands=['ls', 'ps -ef'],
                      capture_output=True)
        task_id = tr_o.add_task(task_o)
        tr_o.start()
        tr_o.wait()
        tr_o.stop()
        
        task_status_o = tr_o.status(task_id=task_id)
        self.assertEqual(task_status_o.get_status(), 0)
        
    def test_multiple_successful_tasks(self):
        tr_o = TaskRunner(concurrency=10)
        
        # Add tasks
        tasks_l = []
        task_o = Task(commands=['ls', 'ps -ef'],
                      capture_output=True)
        task_id = tr_o.add_task(task_o)
        tasks_l.append((task_id, task_o))
        
        task_o = Task(commands=['ls'],
                      capture_output=True)
        task_id = tr_o.add_task(task_o)
        tasks_l.append((task_id, task_o))
        
        task_o = Task(commands=['pwd', 'ps -ef'],
                      capture_output=True)
        task_id = tr_o.add_task(task_o)
        tasks_l.append((task_id, task_o))
        
        # Start execution
        tr_o.start()
        tr_o.wait()
        tr_o.stop()
        
        # Assess results
        for task_t in tasks_l:
            task_id        = task_t[0]
            task_status_o  = task_t[1]
            self.assertEqual(task_status_o.get_status(), 0)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def TaskRunnerUnitTestRunner():
    tests = ['test_failed_task',
             'test_passed_task']
    
    return unittest.TestSuite(map(TaskRunnerUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='TaskRunnerUnitTestRunner',
                  verbosity=2)
