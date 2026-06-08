import sys
import math

prev_x = None
prev_y = None
boost_used = False

# game loop
while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if prev_x is None:
        vx = 0
        vy = 0
    else:
        vx = x - prev_x
        vy = y - prev_y
    
    prev_x = x
    prev_y = y

    k = 3.0
    aim_x = next_checkpoint_x - int(vx * k)
    aim_y = next_checkpoint_y - int(vy * k)

    checkpoint_angle_deg = math.degrees(math.atan2(next_checkpoint_y - y, next_checkpoint_x - x))
    pod_facing_deg = checkpoint_angle_deg - next_checkpoint_angle
    
    aim_angle_deg = math.degrees(math.atan2(aim_y - y, aim_x - x))
    new_relative_angle = aim_angle_deg - pod_facing_deg
    new_relative_angle = (new_relative_angle + 180) % 360 - 180
    
    thrust = 100
    abs_angle = abs(new_relative_angle)

    if abs_angle > 90:
        thrust = 0
    elif abs_angle > 45:
        thrust = 45
    elif next_checkpoint_dist < 2200 and abs_angle > 15:
        thrust = 15

    if not boost_used and next_checkpoint_dist > 5000 and abs(next_checkpoint_angle) < 5:
        action = f"{aim_x} {aim_y} BOOST"
        boost_used = True
    else:
        action = f"{aim_x} {aim_y} {thrust}"
        
    print(action)
