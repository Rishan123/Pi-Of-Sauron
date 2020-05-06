import time
import cv2
import numpy as np

r = (150, 0, 0)
y = (255,255,0)
o = (255,155,0)
b = (0, 0, 0)

def look_straight(op):
    if op == 1:
        anim1straight = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, y, y, r, r, r,
            r, r, y, b, b, y, r, r,
            r, y, b, b, b, b, y, r,
            r, r, y, b, b, y, r, r,
            r, r, r, y, y, r, r, r,
            r, r, r, r, r, r, r, r
        ]
        return anim1straight
#     elif op == 2:
#         anim2straight = [
#             r, r, r, r, y, r, r, r,
#             y, r, r, y, r, r, r, y,
#             r, y, r, r, y, r, y, r,
#             y, r, y, b, b, y, y, r,
#             r, y, b, b, b, b, r, r,
#             r, r, y, b, b, y, y, r,
#             y, y, r, y, y, r, y, y,
#             r, r, y, r, r, r, r, r
#         ]
#         return anim2straight
#     else:
#         if op == 3:
#             anim3straight = [
#                 r, r, y, r, y, r, r, r,
#                 r, y, r, y, r, r, r, r,
#                 r, y, r, r, y, r, y, r,
#                 r, r, y, b, b, y, r, y,
#                 r, y, b, b, b, b, y, r,
#                 r, r, y, b, b, y, r, r,
#                 r, y, r, y, y, r, y, r,
#                 y, r, r, r, r, y, r, r
#             ]
#             return anim3straight
#         else:
#             print('[INFO] Invalid option: ',str(op))
        
    
def look_left(op):
    if op == 1:   
        # Look left
        anim1left = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, y, y, r, r, r, r, r,
            y, b, b, y, r, r, r, r,
            b, b, b, b, y, r, r, r,
            y, b, b, y, r, r, r, r,
            r, y, y, r, r, r, r, r,
            r, r, r, r, r, r, r, r
        ]
        return anim1left
#     elif op == 2:
#         anim2left = [
#             r, r, r, r, y, r, r, r,
#             y, r, r, y, r, r, r, r,
#             r, y, r, r, y, r, y, r,
#             y, b, b, y, y, r, r, r,
#             b, b, b, b, y, y, r, r,
#             y, b, b, y, y, r, y, r,
#             y, y, r, y, y, r, r, r,
#             r, r, y, r, r, r, r, r
#         ]
#         return anim2left
#     else:
#         if op == 3:
#             anim3left = [
#                 r, r, r, r, y, r, r, r,
#                 y, r, y, y, r, y, r, r,
#                 r, y, r, r, y, r, y, r,
#                 y, b, b, y, y, r, y, r,
#                 b, b, b, b, y, y, r, y,
#                 y, b, b, y, y, r, y, r,
#                 y, r, r, y, y, y, r, y,
#                 r, y, y, r, r, r, r, r
#             ]
#             return anim3left
#         else:
#             print('[INFO] Invalid option: ',str(op))

def look_right(op):
    if op == 1:   
        # Look left
        anim1right = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, y, y, r,
            r, r, r, r, y, b, b, y,
            r, r, r, y, b, b, b, b,
            r, r, r, r, y, b, b, y,
            r, r, r, r, r, y, y, r,
            r, r, r, r, r, r, r, r
        ]
        return anim1right
#     elif op == 2:
#         anim2right = [
#             r, r, r, r, y, r, r, r,
#             y, r, r, y, r, r, r, r,
#             r, y, r, r, y, r, y, r,
#             r, r, y, y, y, b, b, y,
#             r, r, y, y, b, b, b, b,
#             r, y, r, y, y, b, b, y,
#             r, y, r, y, r, y, y, r,
#             r, r, r, r, r, r, y, r
#         ]
#         return anim2right
#     else:
#         if op == 3:
#             anim3right = [
#                 r, r, r, r, y, r, r, r,
#                 r, r, y, y, r, y, r, r,
#                 r, y, r, r, y, y, y, r,
#                 y, y, r, y, y, b, b, y,
#                 r, r, y, y, b, b, b, b,
#                 r, y, r, y, y, b, b, y,
#                 y, r, r, y, y, y, y, y,
#                 r, r, y, r, r, y, r, r
#             ]
#             return anim3right
#         else:
#             print('[INFO] Invalid option: ',str(op))