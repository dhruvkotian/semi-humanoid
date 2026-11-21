from adafruit_servokit import ServoKit 
import time

# Define the I2C bus number (for Raspberry Pi 5, it's typically 1)
i2c_bus = 1

# Create a ServoKit instance with 16 channels (PCA9685)
kit = ServoKit(channels=16, i2c_bus=i2c_bus)

# Function to write an angle to the servo on the specified channel
def write_angle_to_servo(channel, angle):
    # Set the angle for the specified channel
    kit.servo[channel].angle = angle

def main():
    # Example usage in the main function
    # Rotate the servo on channel 0 to 90 degrees
    write_angle_to_servo(0, 90)
    time.sleep(1)  # Hold position for 1 second

    # Rotate the servo on channel 0 to 45 degrees
    write_angle_to_servo(0, 45)
    time.sleep(1)  # Hold position for 1 second

    # Rotate the servo on channel 0 to 135 degrees
    write_angle_to_servo(0, 135)
    time.sleep(1)  # Hold position for 1 second

if __name__ == "__main__":
    main()
