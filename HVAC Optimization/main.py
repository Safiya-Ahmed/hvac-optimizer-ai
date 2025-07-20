import matplotlib.pyplot as plt

from llm_explainer import get_llm_explanation

# Dummy example temperature and energy history
temperature_settings = [22, 22, 23, 21, 22, 23, 22]
energy_usage = [4.2, 4.1, 5.0, 3.8, 4.3, 5.1, 4.2]
days = list(range(1, len(temperature_settings) + 1))

# 1. ✅ Plot the chart (no text inside the chart)
fig, ax1 = plt.subplots()

# Primary Y-axis: Energy usage
ax1.set_xlabel('Day')
ax1.set_ylabel('Energy Usage (kWh)', color='tab:blue')
ax1.plot(days, energy_usage, color='tab:blue', marker='o', label='Energy Usage')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Secondary Y-axis: Temperature setting
ax2 = ax1.twinx()
ax2.set_ylabel('Temperature (°C)', color='tab:red')
ax2.plot(days, temperature_settings, color='tab:red', linestyle='--', marker='^', label='Temperature Setting')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title and layout
plt.title('HVAC Agent: Temperature vs Energy Usage')
fig.tight_layout()
plt.grid(True)
plt.show()

# ... previous code (chart plotting) ...

# Call LLM for explanation
history = list(zip(temperature_settings, energy_usage))
explanation = get_llm_explanation(history)

# Display explanation below the chart in terminal
print("\n=== LLM Explanation ===\n")
print(explanation)
