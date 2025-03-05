import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the Laplace variable 's'
s = ctrl.tf('s')

# Process transfer function:
# G(s) = (0.5s + 1) / ((s + 1)^3 * (0.1s + 1))
G = (0.5*s + 1) / ((s + 1)**3 * (0.1*s + 1))

# -----------------------------
# Method 1: Ziegler-Nichols Process Reaction Curve Method
# -----------------------------
# For demonstration, assume estimated FOPDT parameters from the process step response:
K_est = 1.0   # Estimated process gain
L_est = 0.5   # Estimated dead time (s)
T_est = 2.0   # Estimated time constant (s)

# Ziegler-Nichols tuning rules for PID:
Kc_1 = 1.2 * T_est / (K_est * L_est)  # Proportional gain
Ti_1 = 2 * L_est                      # Integral time
Td_1 = 0.5 * L_est                    # Derivative time

# Define the PID controller:
# PID(s) = Kc * (1 + 1/(Ti*s) + Td*s)
PID1 = Kc_1 * (1 + 1/(Ti_1 * s) + Td_1 * s)

# Closed-loop system for Method 1:
CL1 = ctrl.feedback(PID1 * G, 1)

# Compute step response for Method 1:
t1, y1 = ctrl.step_response(CL1)

# Plotting the step response for Method 1:
plt.figure()
plt.plot(t1, y1, label='Method 1: ZN Process Reaction Curve', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Closed-loop Step Response (Method 1)')
plt.legend()
plt.grid(True)
plt.savefig('ZN1_step_response.pdf')

# -----------------------------
# Method 2: Ziegler-Nichols Ultimate Sensitivity Method
# -----------------------------
# For demonstration, assume experimentally obtained values:
Ku = 2.5  # Ultimate gain (assumed)
Tu = 3.5  # Ultimate period (s) (assumed)

# Ziegler-Nichols tuning rules for PID using ultimate sensitivity:
Kc_2 = 0.6 * Ku
Ti_2 = 0.5 * Tu
Td_2 = 0.125 * Tu

# Define the PID controller for Method 2:
PID2 = Kc_2 * (1 + 1/(Ti_2 * s) + Td_2 * s)

# Closed-loop system for Method 2:
CL2 = ctrl.feedback(PID2 * G, 1)

# Compute step response for Method 2:
t2, y2 = ctrl.step_response(CL2)

# Plotting the step response for Method 2:
plt.figure()
plt.plot(t2, y2, label='Method 2: ZN Ultimate Sensitivity', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Closed-loop Step Response (Method 2)')
plt.legend()
plt.grid(True)
plt.savefig('ZN2_step_response.pdf')

plt.show()
