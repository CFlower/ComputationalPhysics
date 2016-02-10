'''
Created on Feb 8, 2016

@author: Chris
'''
import math
import matplotlib.pyplot as plt


xvalues = []
yvalues = [] #define some arrays to hold the values as we go through Timez 
vxvalues = []
vyvalues = [] #couple of arrays to store the velocities 
timevalues = []
#set some constants
g = 9.81 #meters per second second
C = 1/2 #drag constant
p = 1.29 #density of air... rho in KG/m^3
A = .0014  #cross sectional area of golf ball in m^2
pi = math.pi #define pi for ease of access

#USER CONTROL 1 = ON;  0 = OFF
drag = 1 
dimples = 1
spin = 1

#Other user defined input
dt = .001 #define some discrete timestep for the approximation to go by - seconds
theta = 45.0 #angle of launch , degrees
x0 = 0.0
y0 = 0.0 #set initial position values 
v0 = 45.0 #initial velocity of the golfball in m/s
vx0 = v0 * math.cos(theta * 2*pi/360)
vy0 = v0 * math.sin(theta * 2*pi/360) #allows for computation in radians rather than degs
m = 46.0 #mass of the ball in grams
#variables for the magnus force terms
s0 = 1
w = -11.5 #omega is the angular velocity in radians/s? These two values result in 0.25

#create variables used for computation
x = x0
y = y0
vx = vx0
vy = vy0
#create temporary clone variables:
tempx = x0
tempy = y0
tempvx = vx0
tempvy = vy0

#add the original positions and velocities to the arrays that will store the data...
xvalues.append(x)
yvalues.append(y)
vxvalues.append(vx)
vyvalues.append(vy)
timevalues.append(0) #add t=0 datapoint to correspond to x0 y0 etc


while (y >= 0): 
    
    v = math.sqrt(tempvx*tempvx + tempvy*tempvy) #calculates the total velocity of current frame
    
    if ((v < 14.0)&(dimples!=0)):
        C = 1/2
    elif ((v>14.0)&(dimples!=0)):
        C = 7.0/v
        
    y = tempy + tempvy*dt
    if (y<=0): #should stop it from adding a single negative value at the end?
        break #this is done FIRST because if we want to trigger an exit we will maintain the same dimensions
    
    yvalues.append(y)
    x = tempx + tempvx*dt
    xvalues.append(x)
    vx = tempvx - drag*(((C*p*1000*A*v*tempvx)/m)*dt) - spin*(s0*w*tempvy/m*dt) #nothing for Dimples yet!!I have a feeling something is up with the v here... seems to fall too soon...
    vxvalues.append(vx)
    vy = tempvy-g*dt - drag*(((C*p*1000*A*v*tempvy)/m)*dt) + spin*(s0*w*tempvx/m*dt)
    vyvalues.append(vy)

    #now, all of the non-temp variables should have their new values calculated from the temp values
    #so we update temp values for the next iteration through
    tempx = x
    tempy = y 
    tempvx = vx 
    tempvy = vy
    
    #t = t+dt
    #timevalues.append(t) #this is done last to be consistent... but might screw up the last iteration if the loop is existed before the last t is added!
    
plt.plot(xvalues,yvalues, label='Trajectory of Golf Ball') #plots the exact data
plt.ylabel('Height (meters)')
plt.xlabel('Distance (meters)')
plt.title('Trajectory of Golf Ball ')
#legend = plt.legend(loc='upper center', shadow=True)
plt.show()


#Note to self... DIMPLES arent the same as SPIN! Figure this out and make an adjustment... should be simple to add :)


