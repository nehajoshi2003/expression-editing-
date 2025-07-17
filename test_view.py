import open3d as o3d

mesh = o3d.io.read_triangle_mesh("triangulated_expressions/Happy.obj")
mesh.compute_vertex_normals()
mesh.scale(10.0, center=mesh.get_center())  # scale up

o3d.visualization.draw_geometries([mesh], window_name="Test Happy.obj")
