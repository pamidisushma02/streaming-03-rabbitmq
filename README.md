<<<<<<< HEAD
=======
# Name: Sushma Pamidi
# Repo: https://github.com/pamidisushma02/streaming-03-rabbitmq

>>>>>>> 42e8cb6 (Module 3)
# streaming-03-rabbitmq

Get started with RabbitMQ, a message broker, that enables multiple processes to communicate reliably through an intermediary

## Before You Begin

1. Fork this starter repo into your GitHub.
<<<<<<< HEAD
1. Clone your repo down to your machine.
1. In VS Code with Python extension, click on emit_message_v1.py to get VS Code in Python mode.
1. View / Command Palette - then Python: Select Interpreter
1. Select your conda environment. See the references below for more.
1. Use the terminal to install pika into your active environment. 

`conda install -c conda-forge pika`

## Read

1. Read the [RabbitMQ Tutorial - Hello, World!](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
1. Read the code and comments in this repo.

## Execute about,py

1. Run about.py.
1. Read about.txt. 
1. Verfiy you have exactly one active, one None env.
=======
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
>>>>>>> 42e8cb6 (Module 3)

## Version 1 - Execute the Producer/Sender

1. Read v1_emit_message.py (and the tutorial)
<<<<<<< HEAD
1. Run the file. 

You'll need to fix an error in the program to get it to run.
Once it runs and finishes, we can reuse the terminal.

## Version 1 - Execute the Consumer/Listener

1. Read v1_listen_for_messages.py (and the tutorial)
1. Run the file.

You'll need to fix an error in the program to get it to run.
Once it runs successfully, will it terminate on its own? How do you know? 
=======
2. Run the file. 

You'll need to fix an error in the program to get it to run. -- Fixed 
Once it runs and finishes, we can reuse the terminal -- Done


## Version 1 - Execute the Consumer/Listener

1. Read v1_listen_for_messages.py (and the tutorial) 
2. Run the file.

You'll need to fix an error in the program to get it to run. -- Fixed 
Once it runs successfully, will it terminate on its own? How do you know?  -- No it does not
>>>>>>> 42e8cb6 (Module 3)
As long as the process is running, we cannot use this terminal for other commands. 

## Version 1 - Open a New Terminal / Emit More Messages

<<<<<<< HEAD
1. Open a new terminal window.
1. Use this new window to emit more messages
1. In v1_emit_message.py, modify the message. 
1. Execute the script. 
1. Watch what happens in the listening window.
1. Do this several times to emit at least 3 different messages.
=======
1. Open a new terminal window 
2. Use this new window to emit more messages
3. In v1_emit_message.py, modify the message. 
4. Execute the script. 
5. Watch what happens in the listening window -- When I open multiple terminals the sent message is received in one of the terminal that is listening but not seen in all the listening terminals
6. Do this several times to emit at least 3 different messages -- Tested on 6 terminals 
>>>>>>> 42e8cb6 (Module 3)

## Version 1: Don't Repeat Yourself (DRY)

1. Did you notice you had to change the message in two places?
<<<<<<< HEAD
    1. You update the actual message sent. 
    1. You also update what is displayed to the user. 
1. Fix this by introducting a variable to hold the message. 
    1. Use your variable when sending. 
    1. Use the variable again when displaying to the user. 
=======
    i. You update the actual message sent. 
    ii. You also update what is displayed to the user. 
2. Fix this by introducting a variable to hold the message -- Done. Added a "message" variable
    i. Use your variable when sending. 
    ii. Use the variable again when displaying to the user. 
>>>>>>> 42e8cb6 (Module 3)

To send a new message, you'll only make one change.
Updating and improving code is called 'refactoring'. 
Use your skills to keep coding enjoyable. 

## Version 2

Now look at the second version of each file.
These include more graceful error handling,
and a consistent, reusable approach to building code.

Each of the version 2 programs include an error as well. 

<<<<<<< HEAD
1. Find the error and fix it. 
1. Compare the structure of the version 2 files. 
1. Modify the docstrings on all your files.
1. Include your name and the date.
1. Imports always go at the top, just after the file docstring.
1. Imports should be one per line - why?
1. Then, define your functions.
1. Functions are reuable logic blocks.
1. Everything the function needs comes in through the arguments.
1. A function may - or may not - return a value. 
1. When we open a connection, we should close the connection. 
1. Which of the 4 files will always close() the connection?
1. Search GitHub for if __name__ == "__main__":
1. How many hits did you get? 
1. Learn and understand this common Python idiom.
=======
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
>>>>>>> 42e8cb6 (Module 3)

## Reference

- [RabbitMQ Tutorial - Hello, World!](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)

## Multiple Terminals

![Mac Example](screenshot.png)
