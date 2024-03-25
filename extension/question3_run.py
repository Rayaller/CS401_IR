from ir_sim.env import EnvBase
from ir_sim.util.collision_dectection_geo import collision_seg_seg 
from potential_fields import potential_fields
from collections import namedtuple
import argparse
import numpy as np

def force(vec, line, car):
    
    distance =abs(np.sum((line[0] - car) * vec ))
    vec = vec /distance

    return vec

def distance(v1, v2):
    
    vec = v1-v2

    return np.sqrt(np.sum(vec * vec))


parser = argparse.ArgumentParser(description='The given force potential fields')
parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

point = namedtuple('point', 'x y')

env = EnvBase(world_name='question3.yaml', save_ani=args.animation)

pf = potential_fields()

line_obs = env.get_obstacle_list() 

for i in range(1000):


    ## please complete this part to solve question3 based on the force defined in question2 


    # pf_vel_0 = pf.perpendicular(env.obstacle_list[0].points, env.robot.state) 
    # pf_vel_0 = force(pf_vel_0, env.obstacle_list[0].points, env.robot.state)

    # pf_vel_1 = pf.perpendicular(env.obstacle_list[1].points, env.robot.state)
    # pf_vel_1 = force(pf_vel_1, env.obstacle_list[1].points, env.robot.state)

    # pf_vel_2 = pf.perpendicular(env.obstacle_list[2].points, env.robot.state)
    # pf_vel_2 = force(pf_vel_2, env.obstacle_list[2].points, env.robot.state)

    point_0 = pf.shortest_distance_point(env.obstacle_list[0].points[0], 
                                         env.obstacle_list[0].points[1],
                                         env.robot.state)
    
    point_1 = pf.shortest_distance_point(env.obstacle_list[1].points[0], 
                                         env.obstacle_list[1].points[1],
                                         env.robot.state)
    
    point_2 = pf.shortest_distance_point(env.obstacle_list[2].points[0], 
                                         env.obstacle_list[2].points[1],
                                         env.robot.state)
    
    pf_vel_0 = pf.repulsive(point_0, env.robot.state) / distance(point_0, env.robot.state) ** 2

    pf_vel_1 = pf.repulsive(point_1, env.robot.state) / distance(point_1, env.robot.state) ** 2

    pf_vel_2 = pf.repulsive(point_2, env.robot.state) / distance(point_0, env.robot.state) ** 2
    
    pf_vel_3 = pf.attractive(env.robot.goal, env.robot.state) / distance(env.robot.goal, env.robot.state)

    # pf_vel_3 = pf.attractive(env.robot.goal, env.robot.state) 

    if (pf_vel_0[1][0] < 0): 

        pf_vel_0 = np.array([[0], [0]])
        pf_vel_1 = np.array([[0], [0]])
        # pf_vel_2 = np.array([[0], [0]])

    pf_vel= pf_vel_0 + pf_vel_1 + pf_vel_2 + pf_vel_3

    pf_force = pf.direction(pf_vel)

    ## please complete this part to solve question3 based on the force defined in question2 

    env.step(pf_force)
    env.render(show_traj=True)

    if env.done():
        break

env.end(ani_name = 'potential_field', ani_kwargs={'subrectangles': True})