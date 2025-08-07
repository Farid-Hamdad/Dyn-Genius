# energie_cognitive.py
class EnergyManager:
    def __init__(self, threshold=5.0):
        self.threshold = threshold

    def compute_energy(self, activations):
        return sum(a ** 2 for a in activations)

    def is_overloaded(self, activations):
        return self.compute_energy(activations) > self.threshold

# Test
if __name__ == "__main__":
    e = EnergyManager()
    activations = [0.8, 0.7, 1.1]
    print("Énergie totale :", e.compute_energy(activations))
    print("Surcharge ?", e.is_overloaded(activations))
