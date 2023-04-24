# import libraries needed
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# Data
arrival_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
start_times = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]
exit_times = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]
queue_times = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]
system_num = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]
queue_num = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]
lam_values_old = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lam_values_new = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
u_values_old = [1/8, 2/22, 3/12, 4/19, 5/25, 6/7, 7/20, 8/29, 9/3, 10/24, 11/14, 12/11, 13/7, 14/5, 15/4]
mean_values = [(1/8)/(1-(1/8)), (2/22)/(1-(2/22)), (3/12)/(1-(3/12)), (4/19)/(1-(4/19)), (5/25)/(1-(5/25)), (6/7)/(1-(6/7)),
               (7/20)/(1-(7/20)), (8/29)/(1-(8/29)), (9/3)/(1-(9-3)), (10/24)/(1-(10/24)), (11/14)/(1-(11/14)), (12/11)/(1-(12/11)),
               (13/7)/(1-(13/7)), (14/5)/(1-(14/5)), (15/4)/(1-(15/4))]
mean_times = [1/8, 1/44, 1/36, 1/76, 1/125, 1/42, 1/140, 1/232, 1/27, 1/240, 1/154, 1/132, 1/97, 1/70, 1/60]
new_mean_times = [1/5 * 1/8, 1/5 * 1/44, 1/5 * 1/36, 1/5 * 1/76, 1/5 * 1/125, 1/5 * 1/42, 1/5 * 1/140, 1/5 * 1/232,
                  1/5 * 1/27, 1/5 * 1/240, 1/5 * 1/154, 1/5 * 1/132, 1/5 * 1/97, 1/5 * 1/70, 1/5 * 1/60]

# Plot the data as a line graph
plt.plot(arrival_times, start_times, "-o")

# Add labels and title
plt.xlabel("Arrival Time (min)")
plt.ylabel("Enter Time (min)")
plt.title("Customer Arrival Time vs. Enter Time")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(arrival_times, exit_times, "-o")

# Add labels and title
plt.xlabel("Arrival Time (min)")
plt.ylabel("Exit Time (min)")
plt.title("Customer Arrival Time vs. Exit Time")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(arrival_times, queue_times, "-o")

# Add labels and title
plt.xlabel("Arrival Time (min)")
plt.ylabel("Queue Time (min)")
plt.title("Customer Arrival Time vs. Queue Time")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(arrival_times, system_num, "-o")

# Add labels and title
plt.xlabel("Arrival Time (min)")
plt.ylabel("Number in System")
plt.title("Customer Arrival Time vs. Number in System")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(arrival_times, queue_num, "-o")

# Add labels and title
plt.xlabel("Arrival Time (min)")
plt.ylabel("Number in Queue")
plt.title("Customer Arrival Time vs. Number in Queue")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(times, u_values_old, "-", label="Old Utilization")
plt.plot(times, u_values_old, "--", label="New Utilization, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Utilization (p)")
plt.title("a) Utilization (p) over Time (t)")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(lam_values_old, lam_values_old, "-", label="Old Throughput")
plt.plot(lam_values_old, lam_values_new, "--", label="New Throughput, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Throughput (x)")
plt.title("b) Throughput (x) over Time (t)")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(times, mean_values, "-", label="Old mean number in system")
plt.plot(times, mean_values, "--", label="New mean number in system, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Mean number in system E[N]")
plt.title("c) Mean number in system E[N] over Time (t)")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(times, mean_times, "-", label="Old mean time in system")
plt.plot(times, new_mean_times, "--", label="New mean time in system, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Mean time in system E[T]")
plt.title("d) Mean time in system E[T] over Time (t)")

# Show the plot
plt.show()