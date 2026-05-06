# Ultrasonic Distance Measurement using Raspberry Pi

##  Objective
To measure the distance of an object using an ultrasonic sensor (HC-SR04) interfaced with Raspberry Pi by calculating the time taken for sound waves to travel.

##  Overview
This project demonstrates real-time distance measurement using ultrasonic sensing technology. The system works on the principle of **time-of-flight**, where the time taken by an ultrasonic wave to hit an object and return is used to calculate the distance.

##  Components Used
- Universal IOT Kit with Raspberry Pi
- Ultrasonic Sensor (HC-SR04)
- Jumper Wires
- USB Cable
- Connecting wires

##  Connections
- TRIG → GPIO Pin 19 (BCM mode)
- ECHO → GPIO Pin 13 (BCM mode)
- VCC → 5V
- GND → GND

##  Working Principle
1. The TRIG pin sends a short ultrasonic pulse.
2. The sound wave travels through air and reflects back after hitting an object.
3. The ECHO pin receives the reflected signal.
4. Raspberry Pi calculates the time difference between sending and receiving.
5. Distance is calculated using:

   Distance = Time × Speed of Sound / 2

##  Code
[ultrasonic.py](ultrasonic.py)

## Output
- Displays distance in centimeters on terminal  
- Provides continuous real-time distance updates  
- Accurate within typical sensor range (2cm – 400cm)
  
##  Applications
Obstacle detection systems
Robotics navigation
Distance measurement devices
Smart parking systems

##  Key Features
Real-time distance sensing
Accurate measurement using ultrasonic waves
Simple and efficient implementation

##  Concepts Used
Sensor Interfacing
Time-of-Flight Measurement
GPIO Programming
Embedded Systems

##  Author
HimagnaMovva27
