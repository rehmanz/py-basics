Notes
    • Finally have the quick program in "scratch_pad.py" that will fulfill requirements related to concurrency
    • Copy the task_runner module to your $HOME directory and set PYTHONPATH=$HOME/task_runner_app
    • Creating a separate command class made it much easier to deal with tasks
    • Now incorporating TaskStatus into Task and utilizing the command class to test executing a single task (i.e. list of commands)
    • Adding getter and setter for TaskStatus to make it easier for Task class to report and manage it's status (i.e. good coding practice instead of accessing the instance vars!)
    • TaskRunner is having issues. Need to debug further.
    
To Dos
    • Need to incorporate logger
    • Add exceptions for all constructors and catch any wierd corner cases
    • Need to do some more testing and debugging of the task manager

--------------------------------------------------------------------------------
Design
    • Create a separate TaskThread class to support executing tasks in parallel 
    • TaskRunner
        Use a thread list (threads_l) to add tasks 
        TODO: Implement concurrentcy later. (i.e. assume we can run all tasks in parallel)
            Using worker queues and locks, limit the number of tasks that can be executed
    • Breakup individual classes into separate files for include unit tests (ie. TDD)

Implementation
    • I was trying to put together a quick program in "scratch_pad.py" that will fulfill all the requirements. I could not get it to work so I had to cut back the design and added the #TODO tags as a reminder to implement later.
    • Skeleton unit test structure was added and it runs successfully so far. But both code and unit test cases are far from being completed.
    • Will continue to work on the program on my own time!

