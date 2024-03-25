import numpy as np

class potential_fields:
    
    # Please complete these functions for question2, the arguments such as coefficient can be changed by your need. The return value should be a 2*1 matrix for robot to perform

    def uniform(self, vector=np.array([ [1], [0] ]), coefficient=1):
        # Please complete this function for question2
        pass
        
        return self.direction(vector)

    def perpendicular(self, line_obstacle, car_position, coefficient=1):
        # line_obstacle: [point1, point2]; point: 2*1 matrix
        # Please complete this function for question2
        pass
        
        car_position = car_position.reshape(-1, 1)

        line_vector = np.array([[line_obstacle[0][1][0] - line_obstacle[1][1][0]], 
                       [line_obstacle[1][0][0] - line_obstacle[0][0][0]]])
        
        line_vector = self.direction(line_vector)

        vector_obstacle = line_vector * np.sum(line_obstacle[0] * line_vector)
        
        vector_car = line_vector * np.sum(car_position * line_vector)

        vector = vector_car -vector_obstacle

        return self.direction(vector)
    
    def attractive(self, goal_point, car_position, coefficient=1):
        # Please complete this function for question2
        pass
        
        goal_point = goal_point.reshape(-1, 1)
        car_position = car_position.reshape(-1, 1)
        
        vector = np.array([[goal_point[0][0] - car_position[0][0]],
                   [goal_point[1][0] - car_position[1][0]]])

        return self.direction(vector)

    def repulsive(self, obstacle_point, car_position, coefficient=1):
        # Please complete this function for question2
        
        obstacle_point = obstacle_point.reshape(-1, 1)
        car_position = car_position.reshape(-1, 1)

        vector = np.array([[ - obstacle_point[0][0] + car_position[0][0]],
                   [ - obstacle_point[1][0] + car_position[1][0]]])

        return self.direction(vector)

    def tangential(self, point, car_position, coefficient=1):
        # Please complete this function for question2

        point = point.reshape(-1, 1)
        car_position = car_position.reshape(-1, 1)

        vector = np.array([[point[1][0] - car_position[1][0]],
                   [ - point[0][0] + car_position[0][0]]])


        return self.direction(vector)

    def shortest_distance_point(self, v, w, p):
        # the minimum distance between line segment vw, and point p
        # v, w, p all are 2*1 matrix

        l2 = (w - v).T @ (w - v)
        if l2 == 0:
            return np.linalg.norm( p-v )

        t = max(0, min(1, (p - v).T @ (w - v) / l2 ))
        proj_point = v + t * (w-v)
        min_distance = np.linalg.norm( p-proj_point )
        
        # return min_distance, proj_point, t
        
        return proj_point


    def direction(self, v):

        return v * (1/np.sqrt(np.sum(v * v)))

