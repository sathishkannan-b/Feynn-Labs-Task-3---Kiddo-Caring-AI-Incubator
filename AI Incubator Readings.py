#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class AIIncubator:
    def __init__(self):
        self.incubator_id = "AI123"
        self.temperature = 36.5
        self.heart_rate = 120
        self.oxygen_level = 98

    def update_health_data(self):
        # Simulate random fluctuations in health data
        self.temperature += random.uniform(-0.5, 0.5)
        self.heart_rate += random.randint(-5, 5)
        self.oxygen_level += random.uniform(-1, 1)

    def get_health_data(self):
        return {
            "Temperature": self.temperature,
            "Heart Rate": self.heart_rate,
            "Oxygen Level": self.oxygen_level
        }

    def analyze_health_data(self):
        # Basic analysis of health data
        if self.temperature > 37.5 or self.heart_rate > 150 or self.oxygen_level < 95:
            return "Warning: Health parameters out of range!"
        else:
            return "Health parameters within normal range."

# Sample usage
if __name__ == "__main__":
    incubator = AIIncubator()
    for _ in range(5):
        incubator.update_health_data()
        health_data = incubator.get_health_data()
        print("Current Health Data:", health_data)
        analysis = incubator.analyze_health_data()
        print("Analysis:", analysis)

