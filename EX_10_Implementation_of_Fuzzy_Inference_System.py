#Ex_No: 10 IMPLEMENATITON OF FUZZY INFERENCE SYSTEM


#When the distance from the front car is 3.5 m or so, what speed should I keep?

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


distance = np.arange(0, 11, 1)
speed = np.arange(0, 31, 1)

small = fuzz.trimf(distance, [0, 0, 4.6667])
medium = fuzz.trimf(distance, [1, 4, 7])
large = fuzz.trimf(distance, [6, 8, 10])


low = fuzz.trimf(speed, [0, 0, 15])
steady = fuzz.trimf(speed, [10, 20, 30])
high = fuzz.trimf(speed, [20, 30, 30])


plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(distance, small, label="Small")
plt.plot(distance, medium, label="Medium")
plt.plot(distance, large, label="Large")
plt.title("Distance Membership Functions")
plt.xlabel("Distance (m)")
plt.ylabel("Membership")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(speed, low, label="Low")
plt.plot(speed, steady, label="Steady")
plt.plot(speed, high, label="High")
plt.title("Speed Membership Functions")
plt.xlabel("Speed (mph)")
plt.ylabel("Membership")
plt.legend()

plt.tight_layout()
plt.show()


distance_input = 3.5


small_level = fuzz.interp_membership(
    distance, small, distance_input
)

medium_level = fuzz.interp_membership(
    distance, medium, distance_input
)

large_level = fuzz.interp_membership(
    distance, large, distance_input
)

print("Distance =", distance_input, "meters")

print("\nMembership Values")
print("-----------------")
print("Small =", round(small_level, 4))
print("Medium =", round(medium_level, 4))
print("Large =", round(large_level, 4))


speed_low = np.fmin(small_level, low)


speed_steady = np.fmin(medium_level, steady)


speed_high = np.fmin(large_level, high)


aggregated = np.fmax(
    np.fmax(speed_low, speed_steady),
    speed_high
)


recommended_speed = fuzz.defuzz(
    speed, aggregated, 'centroid'
)

print("\nRecommended Speed:",
      round(recommended_speed, 2),
      "miles/hour")


plt.figure(figsize=(8, 5))

plt.plot(speed, low, label="Low")
plt.plot(speed, steady, label="Steady")
plt.plot(speed, high, label="High")

plt.fill_between(
    speed, 0, aggregated,
    alpha=0.3, label="Aggregated Output"
)

plt.axvline(
    recommended_speed,
    linestyle="--",
    label="Recommended Speed"
)

plt.title("Fuzzy Inference System - Driving")
plt.xlabel("Speed (mph)")
plt.ylabel("Membership")
plt.legend()
plt.tight_layout()
plt.show()


#OUTPUT:

#MEMBERSHIP VALUES
#Small = 0.25
#Medium = 0.8333333
#Large = 0.0

#Recommended Speed = 16.7i miles/hour

