class SimpleReflexAgent:
    def __init__(self, fixed_temp):
        self.fixed_temp = fixed_temp   
        self.current_temp = None

    def sensor(self, temp):
        
        self.current_temp = temp

    def performance(self):
        
        action = None
        if self.current_temp < self.fixed_temp:
            action = "Turn ON the Air conditioner"
        else:
            action = "Turn OFF the Air conditioner"
        return action

    def actuator(self):
        
        action = self.performance()
        print(f"Room Temp = {self.current_temp}°C => Action: {action}")



agent = SimpleReflexAgent(22)


rooms = {
    "Living Room": 30,
    "Drawing Room": 22,
    "Kitchen": 34,
    "Store Room": 20,
    "Kill Room: Tonight the night, it is going to happen again": 20
}


for room, temp in rooms.items():
    print(room, end=":\t")
    agent.sensor(temp)
    agent.actuator()
