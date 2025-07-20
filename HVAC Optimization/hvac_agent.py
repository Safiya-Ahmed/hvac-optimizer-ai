class HVACAgent:
    def __init__(self):
        self.temp = 24  # Starting temp
        self.history = []

    def decide_temperature(self):
        return self.temp

    def update_policy(self, energy):
        self.history.append((self.temp, energy))
        if len(self.history) > 1:
            prev_energy = self.history[-2][1]
            if energy > prev_energy:
                self.temp += 1
            else:
                self.temp -= 1
        self.temp = max(22, min(27, self.temp))  # Keep within realistic range
