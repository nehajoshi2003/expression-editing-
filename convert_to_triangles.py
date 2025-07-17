import os
import open3d as o3d

input_folder = "expressions"
output_folder = "triangulated_expressions"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".obj"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            mesh = o3d.io.read_triangle_mesh(input_path)

            # Only keep triangles
            mesh.triangles = o3d.utility.Vector3iVector(
                [tri for tri in mesh.triangles if len(tri) == 3]
            )
            o3d.io.write_triangle_mesh(output_path, mesh)
            print(f"✅ Converted {filename}")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")
