# FRC New Programming Student Python Training

Last Updated: May 1, 2023

## Overview of Training Topics

This is a list of topics that I'm putting together to train new FRC robotics students. It's obviously not complete but will cover the following when completed:
* Basic robot safety issues
* Introduction to FRC hardware and wiring
* Fundamentals of Python
* More advanced Python topics (particulary OOP)
* robotpy
* Introduction to computer vision
* Scouting (and in particular using Python to pull & analyze data)

New programming students are also required to take the basic handtools, mechanical, and electrical training in the preseason.

## Detailed List of Training Topics
#### 1. Safety (Focused a lot on issues that programmers would deal with while testing code)
* ***General Knowledge***
   * Battery Safety
     * How to safely carry a battery
     * The cables are not a handle!
     * What happens if battery is dropped?
     * What about a leaking battery?
   * No long hair (should be tied back), dangling jewelry, ties, loose clothing, etc. when working around a robot
   * Lifting
   * Assume anything designed to shoot/throw an object can do that during testing and avoid being in front of it.
   * Assume that a robot will travel in a direction you don't expect.
     * Keep distance and barrier between you and robot.
     * Be prepared to emergency stop the robot
   * [Robot Signal Light (RSL) - What do the following states indicate?](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html#robot-signal-light-rsl)
     * Off
     * On
     * On & Blinking 
  * ***Demonstrate how to do the following:***
    * [Perform an emergency stop of the robot](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html#driver-station-key-shortcuts)
    * Show how to safely carry a battery
    * Show how to turn on/off the robot
  * ***Robotics Safety Links***
    * [2023 FRC Safety Manual](https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/team-resources/safety/2023/2023-Safety-Manual.pdf)
    * [WPILIB Battery Safety & Handling](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-battery.html#battery-safety-handling)

#### 2. Robot Hardware - Part 1
* ***General Knowledge***
  * roboRIO
    * What IP address(es) does the RIO have?
    * [What do the LED status lights mean?](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html#roborio)
    * Identify and know what the various ports are used for:
      * Power Connector
      * Ethernet
      * USB
      * DIO
      * PWM
      * CAN Bus
    * [How do you update the image?](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/roborio2-imaging.html)
    * [How do you update the team number?](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/roborio2-imaging.html#setting-the-roborio-team-number)
    * Why is it important to have the team number correct?
    * [What is a brownout?](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-brownouts.html)
  * CAN Bus
    * Understand how the CAN bus is wired
    * Where are the ends of the CAN bus connected in a robot?
    * What happens if there is a break in the CAN bus?
    * How do you identify the CAN bus wires?
  * Motors & Motor Controllers
    * Be able to identify common FRC motors
    * Know what motor controllers can be used with motors
    * Explain difference between brushed and brushless motors
    * Know if these common motors are brushed or brushless
    * What are advantages/disadvantage of brushed/brushless motors?
    * Talon SRX LED Codes
    * Spark MAX LED Codes
  * Other hardware on the robot:
    * [Power Distribution Panel (PDP)](https://store.ctr-electronics.com/power-distribution-panel/)/[Power Distribution Hub(PDH)](https://www.revrobotics.com/rev-11-1850/)
    * Voltage Regulator Module (VRM)
    * Pneumatics Control Module (PCM)
    * Radio (lights, boot up, radio configuration utility)
    * Pigeon
  * Driver Station
    * Understand the red/green indicators for communication, robot code, and joystick
    * Be able to debug issues with those indicators especially for communications
    * [Know how to change the team number](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html#setting-up-the-driver-station)
    * [Know how to perform an emergency stop](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html#driver-station-key-shortcuts)
* ***Demonstrate how to do the following:***
  * roboRIO
    * Connect to the roboRIO via USB and demonstrate that robot communication has been established
    * Connect to the roboRIO via the radio (assuming the test bench has a radio) and demonstrate that robot communication has been established
    * Update the image
    * Update the team number
  * Update firmware:
    * Spark Max Motor Controller
    * Talon SRX Motor Controller
  * [Show how to configure a Spark Max motor controller to use a brushed or brushless motor](https://docs.revrobotics.com/sparkmax/operating-modes/motor-type-brushed-brushless-mode)
  * CAN Bus
    * Identify the wires used in the CAN Bus
    * Check/Update CAN IDs with
      * Phoenix Tuner
      * REV Hardware Client
   * Deploy sample code to the robot and demonstrate that the code is executing properly
   * [Change team number in driver station](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html#setting-up-the-driver-station)
* ***Robot Hardware Links***
  * [WPILIB roboRIO Introduction](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-introduction.html)
  * [roboRIO User Manual](https://www.ni.com/docs/en-US/bundle/roborio-20-umanual/page/umanual.html)
  * [Brushed Vs Brushless Motor - What Is The Difference?](https://www.youtube.com/watch?v=4LW-iUehJh8)
#### 3. Robot Hardware - Part 2
  * ***General Knowledge***
    * Drivetrains
      * Be able to identify common drivetrains
      * Be able to explain the advantages/disadvantages of various common drivetrains
    * Gears
    * Sensors
      * Encoders
        * Absolute
        * Relative
      * [Limit switches](https://docs.wpilib.org/en/2020/docs/software/old-commandbased/commands/limit-switches-control-behavior.html)
      * Beam break sensors
      * Potentiometers
      * Gyro
  * ***Demonstrate how to do the following:***
    * Gear activity with LEGO
    * This needs to bge developed more
  * ***Additional Robot Hardware Links***
    * Drivetrains
      * [Intro to FRC Mechanisms](https://www.youtube.com/watch?v=JTZ31lpMkfA)
      * [REV Drivetrain Info](https://docs.revrobotics.com/frc-kickoff-concepts/charged-up-2023/drivetrains)
      * [What Does an FRC Drivetrain Do?](https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/team-resources/behind-the-lines/2017/btl-s03e04-drivetrains.pptx)
 
 #### 4. Basic Python
  * ***Basic Python Knowledge for FRC***
    * Output with print()
    * Input with input()
    * Loops
    * If/else
    * Basic Data Structures
      * Lists
      * Dictionaries
      * Tuples
      * Sets
      * Basic methods for these
    * Functions
    * Try/Except
    * String methods
    * Other Basic Methods
    * File IO
  * ***Demonstrate Python Knowledge by Doing the following:***
  * ***Basic Python Learning Links/Options***
    * With Python, there is no shortage of online resources and tutorials to learn with. The links I've included here are ones that I've used, but there are many more options than what is listed.
    * I have used the following books to teach Python to various groups:
      * *[Invent Your Own Computer Games with Python](https://inventwithpython.com/invent4thed/)*
      * *[Python Crash Course](https://nostarch.com/python-crash-course-3rd-edition)*
      * *[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)*
    * Youtube Tutorials and useful channels:
      * [Tech with Tim](https://www.youtube.com/c/TechWithTim)
 
 #### 5. Intermediate/Advanced Python
  * Object Oriented Programming with Python
  * *args and **kwargs
  * Dunder methods
  * Generators
  * List comprehensions
  * Decorators
  * Testing
  * PIP
  * [PEP8](https://peps.python.org/pep-0008/)/[General Python Programming Style](https://docs.python-guide.org/writing/style/)
  * PyDoc
 
 #### 6. Installing robotpy

* Robot Programming
  * Motors
  * Encoders
  * Sensors
  * Pneumatics
* PID
* Network Tables
* Simulation
* Unit Testing
* Vision
  * Apriltags
  * Limelight
* Scouting
  * The Blue Alliance
  * Python request and json modules
 
 ### Useful Links
* [WPILIB](https://docs.wpilib.org/en/stable/)
* [robotpy](https://robotpy.readthedocs.io/en/stable/#)
* https://www.youtube.com/watch?v=p15xzjzR9j0
* https://www.youtube.com/watch?v=27u8xHqLMZE
* https://python-course.eu/

