# -*- coding: utf-8 -*-
"""lankmark_points_mesh.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kdZxtigthL98R_XNP7RK-ZfHVu57pe9n
"""

!pip install mediapipe opencv-python matplotlib
!pip uninstall -y numpy
!pip install numpy==1.23.5 --force-reinstall
!pip install --upgrade --force-reinstall opencv-python mediapipe matplotlib

#this code plots the landmark points in 3D --------------------------------------------------------------------------------------------
import cv2
import mediapipe as mp
import numpy as np
import plotly.graph_objs as go
from google.colab import files

# Upload image, use this code only if you are using colab otherwise change the code.
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Load image
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, _ = image.shape

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

# Process image
results = face_mesh.process(image_rgb)

if results.multi_face_landmarks:
    face_landmarks = results.multi_face_landmarks[0]

    # Extract 3D normalized coordinates
    xs, ys, zs = [], [], []
    for lm in face_landmarks.landmark:
        xs.append(lm.x)
        ys.append(lm.y)
        zs.append(-lm.z)  # Flip Z for natural depth perception

    # Convert to numpy arrays and scale
    xs = np.array(xs) * w
    ys = np.array(ys) * h
    zs = np.array(zs) * w  # Optional scaling for depth

    # Save Nx2 (x, y) coordinates to file
    landmarks_2d = np.stack((xs, ys), axis=1)
    np.savetxt("face_landmarks_2d.txt", landmarks_2d, fmt="%.2f", delimiter=",", header="x,y", comments='')

    print("2D facial landmarks saved to face_landmarks_2d.txt")

    # Plot interactive 3D scatter with Plotly
    fig = go.Figure(data=[go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode='markers',
        marker=dict(size=2, color='green'),
    )])

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data',
            yaxis=dict(autorange='reversed')  # Flip Y to match image
        ),
        title="Interactive 3D Face Landmarks",
        width=700,
        height=700
    )
    fig.show()
else:
    print("No face landmarks detected.")
#-------------------------------------------------------------------------------------
#this code plots the landmark points on the image.
import cv2
import mediapipe as mp
from google.colab.patches import cv2_imshow
from google.colab import files

# Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Load and process image
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

results = face_mesh.process(image_rgb)

if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        for lm in face_landmarks.landmark:
            x = int(lm.x * image.shape[1])
            y = int(lm.y * image.shape[0])
            cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

    # Show result in Colab
    cv2_imshow(image)
else:
    print("No face landmarks detected.")
#--------------------------------------------
# use this code to plot and save the landmark points in 2D and 3D
import cv2
import mediapipe as mp
import numpy as np
import plotly.graph_objs as go
from google.colab import files

# Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Load image
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, _ = image.shape

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

# Process image
results = face_mesh.process(image_rgb)

if results.multi_face_landmarks:
    face_landmarks = results.multi_face_landmarks[0]

    # Extract 3D normalized coordinates
    xs, ys, zs = [], [], []
    for lm in face_landmarks.landmark:
        xs.append(lm.x)
        ys.append(lm.y)
        zs.append(-lm.z)  # Flip Z for natural depth perception

    # Convert to numpy arrays and scale
    xs = np.array(xs) * w
    ys = np.array(ys) * h
    zs = np.array(zs) * w  # Optional scaling for depth

    # Save Nx2 (x, y) coordinates to file
    landmarks_2d = np.stack((xs, ys), axis=1)
    np.savetxt("face_landmarks_2d_gane.txt", landmarks_2d, fmt="%.2f", delimiter=",", header="x,y", comments='')

    # Save Nx3 (x, y, z) coordinates to file
    landmarks_3d = np.stack((xs, ys, zs), axis=1)
    np.savetxt("face_landmarks_3d_gane.txt", landmarks_3d, fmt="%.2f", delimiter=",", header="x,y,z", comments='')

    print("2D facial landmarks saved to face_landmarks_2d_sou.txt")
    print("3D facial landmarks saved to face_landmarks_3d_sou.txt")

    # Plot interactive 3D scatter with Plotly
    fig = go.Figure(data=[go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode='markers',
        marker=dict(size=2, color='green'),
    )])

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data',
            yaxis=dict(autorange='reversed')  # Flip Y to match image
        ),
        title="Interactive 3D Face Landmarks",
        width=700,
        height=700
    )
    fig.show()
else:
    print("No face landmarks detected.")

#----------------------------------------------------------------------------------
#the below code generates a mesh just to visualize a nrml mesh and save it
import cv2
import mediapipe as mp
import numpy as np
import plotly.graph_objects as go

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def save_obj(filename, vertices, faces):
    """Save vertices and triangle faces to an .obj file."""
    with open(filename, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for face in faces:
            # OBJ file indices start at 1
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")

def plot_facial_landmarks_3d(image, save_path='face_mesh.obj'):
    """Detects facial landmarks, plots in 3D, and saves mesh to .obj."""
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks_3d = []
            for lm in face_landmarks.landmark:
                landmarks_3d.append([lm.x, lm.y, -lm.z])
            landmarks_3d = np.array(landmarks_3d)

            # Scale to image resolution
            h, w, _ = image.shape
            xs = landmarks_3d[:, 0] * w
            ys = landmarks_3d[:, 1] * h
            zs = landmarks_3d[:, 2] * w
            vertices = np.stack((xs, ys, zs), axis=-1)

            # Extract triangle mesh from MediaPipe tesselation
            connections = mp_face_mesh.FACEMESH_TESSELATION
            faces = set()
            for edge in connections:
                faces.add(tuple(sorted(edge)))  # avoid duplicates
            # Convert edge-pairs to triangles (rough approximation)
            # For true triangulation, a separate step is required.
            triangle_faces = []
            face_dict = {}
            for a, b in faces:
                if a in face_dict:
                    face_dict[a].append(b)
                else:
                    face_dict[a] = [b]
            for a in face_dict:
                neighbors = face_dict[a]
                if len(neighbors) >= 2:
                    for i in range(len(neighbors)-1):
                        triangle_faces.append([a, neighbors[i], neighbors[i+1]])

            # Save .obj file
            save_obj(save_path, vertices, triangle_faces)
            print(f"Saved 3D mesh to: {save_path}")

            # Create edge lines for interactive visualization
            edge_x, edge_y, edge_z = [], [], []
            for start_idx, end_idx in connections:
                edge_x += [xs[start_idx], xs[end_idx], None]
                edge_y += [ys[start_idx], ys[end_idx], None]
                edge_z += [zs[start_idx], zs[end_idx], None]

            # Plot using Plotly
            fig = go.Figure()

            # Plot landmarks
            fig.add_trace(go.Scatter3d(
                x=xs, y=ys, z=zs,
                mode='markers',
                marker=dict(size=2, color='blue'),
                name='Landmarks'
            ))

            # Plot mesh edges
            fig.add_trace(go.Scatter3d(
                x=edge_x, y=edge_y, z=edge_z,
                mode='lines',
                line=dict(color='gray', width=1),
                name='Mesh'
            ))

            fig.update_layout(
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',
                    yaxis=dict(autorange='reversed'),
                    aspectmode='data'
                ),
                title="Interactive 3D Face Mesh from MediaPipe",
                width=800,
                height=800,
                showlegend=False
            )
            fig.show()
            return vertices
    else:
        print("No face detected in the image.")
        return None

# Load image and process
image_path = '/content/flipped_sou.jpg'
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")
    landmarks_3d = plot_facial_landmarks_3d(image, save_path='face_mesh_flippedSou.obj')
    if landmarks_3d is not None:
        print("Exported landmarks shape:", landmarks_3d.shape)
except FileNotFoundError as e:
    print(e)

# Clean up MediaPipe
face_mesh.close()