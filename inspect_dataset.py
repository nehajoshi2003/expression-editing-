import numpy as np

# Load the stacked vertices data
X = np.load("X.npy")

# Check the shape
print("Original shape of X.npy:", X.shape)

# Reshape it to (5, num_vertices * 3)
X_reshaped = X.reshape(5, -1)
print("Reshaped shape (for VAE):", X_reshaped.shape)

# Save the reshaped file
np.save("X_vae.npy", X_reshaped)
print("✅ Saved reshaped data to X_vae.npy")
