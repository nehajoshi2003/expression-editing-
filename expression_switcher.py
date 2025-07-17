from transformers import pipeline
import open3d as o3d

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

emotion_to_obj = {
    "joy": "happy1.obj",
    "happiness": "happy1.obj",
    "sadness": "saddie.obj",
    "anger": "angry1.obj",
    "fear": "feared.obj",
    "surprise": "surprise.obj",
    "disgust": "disg.obj",
    "contempt": "pls.obj",
    "neutral": "pls.obj",
}

sentence = input("Enter a sentence: ")
result = classifier(sentence)[0][0]  # <-- fix is here!
emotion = result['label'].lower()
confidence = result['score']

print(f"Detected emotion: {emotion} (confidence: {confidence:.2f})")

obj_file = emotion_to_obj.get(emotion, "neutral.obj")

mesh = o3d.io.read_triangle_mesh(obj_file)
if not mesh.has_triangles():
    print("Error: No geometry found in mesh!")
else:
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh], window_name=f"Emotion: {emotion}")
