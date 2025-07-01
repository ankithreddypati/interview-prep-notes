Quick review of OS: 
 https://codeforces.com/blog/entry/93861

A. Operating system: is a software that acts as interface between computer hardware and 
user applications, it manges the resources and provides services for 
Efficient and secure execution of programs , function include 1. Process management
 2. Memory management 3. File management 4. Device management and user interface 


 Program : a set of instructions written in a programming language that perform a specific task
stored as file on disk . Any executable or user programs like webbrowser etc 

process: an instance of program in execution when program is loaded into memory .ie ram and executed . ,
 managed by os , each process runs in its own protected memory space , can be concurrent and communicate 
 with IPC (interprocess communication) . 

pipe command in linux command is IPC between processes

3. Process Control Block(PCB)
    It is a data structure that stores all information about a process.
    It contains these:
    Process State: We already saw these
    Process ID: self-explanatory
    CPU registers and Program Counter: It is basically a pointer to the next instruction to be executed.
    CPU scheduling information: priority and pointers to scheduling queues(will see later)
    Memory management information: self-explanatory
    Accounting Information: CPU time consumed, limits, etc.
    I/o Status information: Devices allocated, open file tables, etc.