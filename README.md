# TBS Robotics Motor Control with Python
TBS Robotics Motor Control with Python
## Preparation
- Laptop computer (or Raspberry Pi, JETSON Nano, etc. with monitor, keyboard and mouse)
- USB cable
- Servo motor with known ID (from last activity)
- U2D2 and U2D2 power hub
- 8x AA battery pack
- SDK from Robotis
- Python3.x installed
- Program editor, such as Atom or VSCode
  - https://atom.io/
  - https://code.visualstudio.com/download 
## Find Software Development Kit (SDK)
- Document: https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/
- Download
  - Option 1: Download link, and extract at desired directory
  - Option 2: Github at linux or unix (MacOS) terminal prompt
    - Change to the desired directory
    - Use git command
```
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
```
- MATLAB is the other fun interactive script option if you are interested
## Install Python SDK
- Windows: https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_windows/#python-windows
- Linux and MacOS at terminal: https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/#python-linux
```
sudo python setup.py install
```
or
```
sudo python3 setup.py install
```
- `sudo` command will ask you superuser password for installation
- Make sure to run python3.x for install. Please do not mix up with python installation version and python you will run. If they are different, python will not be able to find the SDK library.
- Use `which python` or `which python3` to know the path to python
- `python --version` or `python3 --version` will print the version
## Run a test program
- Connect servo motor, U2D2, U2D2 power hub, and 8x AA battery pack
- Find USB port for U2D2 connection
- `ls /dev/*` to find `ttyUSBx` for U2D2 connection. The `ttyUSBx` will appear when USB is connected and disappear when disconnected.
- Use program editor to modify the code first
- Set motor ID and communication speed set with Dynamixel Wizard
## How to set a target position
- Set up position first
- Then start - Torque enable
## How to run at constant speed
- Start first - Torque enable
```dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, self.DXL1_ID, self.ADDR_TORQUE_ENABLE, self.TORQUE_ENABLE)```
- Then set speed
```dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, self.DXL1_ID, self.ADDR_GOAL_VELOCITY, self.speedMotor1 * self.DXL1_orientation)```
## Group write for multiple motors

