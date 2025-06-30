import streamlit as st
import numpy as np
import cv2
from io import BytesIO
from PIL import Image
from streamlit_image_comparison import image_comparison
import time

# Constants
PRIMARY_COLOR = "#1f2937"
ACCENT_COLOR = "#10b981"
BOX_COLOR = (255, 0, 0)
FONT_FAMILY = "Poppins, sans-serif"

# Page config
st.set_page_config(
    page_title="Change Detection",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject CSS for fonts and styling
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

body {{
    font-family: {FONT_FAMILY};
    background-color: #f9fafb;
}}

h1 {{
    color: {PRIMARY_COLOR};
    font-weight: 600;
}}

.stButton>button {{
    background-color: {ACCENT_COLOR};
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5em 1.2em;
    font-size: 1rem;
    transition: 0.2s;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}}

.stButton>button:hover {{
    background-color: #0f766e; /* slightly darker accent */
    transform: translateY(-1px);
    box-shadow: 0 6px 8px rgba(0,0,0,0.15);
}}

.stInfo, .stSuccess, .stError, .stWarning {{
    border-radius: 8px !important;
    padding: 1em !important;
}}

img[alt=""] {{
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border-radius: 6px;
}}

.css-1d391kg {{
    gap: 1.5rem;  /* spacing between columns */
}}
</style>
""", unsafe_allow_html=True)

# Sidebar instructions
with st.sidebar:
    st.title("🔍 Instructions")
    st.write("""
    - Upload **aligned** Before & After images.
    - Adjust **sensitivity slider** for detection threshold.
    - Click **Detect Changes** to process.
    - Compare results with slider & download output.
    """)
    st.write("---")
    st.write("📷 Sample images available [here](https://github.com/arnaudmiribel/streamlit-image-comparison).")

# Header
st.markdown("<h1>🖼️ Change Detection</h1>", unsafe_allow_html=True)

# Upload images side-by-side
col1, col2 = st.columns([1, 1], gap="medium")
with col1:
    before_file = st.file_uploader("Before Image", type=["jpg", "png"], key="before")
    if before_file:
        before = Image.open(before_file).convert("RGB")
        st.write(f"✅ Uploaded: {before.size[0]}×{before.size[1]} px")
with col2:
    after_file = st.file_uploader("After Image", type=["jpg", "png"], key="after")
    if after_file:
        after = Image.open(after_file).convert("RGB")
        st.write(f"✅ Uploaded: {after.size[0]}×{after.size[1]} px")

# Sensitivity slider for threshold
sensitivity = st.slider(
    "Detection Sensitivity",
    min_value=10,
    max_value=100,
    step=5,
    value=30,
    help="Adjust threshold for change detection (higher = less sensitive)."
)

# Validate images and detect changes
if before_file and after_file:
    if before.size != after.size:
        st.error("⚠️ Image dimensions do not match. Please upload aligned images of the same size.")
        st.stop()
    else:
        detect_btn = st.button("🚀 Detect Changes")
        if detect_btn:
            with st.spinner("Detecting removed objects..."):
                time.sleep(0.5)  # simulate processing

                before_np = cv2.cvtColor(np.array(before), cv2.COLOR_RGB2BGR)
                after_np = cv2.cvtColor(np.array(after), cv2.COLOR_RGB2BGR)

                gray_b = cv2.GaussianBlur(cv2.cvtColor(before_np, cv2.COLOR_BGR2GRAY), (5,5), 0)
                gray_a = cv2.GaussianBlur(cv2.cvtColor(after_np, cv2.COLOR_BGR2GRAY), (5,5), 0)
                diff = cv2.absdiff(gray_b, gray_a)
                _, thresh = cv2.threshold(diff, sensitivity, 255, cv2.THRESH_BINARY)
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
                cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
                contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                annotated = after_np.copy()
                count = 0
                for cnt in contours:
                    if cv2.contourArea(cnt) < 500:
                        continue
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(annotated, (x, y), (x + w, y + h), BOX_COLOR, 2)
                    count += 1

                annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
                result_img = Image.fromarray(annotated_rgb)

            st.success(f"✅ Done! Detected **{count}** removed object(s).")

            st.markdown("### Compare Before vs Detected Changes")
            image_comparison(
                img1=before,
                img2=result_img,
                label1="Before",
                label2="Detected Changes",
                width=700,
            )

            # Download result
            buf = BytesIO()
            result_img.save(buf, format="JPEG")
            st.download_button(
                "💾 Download Result",
                data=buf.getvalue(),
                file_name="detected_changes.jpg",
                mime="image/jpeg",
            )
else:
    st.info("Please upload both Before and After images to begin.")
