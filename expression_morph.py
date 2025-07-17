import open3d as o3d

mesh = o3d.io.read_triangle_mesh("contempt.obj")
print("Vertices:", len(mesh.vertices))
print("Triangles:", len(mesh.triangles))

o3d.visualization.draw_geometries([mesh])
