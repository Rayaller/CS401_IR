

<p align="right">ID: 12110525</p>
<p align="right">Name: 朱家骆</p>

## Question 1

- (a) Imagine you want your robot to perform navigation tasks, which approach would you choose?
- (b) What are the benefits of the behavior based paradigm?
- (c) Which approaches will win in the long run?

## Answer 1

**(a)**  There are typically two main approaches
- **Map-based navigation**: This approach requires the robot to have a map of the environment. The robot uses sensor data to determine its location on the map and then plans a path to the goal. This approach works well in known environments but may struggle in unknown or dynamically changing environments.
- **Behavior-based navigation**: This approach does not require a map and instead relies on the robot’s perception and reaction capabilities. The robot decides on the next action based on the current perception data. This approach works well in unknown or dynamically changing environments but may not find the optimal path.  


**(b)** The behavior-based paradigm offers several advantages:
- **Modularity**: The system is composed of separate behaviors, making it easier to modify or extend specific functionalities without affecting the entire system.
- **Robustness**: The robot can handle unforeseen situations by dynamically selecting appropriate behaviors based on sensory input.
- **Real-Time Responsiveness**: Behavior-based systems react quickly to changing conditions, which is essential for navigation tasks.


**(c)** Behavior-based navigation approach is advantageous in dynamic or unknown environments. If the robot needs to adapt to changes in the environment or handle unexpected obstacles, a behavior-based approach could prove more successful over time


## Question 2

- (a) How to generate uniform, perpendicular, attractive, repulse, tangential forces for a robot and obstacles with known positions? Provide related mathematical formulas.
- (b) Please simulate the motions of a robot with the given force fields from the following figure.

## Answer 2

### Part (a)

#### **uniform**

For the uniform force filed, the direction of the force remains as a constant, which is  given by the force vector
$$
\vec{F}=\vec{vector}
$$
the unit vector of the force is
$$
\vec{v}=\frac{\vec{F}}{|\vec{F}|}
$$
#### **perpendicular**

The state point of the robot is $\vec{p_0}=(x_0, y_0)$

The direction of perpendicular force is perpendicular to the line of the obstacles, $\vec{p_1}=(x_1, y_1)$ and $\vec{p_2}=(x_2, y_2)$. In other worlds,  The direction is parallel to the normal vector of the line.

line vector: $\vec{l}=\vec{p_1}-\vec{p_2}=(x_1-x_2,y_1-y_2)$

normal vector: $\vec{n_0}=(y_1-y_2,x_2-x_1)$, which satisfying $\vec{l} \cdot \vec{n_0}=0$

while the unit normal vector could be describe as
$$
\vec{n}=\frac{\vec{n_0}}{|\vec{n_0}|}
$$
which is parallel to the force as well, either at the same direction or at the opposite direction. To determine this,  we need calculate two vectors, the first is the projection point of the state point of the robot $\vec{v_r}$, and the distance vector of the line and the original point $\vec{v_l}$
$$
\vec{v_r} =\vec{p_0} \cdot \vec{n} \cdot \vec{n}
$$
similarly
$$
\vec{v_l} =\vec{p_1} \cdot \vec{n} \cdot \vec{n}
$$
the vector from the obstacle line point to the robot could be describe as
$$
\vec{v_0}=\vec{v_r}-\vec{v_l}
$$
the unit vector of the force is
$$
\vec{v}=\frac{\vec{v_0}}{|\vec{v_0}|}
$$
#### **attractive**

The state point of the robot is $\vec{p_0}=(x_0, y_0)$， while the attractive point is $\vec{p_1}=(x_1, y_1)$
The distance vector from the robot to the attractive point
$$
\vec{v_0}=\vec{p_1}-\vec{p_0}
$$
the unit vector of the force is 
$$
\vec{v}=\frac{\vec{v_0}}{|\vec{v_0}|}
$$

#### **repulse**

The state point of the robot is $\vec{p_0}=(x_0, y_0)$， while the repulse point  is $\vec{p_1}=(x_1, y_1)$
The distance vector from the repulse point to the robot
$$
\vec{v_0}=\vec{p_0}-\vec{p_1}
$$

the unit vector of the force is 
$$
\vec{v}=\frac{\vec{v_0}}{|\vec{v_0}|}
$$

#### **tangential**
The state point of the robot is $\vec{p_0}=(x_0, y_0)$， while the point  is $\vec{p_1}=(x_1, y_1)$
The distance vector from the point to the robot
$$
\vec{v_0}=\vec{p_0}-\vec{p_1}=(x_0-x_1, y_0-y_1)
$$
the vector that vertical to the distance vector satisfying $\vec{v_1} \cdot {\vec{v_0} = 0}$, thus
$$
\vec{v_1}=(y_0-y_1, x_1-x_0)
$$

the unit vector of the force is 
$$
\vec{v}=\frac{\vec{v_1}}{|\vec{v_1}|}
$$

### Part (b)

The motions of a robot with the given force fields is shown below 

#### uniform
![[uniform.gif|300]]
#### perpendicular
![[perpendicular.gif|300]]

#### attractive
![[attractive.gif|300]]

#### repulse
![[repulsive.gif|300]]

#### tangential
![[tangential.gif|300]]


## Question 3 - Extra Credit

Simulate a robot can reach the goal without sticking into a local trap. Provide codes and plots of simulation results. You can follow the instruction to complete the file *question3_run.py* in the source folder to generate the animation as shown below:

## Answer 3

In question 2, we make the magnitude of every force to be the unit one. In this part, vector superposition is involved, so it is the essential to determine the  magnitude vectors. 

Besides, each of the three walls has its length instead of be infinite, using the perpendicular force as its force may cause unexpected situation. So I use the repulse force between the robot and the closest point between the wall and the robot to replace the perpendicular force.

Moreover, when the robot getting out of the shape of "⊐",  it will never get back into it, so I set the force of the first wall as well as the second wall to be zero at that time.

At other time, the magnitude force of each part are

wall 1: $F_1=1/(distance(p_0, ClosestPoint(wall_1,p_0)))^2$
wall 2: $F_2=1/(distance(p_0, ClosestPoint(wall_2,p_0)))^2$
wall 3: $F_3=1/(distance(p_0, ClosestPoint(wall_3,p_0)))^2$
goal: $F_4 = 1/(distance(p_0,goal))$

the sum of those force $\vec{F}=\vec{F_1}+\vec{F_2}+\vec{F_3}+\vec{F_4}$

the unit vector of the force $\vec{v}=\frac{\vec{F}}{|\vec{F}|}$

The motions of a robot with the given force fields is shown below 
![[potential_field.gif|400]]