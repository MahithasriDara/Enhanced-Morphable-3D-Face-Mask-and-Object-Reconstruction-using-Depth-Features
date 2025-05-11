# Enhanced-Morphable-3D-Face-Mask-and-Object-Reconstruction-using-Depth-Features

This repository contains the implementation for the final year project titled **"Enhanced Morphable 3D Face and Object Reconstruction using Depth Features"**. The project focuses on generating accurate and editable 3D face and object models from a single 2D image using landmark detection, depth feature extraction, and edge enhancement techniques.

## 📌 Project Description

Traditional 3D reconstruction methods often require multiple images or depth sensors, which are costly and computationally intensive. This project uses deep learning methods to reconstruct 3D models from a single 2D image by integrating:

- 2D to 3D landmark mapping
- Depth feature extraction
- Edge detection for mesh refinement
- 3D mesh generation and export

The final output is an editable 3D mesh model that can be exported in formats such as `.obj` or `.ply`.

---

## 🧾 Files in this Repository

- `landmark_points_mesh.py` - Generates 3D mesh using facial landmarks.
- `depth_generator.py` - Extracts depth features from the input image.
- `edge_detection.py` - Applies edge detection to enhance the mesh.
- `DESIGN_PROJECT_MID_REVIEW.pdf` - Project PPT summarizing the objectives, methodology, and results.
- `/architecture_images/` - Contains images showing system architecture and flow diagrams.
- `/outputs/` - Screenshots of generated 3D models and mesh comparisons.

---

## 🏗️ Methodology Overview

### ➤ Input: 2D Image  
### ➤ Steps:
1. **Preprocessing:** Resize and normalize the input image.
2. **Face Detection:** Check if the image contains a face.
3. **Landmark Extraction:** Use 468-point detection for improved mesh accuracy.
4. **Depth and Edge Extraction:** Extract and enhance depth and edge features.
5. **3D Mesh Generation:** Fuse features into a 3D mesh using morphable models.
6. **Export:** Save the mesh in editable format.

<p align="center">
  <img src="architecture_images/new.jpg" width="500" />
  <br>
  <em>Proposed System Architecture</em>
</p>

---

## 🧪 Sample Results

<p align="center">
  <img src="outputs/visual results.png" width="500" />
  <br>
  <em>Sample Output: 3D Mesh from 2D Face Input</em>
</p>

---

## 🔮 Future Work

- Reconstruct multiple faces or full body with pose estimation.
- Improve texture mapping for more realism.
- Build an open-source 3D reconstruction toolkit using AI.

---


