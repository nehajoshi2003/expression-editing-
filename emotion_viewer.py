import open3d as o3d
import time
import os
import math

EMOTION_MAP = {
    "Joy": "Happy",
    "Anger": "Anger",
    "Fear": "Fear",
    "Sadness": "Sad",
    "Surprise": "Surprise"
}

def show_expression_sequence(expression_list, path="triangulated_expressions"):
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="Emotion Viewer", width=800, height=800)

    first_expr = EMOTION_MAP.get(expression_list[0], expression_list[0])
    mesh = o3d.io.read_triangle_mesh(os.path.join(path, f"{first_expr}.obj"))
    mesh.compute_vertex_normals()
    vis.add_geometry(mesh)
    vis.poll_events()
    vis.update_renderer()

    view_ctl = vis.get_view_control()
    bbox = mesh.get_axis_aligned_bounding_box()
    view_ctl.set_lookat(bbox.get_center())
    view_ctl.set_front([0, 0, 1])
    view_ctl.set_up([0, 1, 0])
    view_ctl.set_zoom(0.8)

    for expr in expression_list:
        mapped_expr = EMOTION_MAP.get(expr, expr)
        file_path = os.path.join(path, f"{mapped_expr}.obj")

        if not os.path.exists(file_path):
            print(f"⚠️ File not found: {file_path}")
            continue

        new_mesh = o3d.io.read_triangle_mesh(file_path)
        new_mesh.compute_vertex_normals()

        vis.remove_geometry(mesh, reset_bounding_box=False)
        mesh = new_mesh
        vis.add_geometry(mesh)

        vis.poll_events()
        vis.update_renderer()
        print(f"🟢 Showing: {mapped_expr}")
        time.sleep(2)

    vis.destroy_window()
