import open3d as o3d
import numpy as np
import os

expression_files = [
    "triangulated_expressions/Anger.obj",
    "triangulated_expressions/Fear.obj",
    "triangulated_expressions/Happy.obj",
    "triangulated_expressions/Sad.obj",
    "triangulated_expressions/Surprise.obj",
]

all_vertices = []

for file in expression_files:
    print(f"Loading {file}...")
    mesh = o3d.io.read_triangle_mesh(file)
    vertices = np.asarray(mesh.vertices)
    print(f"→ Vertices count for {file}: {vertices.shape}")
    all_vertices.append(vertices)

# Check for mismatched shapes before stacking
shapes = [v.shape for v in all_vertices]
if len(set(shapes)) != 1:
    print("\n❌ Mismatch found!")
    for file, shape in zip(expression_files, shapes):
        print(f"{file} → {shape}")
    exit()

# If all shapes match, save as dataset
data = np.vstack(all_vertices)
np.save("X.npy", data)
print("✅ Saved X.npy successfully.")
