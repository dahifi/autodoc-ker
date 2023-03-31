[View code on GitHub](https://github.com/pHaeusler/micro-agent/agent/prompts.py)

The code provided is a set of constants that define various prompts and messages used in a larger project called micro-agent. The purpose of this code is to provide standardized prompts and messages for tasks that need to be completed within the micro-agent project. 

The `PREFIX` constant defines a message that is used at the beginning of each task prompt. It includes a placeholder for a module summary and a placeholder for the purpose of the code. This message is used to provide context for the task at hand.

The `ACTION_PROMPT` constant defines a message that is used to prompt the user to take action on a task. It lists the available actions that can be taken and provides instructions on how to complete the task. This message is used to guide the user through the task and ensure that they are taking the correct actions.

The `TASK_PROMPT` constant defines a message that is used to prompt the user to define a task that needs to be completed in order to achieve the code purpose. This message is used to ensure that the user is breaking down the larger goal into smaller, more manageable tasks.

The `READ_PROMPT`, `ADD_PROMPT`, and `MODIFY_PROMPT` constants define messages that are used to prompt the user to read, add, or modify a file, respectively. These messages provide instructions on how to complete the task and what information is needed to do so.

The `UNDERSTAND_TEST_RESULTS_PROMPT` constant defines a message that is used to prompt the user to analyze test results and determine why they failed. This message is used to guide the user through the debugging process and ensure that they are able to fix any issues that arise.

The `COMPRESS_HISTORY_PROMPT` constant defines a message that is used to prompt the user to summarize their progress on a task. This message is used to ensure that the user is keeping track of their progress and is able to communicate their progress to others working on the project.

Overall, this code provides a set of standardized prompts and messages that are used to guide users through tasks in the micro-agent project. By providing clear instructions and guidance, this code helps ensure that tasks are completed correctly and efficiently.
## Questions: 
 1. What is the purpose of this code?
- The purpose of this code is to provide prompts and instructions for completing tasks related to a micro-agent project.

2. What are the available actions that can be taken?
- The available actions that can be taken include UPDATE-TASK, READ-FILE, MODIFY-FILE, ADD-FILE, TEST, and COMPLETE.

3. How can test results be understood and fixed?
- Test results can be understood and fixed by reviewing the STDOUT and STDERR outputs and describing why the tests failed and how to fix them.