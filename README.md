
# 🖼️ Change Detection App — Automated Detection of Removed Objects Between Two Images

An intuitive computer vision-based app for detecting **removed objects** between two input images — automatically and reliably.

Ideal for applications in:

- 🛡️ Security Surveillance (e.g., detecting theft or tampering)
- 🏗️ Construction Progress Monitoring (e.g., missing equipment or materials)
- 🛒 Retail Loss Prevention (e.g., empty shelves or misplaced items)
- 🌳 Environmental Change Tracking (e.g., illegal deforestation or soil erosion)

---

## 📌 Problem Statement

Manually detecting object removal between two images is:

-  Time-consuming  
-  Error-prone  
-  Not scalable for real-world deployments  

Further challenges such as **lighting changes**, **minor viewpoint shifts**, **occlusions**, and **background noise** make manual comparison unreliable.

🧠 **This app solves the problem by** automating the detection process using image processing techniques — providing quick, reliable, and interpretable outputs, with no ML training required.

---

## 🧠 How It Works

The core of the app is a computer vision pipeline built with OpenCV:

1. 🔄 **Image Preprocessing**
   - Convert both “before” and “after” images to **grayscale**
   - Apply **Gaussian blur** to reduce noise and smooth textures

2. 🧮 **Image Differencing**
   - Compute the **absolute difference** between the two images, pixel by pixel

3. 🎯 **Thresholding & Morphological Filtering**
   - Apply **binary thresholding** to isolate areas of change
   - Use **morphological closing** (dilation → erosion) to eliminate small artifacts

4. ✂️ **Contour Detection**
   - Extract **contours** from the processed difference map
   - Filter based on area to remove false positives

5. 📏 **Visualization**
   - Draw **bounding boxes** around detected removed objects
   - Output saved image clearly marks what was removed

---

## 🖼️ Sample Output

- ✅ Clear bounding boxes over missing objects
- 🖼️ All outputs saved to `task_2_output/` directory
- 🔁 Includes web-based image upload and result download features

### 📁 Example Output Files:

```text
task_2_output/
├── 1~3.jpg       ← Before/After comparison with detection overlay
├── 2~3.jpg
├── ...
└── detected_changes.jpg
````

---

## 📁 Project Structure

```bash
Produtz/
├── app.py                           # Main Flask app (UI + detection logic)
├── Change_Detection.ipynb           # Step-by-step walkthrough in Jupyter
├── detected_changes.jpg             # Sample output image
├── requirements.txt                 # Python dependencies
├── task_2_output/                   # Processed result images
│   ├── 1~3.jpg, ..., 18~3.jpg
├── temp/                            # Temporary storage during app usage
│   └── <uploaded files>.jpg
└── Task 2 - Change Detection Algorithm/
    └── input-images/
        ├── 1.jpg, 1~2.jpg, ..., 18~2.jpg  # Before/after image pairs
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone This Repository

```bash
git clone https://github.com/sAI-2025/change-detection-app.git
cd change-detection-app
```

### 2️⃣ Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install All Dependencies

Ensure you have **Python 3.7 or higher**.

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the App

### ▶️ Option 1: Run via Python (Flask UI)

```bash
python app.py
```

* Launches a local web app (Flask)
* Upload “before” and “after” images
* Click **“Detect Removed Objects”**
* Download the processed output

### 🧪 Option 2: Run via Jupyter Notebook

```bash
jupyter notebook Change_Detection.ipynb
```

Explore and visualize the full pipeline step-by-step. Ideal for learning, debugging, or customizing.

---

## 📈 Future Improvements

🔧 Planned upgrades and enhancements:

* ✅ Auto-alignment of input images (image registration)
* ✅ Add slider UI to adjust detection thresholds dynamically
* ✅ Detect added/modified objects as well (not just removals)
* ✅ Integrate deep learning models for semantic-aware change detection
* ✅ Real-time detection from surveillance video streams
* ✅ Side-by-side interactive before/after comparison

---

## 📦 Requirements

**From `requirements.txt`:**

```text
opencv-python
numpy
matplotlib
flask
Pillow
```

To install:

```bash
pip install -r requirements.txt
```

---

## 🔍 Real-World Use Cases

### 🛒 Retail Theft or Restocking

* **Before**: Shelf fully stocked
* **After**: Items missing or misplaced
* ➡️ Detected and marked in output

### 🏗️ Construction Equipment Tracking

* **Before**: Site with tools and machinery
* **After**: Equipment removed overnight
* ➡️ Identified via bounding boxes

### 🌿 Environmental Monitoring

* **Before**: Natural habitat with trees
* **After**: Trees cut down or displaced
* ➡️ App highlights affected regions

---

## 👨‍💻 Developed By

**Sai Krishna Chowdary Chundru**
📧 [cchsaikrishnachowdary@gmail.com](mailto:cchsaikrishnachowdary@gmail.com)
📞 +91 6305579992
🔗 [LinkedIn](https://www.linkedin.com/in/sai-krishna-chowdary-chundru) | [GitHub](https://github.com/sAI-2025)

---

## 📝 License

MIT License.
Feel free to modify and use this project for both personal and commercial use — attribution appreciated.

---

