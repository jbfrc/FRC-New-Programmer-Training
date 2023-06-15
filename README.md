<h1>Ozone Robotics - New Programming Student Training</h1>

Last Updated: June 15, 2023

<h2>Overview of Training Topics</h2>

This is a list of topics to train new FRC robotics programming students. It's obviously not complete but will cover the following when completed:

* Basic robot safety issues
* Introduction to FRC hardware and wiring
* Fundamentals of Python
* More advanced Python topics (particulary OOP)
* robotpy
* Introduction to computer vision
* Scouting (and in particular using Python to pull & analyze data)

New programming students are also required to take the basic handtools, mechanical, and electrical training in the preseason.

## Detailed List of Training Topics
#### 1. Background knowledge. Complete the following training during the preseason:
* Basic electrical
* Basic hand tools
* Basic mechanical
#### 2. Safety (Focused a lot on issues that programmers would deal with while testing code)
* ***General Knowledge***
   * [Battery Safety](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-battery.html#battery-safety-handling)
     * How to safely carry a battery
     * The cables are not a handle!
     * What happens if battery is dropped?
     * What about a leaking battery?
   * [Long hair must be tied back, no dangling jewelry, no ties, clothing should fit properly to avoid getting caught in the robot, etc.](https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/team-resources/safety/2023/2023-Safety-Manual.pdf#%5B%7B%22num%22%3A29%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C70%2C487%2C0%5D)
   * [Lifting the robot](https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/team-resources/safety/2023/2023-Safety-Manual.pdf#%5B%7B%22num%22%3A24%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C70%2C691%2C0%5D)
   * Assume anything designed to shoot/throw an object can do that during testing and avoid being in front of it.
   * Assume that a robot will move in a direction or way you don't expect.
     * Keep distance and barrier between you and robot.
     * Be prepared to emergency stop the robot
   * Assume any motor can move in ways you aren't expecting
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

#### 3. Robot Hardware - Part 1
* ***General Knowledge***
  * roboRIO
    * Know how to connect via USB and with the radio.
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
  * [CAN Bus](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html)
    * Understand how the CAN bus is wired
    * Where are the ends of the CAN bus connected in a robot?
    * What happens if there is a break in the CAN bus?
    * How do you identify the CAN bus wires?
  * Motors & Motor Controllers
    * Be able to identify common FRC motors
      * [Beginner Motors for FRC](https://www.youtube.com/watch?v=vWKKIhUcTzw)
      * 
    * Know what motor controllers can be used with motors
    * Explain difference between brushed and brushless motors
    * Know if these common motors are brushed or brushless
    * What are advantages/disadvantage of brushed/brushless motors?
    * [Talon SRX LED Codes](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html#talon-srx-victor-spx-talon-fx-motor-controllers)
    * [Spark MAX LED Codes](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html#spark-max-motor-controller)
  * Other hardware on the robot:
    * [Power Distribution Panel (PDP)](https://store.ctr-electronics.com/power-distribution-panel/)/[Power Distribution Hub(PDH)](https://www.revrobotics.com/rev-11-1850/)
    * [Voltage Regulator Module (VRM)](https://www.andymark.com/products/voltage-regulator-module)
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
  * [Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
#### 4. Robot Hardware - Part 2
  * ***General Knowledge***
    * [Drivetrains](
https://youtu.be/JTZ31lpMkfA)
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
    * This needs to be developed more
  * ***Additional Robot Hardware Links***
    * Drivetrains
      * [Intro to FRC Mechanisms](https://www.youtube.com/watch?v=JTZ31lpMkfA)
      * [REV Drivetrain Info](https://docs.revrobotics.com/frc-kickoff-concepts/charged-up-2023/drivetrains)
      * [What Does an FRC Drivetrain Do?](https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/team-resources/behind-the-lines/2017/btl-s03e04-drivetrains.pptx)
 
#### 5. Basic Python 
#### 6. Intermediate/Advanced Python
#### 7. Installing robotpy
#### 8. Robot Programming - Part 1
#### 9. PID
#### 10. Robot Programming - Part 2
#### 11. Introduction to Computer Vision
#### 12. Scouting
 
 ### Useful Links
* [WPILIB](https://docs.wpilib.org/en/stable/)
* [robotpy](https://robotpy.readthedocs.io/en/stable/#)

