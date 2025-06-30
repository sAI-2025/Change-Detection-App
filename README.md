
# 🖼️ Change Detection App — Automated Detection of Removed Objects Between Two Images

<!---[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  -->
<!---[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  -->
<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" alt="Python 3.10"/>
  <img src="https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Status-Beta-orange?logo=githubactions" alt="Beta Status"/>
  <img src="https://img.shields.io/badge/LangChain-Framework-4A90E2?logo=langchain" alt="LangChain"/>
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Store-00BFFF?logo=database" alt="ChromaDB"/>
  <img src="https://img.shields.io/badge/Groq-API-purple?logo=api" alt="Groq API"/>
  <img src="https://img.shields.io/badge/Colab-Ready-orange?logo=googlecolab" alt="Google Colab"/>
  <a href="https://colab.research.google.com/drive/1r6LuB3XVM_V4OWgakm90mKBLTTht2STp" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
  </a>
  <a href="https://github.com/sAI-2025/Jupiter_FAQ_Bot/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/sAI-2025/Jupiter_FAQ_Bot?style=social" alt="GitHub Stars"/>
  </a>
</p>

  
An intuitive and fully automated **computer vision app** to detect **removed objects** between two input images using OpenCV and Python.

This app is ideal for:
- 🛡️ **Security Surveillance** (e.g., detecting theft, missing assets)
- 🏗️ **Construction Progress Monitoring** (e.g., missing equipment or materials)
- 🛒 **Retail Loss Prevention** (e.g., empty shelves, misplaced items)
- 🌳 **Environmental Change Tracking** (e.g., deforestation, land changes)

---

## 🚀 Quick Features

✔️ Fully automated pipeline  
✔️ Web-based UI using Flask  
✔️ Visual bounding boxes over removed objects  
✔️ Batch processing supported  
✔️ Lightweight, no machine learning training required  
✔️ Easy-to-use Jupyter Notebook for detailed analysis  

---

## 📌 Problem Statement

Manually detecting object removal between two images is:
-  Time-consuming  
-  Error-prone  
-  Not scalable for real-world deployment  

Real-world conditions like:
- **Lighting variations**
- **Viewpoint shifts**
- **Occlusions**
- **Background noise**

… make manual comparison ineffective.

### ✅ Solution:
This app **automates object removal detection** using reliable computer vision techniques that are:
- Fast
- Scalable
- Interpretable

---

## 🧠 How It Works — Detection Pipeline

1. 🔄 **Image Preprocessing**
   - Convert input images to grayscale
   - Apply Gaussian blur to reduce camera noise and texture complexity

2. 🧮 **Image Differencing**
   - Compute absolute pixel-wise difference between the two images

3. 🎯 **Thresholding & Morphological Filtering**
   - Apply binary thresholding to segment major changes
   - Use morphological closing to remove minor noise and artifacts

4. ✂️ **Contour Detection**
   - Extract contours and filter out small, irrelevant regions

5. 📏 **Visualization**
   - Draw bounding boxes around detected removed objects
   - Save processed images for easy review and reporting

---

## 🖼️ Sample Output

- ✅ Clear bounding boxes over removed objects
- 🖼️ Results saved to `task_2_output/` directory
- 🔁 Upload and download interface for easy web-based usage

### 📁 Example Output Files:
```text
task_2_output/
├── 1~3.jpg       ← Processed detection result
├── 2~3.jpg
├── ...
└── detected_changes.jpg
````

---

## 📂 Project Structure

```bash
Produtz/
├── app.py                           # Flask web app (UI + detection logic)
├── Change_Detection.ipynb           # Jupyter notebook for detailed walkthrough
├── detected_changes.jpg             # Sample output image
├── requirements.txt                 # Python dependency list
├── task_2_output/                   # Processed result images
│   ├── 1~3.jpg, ..., 18~3.jpg
├── temp/                            # Temporary image storage
│   └── <uploaded files>.jpg
└── Task 2 - Change Detection Algorithm/
    └── input-images/
        ├── 1.jpg, 1~2.jpg, ..., 18~2.jpg  # Before/After image pairs
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

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

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

✔️ Python 3.7+ is required.

---

## 🚀 How to Run the App

### ▶️ Run via Flask Web App

```bash
python app.py
```

* Launches a local web app (Flask)
* Upload "Before" and "After" images via the web interface
* Click **“Detect Removed Objects”**
* View and download the processed result

### 🧪 Run via Jupyter Notebook

```bash
jupyter notebook Change_Detection.ipynb
```

* Step-by-step execution
* Ideal for debugging, learning, and custom processing

---

## ✅ Key Advantages

* 🔧 **No training data required**
* ⚡ **Fast and lightweight**
* 💻 **Works with local files, no internet dependency**
* 🌍 **Real-world robust: handles small misalignments and noise**
* 🖼️ **Visual outputs for quick verification**

---

## 📈 Future Improvements

* ✅ Auto-alignment of input images (image registration)
* ✅ Dynamic threshold adjustment via UI sliders
* ✅ Detection of added/modified objects (beyond removal)
* ✅ Deep learning-based semantic change detection
* ✅ Real-time video feed support
* ✅ Interactive before/after slider for better UX

---

## 📦 Requirements

```text
opencv-python
numpy
matplotlib
flask
Pillow
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🔍 Real-World Use Cases

### 🛒 Retail Loss Prevention

* Before: Shelf fully stocked
* After: Items missing or misplaced
  ✔️ Detected and marked in output

### 🏗️ Construction Monitoring

* Before: Tools and machinery present
* After: Equipment removed overnight
  ✔️ Identified via bounding boxes

### 🌿 Environmental Tracking

* Before: Natural habitat intact
* After: Trees cut down or displaced
  ✔️ Detected and highlighted regions

---

## 👨‍💻 Developed By

**Sai Krishna Chowdary Chundru**
📧 [cchsaikrishnachowdary@gmail.com](mailto:cchsaikrishnachowdary@gmail.com)
📞 +91 6305579992
🔗 [LinkedIn](https://www.linkedin.com/in/sai-krishna-chowdary-chundru) | [GitHub](https://github.com/sAI-2025)

---

## 📝 License

This project is licensed under the MIT License.
Feel free to modify, extend, and use it for both personal and commercial purposes. Attribution is appreciated.

---

## 📚 Additional Resources

* [OpenCV Documentation](https://docs.opencv.org/)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Python venv Guide](https://docs.python.org/3/library/venv.html)

---

## ⭐️ Support the Project

If you find this project useful, please consider giving it a ⭐️ on GitHub.
It helps grow the project and encourages further improvements!

---



