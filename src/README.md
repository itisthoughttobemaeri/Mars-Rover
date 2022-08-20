
# Mars Rover

This project implements a semplification of a rover in ROS.

## Installation

To use this package move the folder inside /catwkin_ws folder

Source the devel workspace:`$ source devel/setup.bash`

This must be done for every terminal. 

The following packages are needed: `ros-noetic-usb-cam`.


## Parameters
The mars rover can be configured with different parameters, such as the wheel radius

To see the available parameters, run `rosparam list`
To get the value of a parameter, run `rosparam get <parameter_name>`
To set the value of a parameter, run `rosparam set <parameter_name>`
To save the edited values, run `rosparam dump param.yaml`

## Launching the module
To launche the module automatically run `roslaunch mars_rover rpm_sim.launch`

## Topics
To see the available topics use `rostopic list`

## Contents of my_robot_tutorial Pkg

*/action*

Navigation file (*.action) that sets an action (point goal, result and feedback)

*/Launch*

Scripts to run the package automatically

*/scripts*

1. action_ : client/server.py : implements the action of reaching a point
2. odd_even_ : client/server.py : returns if a number is odd or even
3. turn_camera_ : client/server.py : turns the camera of the robot and shows the capture


`rosrun mars_rover <script.py>` to run a single script

## ROS was made by
Open Robotics https://www.openrobotics.org/








