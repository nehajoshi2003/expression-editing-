import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
from vae_model import VAE  # your VAE model class file

# Custom Dataset to load your numpy data
class ExpressionDataset(Dataset):
    def __init__(self, npy_file):
        self.data = np.load(npy_file).astype(np.float32)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Loss function: Reconstruction + KL divergence
def loss_function(recon_x, x, mu, logvar):
    MSE = nn.MSELoss()(recon_x, x)
    # KL divergence
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return MSE + KLD * 0.001  # weight KL loss lightly

def train():
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

    dataset = ExpressionDataset("X.npy")
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

    # Load the model - input_dim should be vertex count * 3 (x,y,z)
    input_dim = dataset[0].shape[0]
    model = VAE(input_dim=input_dim, latent_dim=32).to(device)

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    epochs = 200  # you can increase later

    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch in dataloader:
            batch = batch.to(device)
            optimizer.zero_grad()
            recon_batch, mu, logvar = model(batch)
            loss = loss_function(recon_batch, batch, mu, logvar)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()



        print(f"Epoch {epoch+1} / {epochs} - Loss: {total_loss / len(dataloader):.4f}")

    torch.save(model.state_dict(), "vae_expression.pth")
    print("Model saved as vae_expression.pth")

if __name__ == "__main__":
    train()
