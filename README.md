# 3D Facial Expression Generation Project

This project focuses on generating and modifying 3D facial expressions using deep learning. It combines emotion detection from text/audio with 3D mesh morphing to animate a cartoon-style face model.

---

## Demo

| Input Text or Audio | Output Expression |
|---------------------|-------------------|
| _"I'm so excited!"_ | ![Happy](![WhatsApp Image 2025-06-29 at 10 12 38 PM](https://github.com/user-attachments/assets/7f294f1b-31cf-4dd0-a356-5b33a095612d)
) |
| _"I'm feeling low today."_ | ![Sad](![WhatsApp Image 2025-06-29 at 10 18 06 PM](https://github.com/user-attachments/assets/81951977-8a13-49c4-82bf-4afa94c88551)
) |

You can also view the full working demo below:

(![WhatsApp Image 2025-06-29 at 10 10 52 PM](https://github.com/user-attachments/assets/7abe312d-240c-4122-bc66-ad79327b9fc0)
)![WhatsApp Image 2025-06-29 at 10 12 38 PM](https://github.com/user-attachments/assets/7dab1272-3055-4fef-9ec9-8eedbb0c87f2)
![WhatsApp Image 2025-06-29 at 10 12 38 PM (1)](https://github.com/user-attachments/assets/3c65dead-750c-41a5-a589-cd58ce797c0d)


---

## Objective

To develop a system that can:
1. Change the facial expression of a 3D model based on user-input text.
2. Modify expressions dynamically based on the tone of audio.
3. Add lip-syncing to match the spoken audio.

---

##  Methodology

Here’s an overview of the system pipeline:

![Methodology Flow](![WhatsApp Image 2025-06-27 at 11 49 33 AM (2)](https://github.com/user-attachments/assets/9951fe4b-27e9-4b1b-89e7-a53a47c87d60)
)

---

##  Techniques Used

- **Deep Learning Models**:
  - **Variational Autoencoders (VAE)** for mesh-based expression generation.
  - **GANs (StyleGAN3)** and **Diffusion Models** for advanced expression synthesis (exploration in progress).
- **Emotion Recognition**:
  - Text-based emotion detection using **Hugging Face Transformers**.
  - Audio emotion inference using tone analysis.
- **3D Processing**:
  - Working with `.obj` files with consistent vertex topology.
  - Real-time rendering and visualization using **Open3D** and optionally **Three.js** for web display.

---

##  Project Milestones

1. **Expression Morphing from Text**  
   → Detects emotions from input text and morphs the 3D face accordingly.

2. **Expression Editing from Audio Tone**  
   → Analyzes emotional tone in voice and changes the 3D expression in real time.

3. **Lip Syncing with Audio**  
   → Adds synchronized mouth movement to match spoken audio.

---

##  Dataset & Resources

- **Custom 3D Cartoon Face Model** (`.obj`)
- **FaceWarehouse 3D Dataset**
- Audio/text datasets for emotion recognition
- FLAME 2023 + Vertex Masks for future integration

---

##  Tools & Libraries

- Python (Open3D, PyTorch, NumPy)
- Hugging Face Transformers
- Web: Three.js (optional)
- Jupyter notebooks for prototyping

---

##  Status

-  Text-to-emotion working with basic expressions
-  Expression morphing implemented using VAE
-  Audio tone mapping and lip-syncing under development
-  Real-time viewer and GUI in progress

---

