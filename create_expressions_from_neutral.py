import open3d as o3d
import numpy as np
import os

def load_mesh(path):
    mesh = o3d.io.read_triangle_mesh(path)
    mesh.compute_vertex_normals()
    return mesh

def save_mesh(vertices, mesh_template, path):
    mesh_copy = o3d.geometry.TriangleMesh(mesh_template)  # Clone the template
    mesh_copy.vertices = o3d.utility.Vector3dVector(vertices)
    o3d.io.write_triangle_mesh(path, mesh_copy)

def create_expression(neutral_vertices, expression_type):
    vertices = neutral_vertices.copy()

    # Modify vertices by index range (adjust ranges based on your model)
    if expression_type == "Happy":
        vertices[3000:3050, 1] += 2
    elif expression_type == "Sad":
        vertices[3000:3050, 1] -= 2
    elif expression_type == "Surprise":
        vertices[3000:3050, 2] -= 2
    elif expression_type == "Anger":
        vertices[100:150, 1] -= 1
    elif expression_type == "Fear":
        vertices[3000:3050, 2] -= 1
        vertices[100:150, 1] += 1
    else:
        raise ValueError("Unsupported expression")

    return vertices

# Load a mesh with the correct vertex count (e.g. Happy.obj)
base_mesh = load_mesh("triangulated_expressions/Happy.obj")
neutral_vertices = np.asarray(base_mesh.vertices)

# Create and save expressions
expressions = ["Happy", "Sad", "Surprise", "Anger", "Fear"]
for expr in expressions:
    new_vertices = create_expression(neutral_vertices, expr)
    save_mesh(new_vertices, base_mesh, f"triangulated_expressions/{expr}.obj")
    print(f"✅ Saved {expr}.obj")
