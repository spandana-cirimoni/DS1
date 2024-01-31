# Distributed System Simulation

## Introduction
This project simulates a simple distributed system with four process objects (PO), each containing a logical clock, based on the principles of clock consistency and drifts in a distributed system. The simulation is written in Python using threads.

## Files Included
- `main.py`: The main script to run the simulation.
- `Process.py`: The class definition for the Process objects.
- `makefile`: A makefile for easy compilation and execution.
- `README.md`: This file providing information about the project, how to run it, and any additional details.

## How to RUN
- Make sure you have installed Python3 before running the code
- Run the main.py using "make" command
- stop the execution after few seconds/minutes as it is running in infinite loop

## Program Structure
- The main program initializes four processes and their message queues.
- Each process runs in a separate thread, simulating internal events, sending, and receiving messages.
- Logical clocks are updated.

## Design Choices
- Processes are implemented as threads to simulate concurrent execution.
- A queue is used for message passing between processes.
- Random selection of processes for sending messages to introduce non-deterministic behavior.
