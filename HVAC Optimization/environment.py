import random

def simulate_energy_usage(temp, outside_temp=32, occupancy=10):
    ideal_temp = 25  # The most energy-efficient temperature
    temp_penalty = abs(temp - ideal_temp) * 10  # Penalty for deviating from ideal
    occupancy_penalty = occupancy * 0.2  # More people = more heat = more energy needed
    weather_penalty = (outside_temp - 25) * 0.5  # Hotter outside = more load
    random_noise = random.uniform(0, 2)  # Simulates sensor noise or unpredictable factors

    return temp_penalty + occupancy_penalty + weather_penalty + random_noise
