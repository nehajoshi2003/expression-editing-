import numpy as np
from sklearn.decomposition import PCA
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# === Load reshaped dataset ===
X = np.load("X_vae.npy")  # Shape: (5, 892332)

# === Step 1: PCA ===
pca_components = 5
pca = PCA(n_components=pca_components)
X_pca = pca.fit_transform(X)  # Now shape: (5, 100)
print(f"PCA output shape: {X_pca.shape}")

# === Save PCA model and data ===
np.save("X_pca.npy", X_pca)
import joblib
joblib.dump(pca, "pca_model.pkl")

# === Step 2: Define VAE ===
class VAE(nn.Module):
    def __init__(self, input_dim=100, latent_dim=2):
        super(VAE, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc21 = nn.Linear(64, latent_dim)  # mean
        self.fc22 = nn.Linear(64, latent_dim)  # logvar
        self.fc3 = nn.Linear(latent_dim, 64)
        self.fc4 = nn.Linear(64, input_dim)

    def encode(self, x):
        h = torch.relu(self.fc1(x))
        return self.fc21(h), self.fc22(h)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z):
        h = torch.relu(self.fc3(z))
        return self.fc4(h)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar

# === Step 3: Train VAE ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vae = VAE(input_dim=pca_components).to(device)
optimizer = optim.Adam(vae.parameters(), lr=1e-3)

X_tensor = torch.tensor(X_pca, dtype=torch.float32).to(device)

def loss_fn(recon_x, x, mu, logvar):
    recon_loss = nn.functional.mse_loss(recon_x, x)
    kl_loss = -0.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp())
    return recon_loss + kl_loss

epochs = 1000
for epoch in range(epochs):
    vae.train()
    recon_batch, mu, logvar = vae(X_tensor)
    loss = loss_fn(recon_batch, X_tensor, mu, logvar)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# === Save VAE model ===
torch.save(vae.state_dict(), "vae_model.pt")
joblib.dump(pca, "pca_model.pkl")
print("✅ VAE training completed and model saved.")

