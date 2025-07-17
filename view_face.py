import open3d as o3d

mesh = o3d.io.read_triangle_mesh("happy1.obj")

print(f"Vertices: {len(mesh.vertices)}")
print(f"Triangles: {len(mesh.triangles)}")

bbox = mesh.get_axis_aligned_bounding_box()
center = bbox.get_center()
print(f"Bounding box center: {center}")

# Move mesh to origin
mesh.translate(-center)

# Scale mesh to unit size
scale = 1.0 / max(bbox.get_extent())
mesh.scale(scale, center=(0, 0, 0))

mesh.compute_vertex_normals()
mesh.paint_uniform_color([0.8, 0.8, 0.8])

o3d.visualization.draw_geometries([mesh])
