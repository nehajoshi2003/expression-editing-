import numpy as np
import torch
from torch import nn
import open3d as o3d
from sklearn.decomposition import PCA
import joblib

# === Load VAE ===
class VAE(nn.Module):
    def __init__(self, input_dim=5, latent_dim=2):
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

# === Load VAE model and PCA ===
input_dim = 5
latent_dim = 2

vae = VAE(input_dim, latent_dim)
vae.load_state_dict(torch.load("vae_model.pt"))
vae.eval()

pca = joblib.load("pca_model.pkl")

# === Generate new expression ===
with torch.no_grad():
    z = torch.randn(1, latent_dim)  # sample from latent space
    generated_pca = vae.decode(z).numpy()
    generated_flat = pca.inverse_transform(generated_pca)

# === Save to OBJ ===
neutral_mesh = o3d.io.read_triangle_mesh("triangulated_expressions/Happy.obj")
generated_vertices = np.reshape(generated_flat, (-1, 3))
neutral_mesh.vertices = o3d.utility.Vector3dVector(generated_vertices)
o3d.io.write_triangle_mesh("generated_expression.obj", neutral_mesh)

print("✅ New expression generated and saved as generated_expression.obj")
