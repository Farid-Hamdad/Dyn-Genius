
# valence.py
class ValenceEngine:
    def compute_emotion(self, activation, valence):
        return activation * valence

# Test
if __name__ == "__main__":
    engine = ValenceEngine()
    print(engine.compute_emotion(0.9, -0.5))  # -> -0.45
