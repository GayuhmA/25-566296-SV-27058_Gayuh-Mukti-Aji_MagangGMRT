import math
import numpy as np

mode = input("Forward Kinematics / Inverse Kinematics: ").strip().lower()

if mode in ["fk", "forward kinematics"]:
    n = int(input("\nMasukkan jumlah Degree of Freedom: "))

    panjang = []
    sudut = []

    for i in range(1, n+1):
        panjang_i = float(input(f"Panjang lengan ke-{i}: "))
        sudut_i = math.radians(float(input(f"Sudut ke-{i}: ")))
        panjang.append(panjang_i)
        sudut.append(sudut_i)

    T_total = np.eye(3)

    for i in range(n):
        T_i = np.array([
            [math.cos(sudut[i]), -math.sin(sudut[i]), panjang[i] * math.cos(sudut[i])],
            [math.sin(sudut[i]),  math.cos(sudut[i]), panjang[i] * math.sin(sudut[i])],
            [0, 0, 1]
        ])
        T_total = np.dot(T_total, T_i)

    x = T_total[0, 2]
    y = T_total[1, 2]

    print("\nPosisi end effector:\n" "x =", round(x, 2), "y =", round(y, 2))
    print("\nMatriks transformasi total:")
    print(np.round(T_total, 3))

elif mode in ["ik", "inverse kinematics"]:
    panjang1 = float(input("Panjang lengan 1: "))
    panjang2 = float(input("Panjang lengan 2: "))
    x = float(input("Target posisi x: "))
    y = float(input("Target posisi y: "))

    cos_theta2 = (x**2 + y**2 - panjang1**2 - panjang2**2) / (2 * panjang1 * panjang2)
    theta2 = math.acos(cos_theta2)

    theta1 = math.atan2(y, x) - math.atan2(panjang2 * math.sin(theta2), panjang1 + panjang2 * math.cos(theta2))

    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)

    print("\nHasil perhitungan:")
    print(f"θ1 = {theta1_deg:.3f}°")
    print(f"θ2 = {theta2_deg:.3f}°")

else:
    print("Pilih FK / IK")
