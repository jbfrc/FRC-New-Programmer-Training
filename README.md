# FRC New Programming Student Python Training

Last Updated: April 28, 2023

This is a list of topics that I'm putting together to train new FRC robotics students. It's obviously not complete but will cover the following when completed:
* Basic robot safety issues
* Introduction to FRC hardware and wiring
* Fundamentals of Python
* robotpy
* Introduction to computer vision
* Scouting (and in particular using Python to pull & analyze data)

### Training Topics
1. Safety (Focused a lot on issues that programmers would deal with while testing code)
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
     * Robot Signal Light (RSL) - What do the following states indicate?
       * Off
       * On
       * On & Blinking 
   * ***Demonstrate how to do the following:***
     * Perform an emergency stop of the robot
     * Show how to safely carry a battery
     * Show how to turn on/off the robot
   * ***Robotics Safety Links***
     * [2023 FRC Safety Manual](https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/team-resources/safety/2023/2023-Safety-Manual.pdf)

 2. Basic Robot Hardware
    * ***General Knowledge***
      * roboRIO
        * What IP address(es) does the RIO have?
        * What do the LED status lights mean?
        * Identify and know what the various ports are used for:
          * Power Connector
          * Ethernet
          * USB
          * DIO
          * PWM
          * CAN Bus
        * How do you update the image?
        * How do you update the team number?
        * Why is it important to have the team number correct?
      * CAN Bus
        * Understand how the CAN bus is wired
        * Where are the ends of the CAN bus connected in a robot?
        * What happens if there is a break in the CAN bus?
        * How do you identify the CAN bus wires?
      * Motors
        * Be able to identify common FRC motors
        * Know what motor controllers can be used with motors
        * Explain difference between brushed and brushless motors
        * Know if these common motors are brushed or brushless
      * Other hardware on the robot:
        * Power Distribution Panel (PDP)/Power Distribution Hub(PDH)
        * Voltage Regulator Module (VRM)
        * Pneumatics Control Module (PCM)
        * Radio
        * Pigeon
      * Driver Station
      * Sensors
    * ***Demonstrate how to do the following:***
      * roboRIO
        * Connect to the roboRIO via USB and demonstrate that robot communication has been established
        * Connect to the roboRIO via the radio (assuming the test bench has a radio) and demonstrate that robot communication has been established
        * Update the image
        * Update the team number
      * Update firmware:
        * Spark Max Motor Controller
        * Talson SRX Motor Controller
      * Show how to configure a Spark Max motor controller to use a brushed or brushless motor
      * CAN Bus
        * Identify the wires used in the CAN Bus
        * Check/Update CAN IDs with
          * Phoenix Tuner
          * REV Hardware Client
       * Deploy sample code to the robot and demonstrate that the code is executing properly
    * ***Robot Hardware Links***
      * [WPILIB roboRIO Introduction](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-introduction.html)
      * [roboRIO User Manual](https://www.ni.com/docs/en-US/bundle/roborio-20-umanual/page/umanual.html)
      * [Brushed Vs Brushless Motor - What Is The Difference?](https://www.youtube.com/watch?v=4LW-iUehJh8)
 3. Basic Python
    * Output with print()
    * Input with input()
    * Loops
    * If/then
    * Lists
    * Dictionaries
    * Tuples
    * Sets
    * Functions
    * Try/Except
 4. Object Oriented Programming with Python
 5. Installing robotpy

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
 
 ### Useful Links
* [WPILIB](https://docs.wpilib.org/en/stable/)
* [robotpy](https://robotpy.readthedocs.io/en/stable/#)
