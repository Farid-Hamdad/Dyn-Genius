# concept.py
class Concept:
    def __init__(self, name, valence=0.0):
        self.name = name
        self.activation = 0.0
        self.valence = valence
        self.links = {}

    def link_to(self, other, weight=1.0):
        self.links[other] = weight

    def propagate(self):
        for concept, weight in self.links.items():
            concept.activation += self.activation * weight

# Exemple d'utilisation
if __name__ == "__main__":
    c1 = Concept("Joie", valence=0.8)
    c2 = Concept("Rire", valence=0.7)
    c1.activation = 1.0
    c1.link_to(c2, weight=0.5)
    c1.propagate()
    print(f"Activation de {c2.name} : {c2.activation}")
