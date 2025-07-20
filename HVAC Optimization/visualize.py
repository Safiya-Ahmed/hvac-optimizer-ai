import matplotlib.pyplot as plt

def plot_energy_usage(history, explanation=None):
    days = list(range(1, len(history) + 1))
    temps = [x[0] for x in history]
    energy = [x[1] for x in history]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Energy Usage', color=color)
    ax1.plot(days, energy, color=color, marker='o', label='Energy Usage')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Temperature Setting (°C)', color=color)
    ax2.plot(days, temps, color=color, linestyle='--', marker='x', label='Temp Setting')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('HVAC Agent: Temperature vs Energy Usage')

    # 🧠 Optional: Display explanation below the plot
    if explanation:
        plt.figtext(0.5, -0.05, explanation, wrap=True, ha='center', fontsize=10)

    fig.tight_layout()
    plt.show()
