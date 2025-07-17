import os
import numpy as np
import open3d as o3d

path = "triangulated_expressions"
expressions = ["Happy", "Anger", "Fear", "Sad", "Surprise"]

meshes = []
for expr in expressions:
    file_path = os.path.join(path, f"{expr}.obj")
    if not os.path.exists(file_path):
        print(f"❌ Missing file: {file_path}")
        continue

    mesh = o3d.io.read_triangle_mesh(file_path)
    mesh.compute_vertex_normals()
    vertices = np.asarray(mesh.vertices)
    meshes.append((expr, vertices))

# Compare all to the first mesh
base_expr, base_vertices = meshes[0]
for expr, vertices in meshes[1:]:
    diff = np.linalg.norm(base_vertices - vertices)
    print(f"🔍 Difference between {base_expr} and {expr}: {diff:.6f}")
