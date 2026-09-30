import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 8)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        s1 = self.relu(self.fc1(x))
        s2 = self.sigmoid(self.fc2(s1))
        return s2

model = NeuralNetwork()
model.load_state_dict(torch.load("model_weights.pth"))
model.eval()

sexe_list = {
    "homme": 0.0,
    "femme": 1.0
}

age_max = 80.0
proches_max = 8.0

while True:
    print("\nEVALUATION DE VOTRE CHANCE DE SURVIE AU TITANIC")

    classe = float(input("Votre classe ? (1, 2, 3)\n> "))
    classe_val = (classe - 1.0) / 2.0

    sexe = input("Votre sexe ? (homme/femme)\n> ").strip().lower()
    sexe_val = sexe_list.get(sexe, 0.0)
    age = float(input("Votre âge ?\n> "))
    age_val = age / age_max

    proches = float(input("Nombre de proches avec qui vous partez ?\n> "))
    proches_val = proches / proches_max

    with torch.no_grad():
        i_data = torch.tensor([[classe_val, sexe_val, age_val, proches_val]], dtype=torch.float32)
        prediction = model(i_data).item() * 100
        
    print(f"\nChance de survie estimée : {prediction:.1f}%\n")