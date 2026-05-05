# Ultrasonic-Distance-Measurement-using-Raspberry-Pi
Ultrasonic distance measurement system using Raspberry Pi and HC-SR04 sensor to calculate distance based on echo time, useful for obstacle detection, robotics, and automation applications.

## Description

This project demonstrates how to measure distance using an ultrasonic sensor (HC-SR04) with Raspberry Pi. The sensor calculates the distance of an object by sending ultrasonic waves and measuring the time taken for the echo to return.

## Components Used

* Ultrasonic Sensor (HC-SR04)
* USB Cable
* Jumper Wires
* Universal IoT Trainer Kit with Raspberry Pi  
* Connecting Wires

## Software Used

* Thonny Python IDE
* Raspbian OS

## Connections

* TRIG → GPIO Pin 19 (BCM mode)
* ECHO → GPIO Pin 13 (BCM mode)
* VCC → 5V
* GND → GND

## Circuit Diagram Explanation

The ultrasonic sensor sends high-frequency sound waves through the TRIG pin. These waves reflect back after hitting an object and are received by the ECHO pin. The Raspberry Pi measures the time taken for the echo to return and calculates the distance based on this time.

## Code

[ultrasonic.py](ultrasonic.py)

## Applications

* Obstacle detection
* Robotics
* Distance measurement systems
* Smart parking systems

## Author

HimagnaMovva27
