import math
import numpy as np

l1 = 96
l2 = 58
r1 = math.radians(40)
r2 = math.radians(30)

T1 = np.array([
    [math.cos(r1), -math.sin(r1), l1 * math.cos(r1)],
    [math.sin(r1),  math.cos(r1), l1 * math.sin(r1)],
    [0, 0, 1]
])

T2 = np.array([
    [math.cos(r2), -math.sin(r2), l2 * math.cos(r2)],
    [math.sin(r2),  math.cos(r2), l2 * math.sin(r2)],
    [0, 0, 1]
])

T_total = np.dot(T1, T2)

x = T_total[0, 2]
y = T_total[1, 2]

print("Posisi end effector:")
print("x =", round(x, 2), "y =", round(y, 2))

print("\nMatriks transformasi total:")
print(np.round(T_total, 3))