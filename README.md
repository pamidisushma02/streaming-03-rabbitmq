# Name: Sushma Pamidi
# Repo: https://github.com/pamidisushma02/streaming-03-rabbitmq
# Notes: Responses are added as well 

# streaming-03-rabbitmq

Get started with RabbitMQ, a message broker, that enables multiple processes to communicate reliably through an intermediary

## Before You Begin -- Done

1. Fork this starter repo into your GitHub.
2. Clone your repo down to your machine.
3. In VS Code with Python extension, click on emit_message_v1.py to get VS Code in Python mode.
4. View / Command Palette - then Python: Select Interpreter
5. Select your conda environment. See the references below for more.
6. Use the terminal to install pika into your active environment. 

`conda install -c conda-forge pika`

# All above are done

## Read

1. Read the [RabbitMQ Tutorial - Hello, World!](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
2. Read the code and comments in this repo.

# All above are done

## Execute about,py

1. Run about.py. -- Done
2. Read about.txt. --Done
3. Verfiy you have exactly one active, one None env. -- Yes

## Version 1 - Execute the Producer/Sender

1. Read v1_emit_message.py (and the tutorial)
2. Run the file. 

You'll need to fix an error in the program to get it to run. -- Fixed 

Once it runs and finishes, we can reuse the terminal -- Done


## Version 1 - Execute the Consumer/Listener

1. Read v1_listen_for_messages.py (and the tutorial) 
2. Run the file.

You'll need to fix an error in the program to get it to run. -- Fixed 

Once it runs successfully, will it terminate on its own? How do you know?  -- No it does not terminate on its own. We can not execute any other command on the terminal. We can use ctrl + C to terminate the process and then run any other command

As long as the process is running, we cannot use this terminal for other commands. 

## Version 1 - Open a New Terminal / Emit More Messages

1. Open a new terminal window 
2. Use this new window to emit more messages
3. In v1_emit_message.py, modify the message. 
4. Execute the script. 
5. Watch what happens in the listening window -- When I open multiple terminals the sent message is received in one of the terminal that is listening but not seen in all the listening terminals
6. Do this several times to emit at least 3 different messages -- Tested on 6 terminals 

## Version 1: Don't Repeat Yourself (DRY)

1. Did you notice you had to change the message in two places?
    i. You update the actual message sent. 
    ii. You also update what is displayed to the user. 
2. Fix this by introducting a variable to hold the message -- Done. Added a "message" variable
    i. Use your variable when sending. 
    ii. Use the variable again when displaying to the user. 

To send a new message, you'll only make one change.
Updating and improving code is called 'refactoring'. 
Use your skills to keep coding enjoyable. 

## Version 2

Now look at the second version of each file.
These include more graceful error handling,
and a consistent, reusable approach to building code.

Each of the version 2 programs include an error as well. 

1. Find the error and fix it -- Fixed. Most files had localhost spelled incorrectly
2. Compare the structure of the version 2 files -- Second one is more clean and structured with error handling  
3. Modify the docstrings on all your files -- Done
4. Include your name and the date -- Done
5. Imports always go at the top, just after the file docstring.
6. Imports should be one per line - why? -- Anything after the import keyword is treated as a module name so all the words in the same line are treated as one module name
7. Then, define your functions.
8. Functions are reuable logic blocks.
9. Everything the function needs comes in through the arguments.
10. A function may - or may not - return a value. 
11. When we open a connection, we should close the connection. 
12. Which of the 4 files will always close() the connection?
13. Search GitHub for if __name__ == "__main__":
14. How many hits did you get? -- I see 39,993,666 in Code, Approximately 1 Million in Commits, 88K in Issues, 1,884 in Discussions, 5,442 in Wiki results
15. Learn and understand this common Python idiom.

## Reference

- [RabbitMQ Tutorial - Hello, World!](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)

## Multiple Terminals
-[Terminal 1](https://github.com/pamidisushma02/streaming-03-rabbitmq/blob/main/Terminal%201.png?raw=true)

-[Terminal 2](https://github.com/pamidisushma02/streaming-03-rabbitmq/blob/main/Terminal%202.png)

-[Terminal 3](https://github.com/pamidisushma02/streaming-03-rabbitmq/blob/main/Terminal%203.png)

-[Terminal 4](https://github.com/pamidisushma02/streaming-03-rabbitmq/blob/main/Terminal%204.png)

-[Terminal 5](https://github.com/pamidisushma02/streaming-03-rabbitmq/blob/main/Terminal%205.png)

-[Terminal 6](https://github.com/pamidisushma02/streaming-03-rabbitmq/blob/main/Terminal%206.png)

