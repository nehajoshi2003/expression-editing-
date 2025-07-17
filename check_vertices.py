import open3d as o3d, glob, os, numpy as np
folder = "triangulated_expressions"
for f in sorted(glob.glob(os.path.join(folder, "*.obj"))):
    v = np.asarray(o3d.io.read_triangle_mesh(f).vertices)
    print(f"{os.path.basename(f):12}  →  {v.shape}")
