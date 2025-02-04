class PollutionControlAgent:

    def __init__(self,preferences):
        self.preferences=preferences  
        self.strategies=[
            {"name": "Increase Public Transport","pollution_reduction": 8,"cost": 5,"public_acceptance": 7},
            {"name": "Industrial Regulations","pollution_reduction": 9,"cost": 8,"public_acceptance": 5},
            {"name": "Promote Electric Vehicles","pollution_reduction": 7,"cost": 6,"public_acceptance": 8},
            {"name": "Green Energy Subsidies","pollution_reduction": 6,"cost": 7,"public_acceptance": 9},
        ]

    def calculate_utility(self,strategy):
        utility=(
            self.preferences["pollution_reduction"]*strategy["pollution_reduction"]-
            self.preferences["cost"]*strategy["cost"]+
            self.preferences["public_acceptance"]*strategy["public_acceptance"]
        )
        return utility
        
    def select_best_strategy(self):
        best_strategy=None
        max_utility=float("-inf")
        for strategy in self.strategies:
            utility = self.calculate_utility(strategy)
            if utility > max_utility:
                max_utility = utility
                best_strategy = strategy
        return best_strategy

preferences = {"pollution_reduction": 0.6, "cost": 0.3, "public_acceptance": 0.1}
pollution_agent = PollutionControlAgent(preferences)
best_strategy = pollution_agent.select_best_strategy()
print("Best Pollution Control Strategy:", best_strategy["name"])
