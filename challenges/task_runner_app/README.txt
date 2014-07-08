Design
    • Used the built-in Queue class to add tasks. 
    • Used the Thread module for parallel execution.
    • Does not account for the 'exclusive' flag for the task per the requirements. To be added later. 
    • Used unit tests for testing individual classes for easier integration

Implementation
    • Initially created the 'scratch_pad.py' program for a quick POC of the parallel execution and concurrency
    • Command class was implemented for differing responsibility of a single command within a task and having it deal with all the exceptions etc.
    • Task and TaskStatus class was implemented next and unit tested.
    • TaskRunner class was implemented at the end. Successfully tested with failed, passed and multiple task cases. There are still a lot of test cases to be incorporated!
    • #TODO tags as a reminder to implement later.
        Need to incorporate logger
        Add exceptions for all constructors and catch any wierd corner cases
        Need to do some more testing and debugging of the task manager
        
To Run Program
    • Extract and copy 'task_runner_app' module in your home directory.
    • Set PYTHONPATH via 'export PYTHONPATH=$HOME/task_runner_app'. Then:
        cd $HOME/task_runner_app
        python task_runner
    • Github Link: https://github.com/rehmanz/python-algorithms/tree/master/challenges/task_runner_app
    • Email: rehmanzile@gmail.com
