import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

df['age'] = df['age'].fillna(df['age'].median())
df['sex'] = df['sex'].map({'male': 0.0, 'female': 1.0})

df['pclass_norm'] = (df['pclass'] - 1) / 2.0
df['age_norm'] = df['age'] / 80.0
df['sibsp_norm'] = df['sibsp'] / 8.0

features = ['pclass_norm', 'sex', 'age_norm', 'sibsp_norm']
X_train = torch.tensor(df[features].values, dtype=torch.float32)
y_train = torch.tensor(df[['survived']].values, dtype=torch.float32)


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
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


iters = 2000
best_loss = float("inf")

for epoch in range(iters):
    predicts = model(X_train)
    loss = criterion(predicts, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if loss.item() < best_loss:
        best_loss = loss.item()
        torch.save(model.state_dict(), "model_weights.pth")

    if (epoch + 1) % 200 == 0:
        print(f"Epoch : [{epoch + 1} / {iters}] | Loss : {loss.item():.4f}")

print(f"Best Loss : {best_loss:.4f}")