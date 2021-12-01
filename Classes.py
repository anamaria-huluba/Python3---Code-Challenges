# 1. Setting Up Our Robot

# Let’s begin by creating the class for our robot. We will begin by setting up the instance variables to keep track of important data related to the robot. 

# Here are the steps we need to do:
# Create a new class called DriveBot
# Set up a basic constructor (no parameters needed)
# Initialize three instance variables within our constructor which all default to 0: motor_speed, 
# direction, and sensor_range

# Define the DriveBot class here!
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

robot_1 = DriveBot()
robot_1.motor_speed = 30
robot_1.direction = 90
robot_1.sensor_range = 25

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# This shows the structure of a simple class which only contains instance variables. The three instance variables are set to 0 for now, which means that they can only be 
# changed by manually by accessing them from an object of the DriveBot class.

# 2. Adding Robot Logic

# Now we want to add some logic to our robot. It would be very useful to be able to control our robot, say we are going to create a control_bot method which changes the speed 
# and direction. We are also going to create a method called adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles. 

# Here are the steps:
# Define a function within the DriveBot class which accepts two additional parameters: one for a new 
# speed and one for a new direction
# Replace the instance variables for speed and direction with the input parameters
# Define another function called adjust_sensor which accepts one additional parameter
# Replace the instance variable sensor_range with the input parameter

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 10
robot_1.direction = 180
robot_1.sensor_range = 20

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

#These two methods were added inside of the DriveBot class. They are used to replace the instance variables with new values from the input parameters. We use self.variable_name 
# to access a certain instance variable within the class.

# 3. Enhanced Constructor

# It can be tedious manually setting the values for each instance variable after we have created an object from the DriveBot class. We can enhance our constructor to 
# automatically assign the values we provide to the instance variables. Instead of taking zero parameters, we are going to make the constructor take three parameters. 

# Here is what we need to do:
# Modify the constructor to take three parameters (in addition to self): one for motor_speed, one 
# for direction, and one for sensor_range
# For the first parameter, make the default value 0
# For the second parameter, make the default value 180
# For the third parameter, make the default value 10
# Within the constructor, replace the instance variables with the variables from the input parameters

class DriveBot:
    # Updated constructor!
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# robot_2 here!
robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

# This upgraded constructor includes input parameters as well as default values for those parameters. This means that if no value is provided for those parameters, then the 
# value they are set equal to will be used. Here are some examples of different ways I used the constructor:

# sensor_range defaults to 10
robot_2 = DriveBot(10, 270) 
 
# direction defaults to 180
robot_2 = DriveBot(sensor_range = 20, motor_speed = 45) 
 
# direction defaults to 180 and sensor_range defaults to 10
robot_2 = DriveBot(50) 
 
# all default values are used
robot_2 = DriveBot() 
 
# no default values are used
robot_2 = DriveBot(18, 95, 30)

# 4. Controlling Them All

# We want to add a new feature which allows the use to control multiple robots at once. The robots should be able to all have the same latitude and longitude GPS destination 
# coordinates as well as a setting for disabling them all called all_disabled. We can accomplish this using class variables. 

# Here is how we can do it:
# Create a new class variable within the DriveBot class called all_disabled and set it equal to False
# Create a new class variable within the DriveBot class called latitude and set it equal to -999999
# Create a new class variable within the DriveBot class called longitude and set it equal to -999999
# Outside of the class, test the class variables by setting the longitude of all robots to 50.0, the 
# latitude to -50.0 and all_disabled to True

class DriveBot:
  # Created the class variables here!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# I placed the class variables at the top of the class outside of the constructor. These variables can be accessed within the scope of the entire class. This means that the 
# class variables contained within every object from the DriveBot class will change if we modify the class variable directly. 
# 
# Here is an example of how to change each of these class variables:
# Changed latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.longitude = -79.98553
DriveBot.latitude = 40.60793
DriveBot.all_disabled = False

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

# 5. Identifying Robots

# In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot when it is created. If we create five robots in a row, we want 
# the IDs of each robot to be 1, 2, 3, 4, and 5 respectively. This can be accomplished by using a class variable counter which increments and is assigned to an instance variable for the ID whenever the constructor is called. 

# Here are the steps:
# Create a new class variable in the DriveBot class called robot_count
# In the constructor, increment the robot_count by 1
# After incrementing the value, assign the value of robot_count to a new instance variable called id.

class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    # Created a counter to keep track of how many robots were created
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assigned an `id` to the robot when it is constructed by incrementing the counter and assigning 
        # the value to `id`
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# print(robot_1.id)
# print(robot_2.id)
# print(robot_3.id)

# The final modifications to this class can be seen at the top of the class and in the constructor. We use a class variable to keep track of the total number of robots. This 
# information is shared across all robot objects we create from the class. Every time a robot object is created, the constructor is called and the count is incremented. Each 
# robot has an instance variable for id which is local to that robot object. This is assigned at the time of construction and stores what the count was at that time.

# Python Code Challenges: Classes (Advanced)

#You have created a robotics company which began with four-wheeled driving robots, but you are now expanding the technology to include bipedal robots. Since a lot of robotic 
# logic already exists from the driving robot, we can modularize the robot class structure using object oriented programming concepts such as inheritance. These five advanced 
# challenge problems will test your knowledge of classes and interactions between multiple classes.

# 1. Robot Inheritance

# The generic variables and methods have been placed into a Robot class for you. You will need to create two new classes. One for DriveBot and one for WalkBot. Both of these should inherit from the Robot 
# class. The constructor for the DriveBot will be essentially the same as the superclass constructor, but the WalkBot constructor will include an extra parameter for an instance variable called step_length. 

# Here is what we need to do:
# Create a new class called DriveBot which inherits from the Robot class
# Call the superclass constructor within the DriveBot constructor but pass motor_speed as the parameter for speed in the super class
# Create a new class called WalkBot which inherits from the Robot class
# Add another parameter to the WalkBot constructor for step_length which defaults to 5
# Call the superclass constructor within the constructor for the WalkBot class
# Assign the input parameter for step_length to a new instance variable for step_length

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

# Created the DriveBot class here!
class DriveBot(Robot):
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

# Created the WalkBot class here!
class WalkBot(Robot):
    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 90, 15, 10)

print(robot_2.id)
# reurns: 2
print(robot_3.step_length)
# reurns: 10
print(robot_1.speed)
# reurns: 0

# By placing Robot in the parentheses next to the two new classes, we cause them to inherit from the Robot class. We can use super().__init__(self, param_1, param_2, etc...) 
# to call the superclass constructor. This will use the constructor in the Robot class to assign the values to the instance variables. Any new changes can then be added afterward.

# 2. Using The Superclass

# There was an issue discovered when testing the WalkBot prototypes. In some cases, the robots were 
# incorrectly detecting their own legs as obstacles. To overcome this, we need to modify our adjust_sensor 
# method to reset obstacle_found to False and step_length to 5 while also using the original logic from 
# the superclass. 

# Here are the steps:
# Override the adjust_sensor method in the WalkBot class by re-defining it in that class.
# Call the superclass version of the method within adjust_sensor
# Add a line of code to set obstacle_found to False
# Add a line of code to set step_length to 5

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)


class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    # Overrided the adjust_sensor method here!
    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

robot_walk = WalkBot(60, 90, 10, 15)
robot_walk.obstacle_found = True
print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)

# Call the overridden adjust_sensor method here!

robot_walk.adjust_sensor(25)

print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)

# As you can see, in order to override the method, we can re-define it again with the same name. You can use super().method_name() in order to call the superclass version of the method.

# 3. Conditional Superclass Logic

# Since the bipedal robot is a bit less stable, the obstacle avoidance must be more delicate. Because of this, we want to call the superclass method for avoiding obstacles 
# within the bipedal robot class if the steps per minute are less than or equal to 60, otherwise the WalkBot should only rotate 90 degrees clockwise and set obstacle_found to 
# False. In either case, we need to half the robot’s speed and step_length in order to slow it down during the turn. 

# Here are the steps we need to do:
# Within the WalkBot class, override the method called avoid_obstacles by re-defining it in the class.
# If an obstacle was found
# If the speed if less than or equal to 60
# Call the superclass version of the method
# Otherwise add 90 to the WalkBot‘s direction. If the new direction is greater than 360, it should loop 
# back around to be between 0 and 360. For example, if the new direction is 370, it should really be 10. 
# (hint: use modulo to do this!)
# You should also set obstacle_found to False is the speed was over 60.
# Regardless of whether an obstacle was found, half the speed and the step_length of the robot

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)


class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

   # Override the avoid_obstacles method here!
    def avoid_obstacles(self):
      if(self.obstacle_found):
        if(self.speed <= 60):
           super().avoid_obstacles()
        else:
           self.direction = (self.direction + 90) % 360
           self.obstacle_found = False
        self.speed /= 2
        self.step_length /= 2

robot_1 = WalkBot(150, 0, 10, 10)
robot_1.obstacle_found = True
robot_1.avoid_obstacles()

print(robot_1.direction)
# returns: 90
print(robot_1.speed)
# returns: 75.0
print(robot_1.step_length)
# returns: 5.0

robot_2 = WalkBot(60, 0, 20, 40)
robot_2.obstacle_found = True
robot_2.avoid_obstacles()

print(robot_2.direction)
# returns: 180
print(robot_2.speed)
# returns: 30/0
print(robot_2.step_length)
# returns: 20.0

# This method shows how the superclass method can be called conditionally. In this case it depends on the speed of the robot and if an obstacle was found. We use modulus when 
# rotating the robot to loop back past 0 if we go over 360 degrees. This is because the robot would have made a full circle.

# 4. Overriding Dunder Methods

# Let’s add an easy way to increase and decrease our speed as well as some other attributes depending on the type of robot. For the Robot class, we want to increase and 
# decrease the speed using the + and - operators. For the DriveBot class, we want to adjust the speed and sensor_range with those operators. Lastly, for the WalkBot class, 
# we want to adjust the speed and step_length with those operators. We can override the dunder methods which represent those operations and call the superclass version of 
# those dunder methods. 

# Here are the steps:
# In the Robot class, override the + operator to add to the speed of the robot
# In the Robot class, override the - operator to subtract from the speed of the robot
# In the DriveBot class, override the + operator to call the superclass version of the operator as well 
# as add to the sensor_range of the robot
# In the DriveBot class, override the - operator to call the superclass version of the operator as well 
# as subtract from the sensor_range of the robot
# In the WalkBot class, override the + operator to call the superclass version of the operator as well 
# as add half of the value on the right side of the operator to the step_length of the robot
# In the WalkBot class, override the - operator to call the superclass version of the operator as well 
# as subtract half of the value on the right side of the operator from the step_length of the robot

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False
  
  # Overrided the + and - operations here!

    def __add__(self, value):
        self.speed += value
 
    def __sub__(self, value):
        self.speed -= value

class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)
    
    # Overrided the + and - operations here while using those dunder methods from the superclass!

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value
 
    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value

class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

    def avoid_obstacles(self):
       if(self.obstacle_found):
           if(self.speed <= 60):
               super().avoid_obstacles()
           else:
               self.direction = (self.direction + 90) % 360
               self.obstacle_found = False
           self.speed /= 2
           self.step_length /= 2

    # Overrided the + and - operations here while using those dunder methods from the superclass!

    def __add__(self, value):
       super().__add__(value)
       self.step_length += value / 2
 
    def __sub__(self, value):
       super().__sub__(value)
       self.step_length -= value / 2

robot_1 = DriveBot()
robot_2 = WalkBot()

robot_1 + 20
robot_1 - 10
robot_2 + 10
robot_2 - 5

print(robot_1.speed)
# returns: 10
print(robot_1.sensor_range)
# returns: 20
print(robot_2.speed)
# returns: 5
print(robot_2.step_length)
# returns: 7.5

# The above code only shows the dunder methods which were added to each class. The child classes both override those operations as well. This shows how superclass versions of 
# dunder methods can also be called from a child class.

# 5. Prevent A Robot Takeover

# Finally, we are going to make some last additions to our bipedal robot and test it out. Your customers are worried that your new robot model might become sentient when 
# controlled in large numbers. To prevent this, program the bipedal robots so that if five WalkBots are created when there are already at least 5 DriveBots (causing 10 or more 
# total bots) then disable all robots. 

# This is what you need to do:
# Create a new class variable in the WalkBot class to count the number of WalkBot instances
# In the constructor for the WalkBot, increment the counter by 1
# Also, in the constructor, check if the number of total Robots (from the superclass) is greater than or equal to 10 and if the number of WalkBots is greater than or equal to 5.
# If so, disable all robots

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

    def avoid_obstacles(self):
       if(self.obstacle_found):
           if(self.speed <= 60):
               super().avoid_obstacles()
           else:
               self.direction = (self.direction + 90) % 360
               self.obstacle_found = False
           self.speed /= 2
           self.step_length /= 2

    def __add__(self, value):
       super().__add__(value)
       self.step_length += value / 2

    def __sub__(self, value):
       super().__sub__(value)
       self.step_length -= value / 2

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)

# Here is the updated constructor and class variable for the WalkBot class:

class WalkBot(Robot):
    walk_bot_count = 0
 
    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length
 
        WalkBot.walk_bot_count += 1
        if(WalkBot.walk_bot_count >= 5 and Robot.robot_count >= 10):
           Robot.all_disabled = True

# This modification uses a similar method of counting from the Robot class, but it uses a separate counter to only track the number of WalkBots. Whenever a new WalkBot is 
# created, the constructor is called and the two counts are checked. If the total number of robots is at least 10 and the number of WalkBots reaches 5 then all robots are disabled.

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value

class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value

class WalkBot(Robot):
    walk_bot_count = 0

    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

        WalkBot.walk_bot_count += 1
        if(WalkBot.walk_bot_count >= 5 and Robot.robot_count >= 10):
           Robot.all_disabled = True

    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

    def avoid_obstacles(self):
       if(self.obstacle_found):
           if(self.speed <= 60):
               super().avoid_obstacles()
           else:
               self.direction = (self.direction + 90) % 360
               self.obstacle_found = False
           self.speed /= 2
           self.step_length /= 2

    def __add__(self, value):
       super().__add__(value)
       self.step_length += value / 2

    def __sub__(self, value):
       super().__sub__(value)
       self.step_length -= value / 2

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled) 
# returns: False
robot_10 = WalkBot()
print(Robot.all_disabled)
# returns: False

# This modification uses a similar method of counting from the Robot class, but it uses a separate counter to only track the number of WalkBots. Whenever a new WalkBot is 
# created, the constructor is called and the two counts are checked. If the total number of robots is at least 10 and the number of WalkBots reaches 5 then all robots are disabled.



