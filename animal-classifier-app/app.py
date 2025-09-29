import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd
from knowledge_base import ANIMAL_INFO # Make sure knowledge_base.py is in the same folder

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Wildlife Identifier",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- TFLITE MODEL LOADING ---
@st.cache_resource
def load_model():
    """Load the TFLite model and allocate tensors."""
    try:
        interpreter = tf.lite.Interpreter(model_path="model_quantized.tflite")
        interpreter.allocate_tensors()
        return interpreter
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

interpreter = load_model()

# --- CLASS NAMES ---
class_names = [
    'antelope', 'badger', 'bat', 'bear', 'bee', 'beetle', 'bison', 'boar',
    'butterfly', 'cat', 'caterpillar', 'chimpanzee', 'cockroach', 'cow',
    'coyote', 'crab', 'crow', 'deer', 'dog', 'dolphin', 'donkey',
    'dragonfly', 'duck', 'eagle', 'elephant', 'flamingo', 'fly', 'fox',
    'goat', 'goldfish', 'goose', 'gorilla', 'grasshopper', 'hamster',
    'hare', 'hedgehog', 'hippopotamus', 'hornbill', 'horse', 'hummingbird',
    'hyena', 'jellyfish', 'kangaroo', 'koala', 'ladybugs', 'leopard',
    'lion', 'lizard', 'lobster', 'mosquito', 'moth', 'mouse', 'octopus',
    
    'okapi', 'orangutan', 'otter', 'owl', 'ox', 'oyster', 'panda',
    'parrot', 'pelecaniformes', 'penguin', 'pig', 'pigeon', 'porcupine',
    'possum', 'raccoon', 'rat', 'reindeer', 'rhinoceros', 'sandpiper',
    'seahorse', 'seal', 'shark', 'sheep', 'snake', 'sparrow', 'squid',
    'squirrel', 'starfish', 'swan', 'tiger', 'turkey', 'turtle', 'whale',
    'wolf', 'wombat', 'woodpecker', 'zebra'
]

# --- IMAGE PREPROCESSING ---
def preprocess_image(image, input_details):
    """Preprocess the uploaded image to fit TFLite model input requirements."""
    # Get input size and type
    input_shape = input_details[0]['shape'][1:3]
    img = image.resize(input_shape)
    img_array = np.array(img, dtype=np.float32) # Input type is float32
    img_array = np.expand_dims(img_array, axis=0)
    
    # Pre-processing specific to MobileNetV2 (scales pixel values to -1..1)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array

# --- UI LAYOUT ---
with st.sidebar:
    st.title("🔬 AI Wildlife Identifier")
    st.markdown("---")
    uploaded_file = st.file_uploader("Upload an image for analysis", type=["jpg", "jpeg", "png"])
    with st.expander("About this App"):
        st.write("""
            This application uses a quantized MobileNetV2 model to identify animal species and provide conservation context.
        """)

st.header("Image Analysis Dashboard")

if uploaded_file is None:
    st.info("Please upload an image using the sidebar to begin analysis.")
else:
    image = Image.open(uploaded_file)
    
    if interpreter is not None:
        # Get input and output tensor details
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        # Preprocess the image and set the tensor
        processed_image = preprocess_image(image, input_details)
        interpreter.set_tensor(input_details[0]['index'], processed_image)
        
        # Run inference
        interpreter.invoke()
        
        # Get the prediction
        prediction = interpreter.get_tensor(output_details[0]['index'])[0]

        # Post-process the prediction
        top_k_indices = np.argsort(prediction)[::-1][:5]
        top_k_probs = prediction[top_k_indices]
        top_k_names = [class_names[i].capitalize() for i in top_k_indices]
        top_prediction_name = top_k_names[0]
        animal_data = ANIMAL_INFO.get(top_prediction_name, ANIMAL_INFO["Default"])

        # --- DISPLAY RESULTS IN TABS ---
        tab1, tab2, tab3 = st.tabs(["**📷 Specimen Analysis**", "**📊 Detailed Prediction**", "**📖 Animal Profile**"])
        with tab1:
            st.image(image, caption="Uploaded Specimen", use_column_width=True)
            st.metric(label="**Top Prediction**", value=top_prediction_name, delta=f"{top_k_probs[0]*100:.2f}% Confidence")
        with tab2:
            st.subheader("Top 5 Model Predictions")
            results_df = pd.DataFrame({'Species': top_k_names, 'Confidence': top_k_probs})
            st.bar_chart(results_df.set_index('Species'))
        with tab3:
            st.subheader(f"Profile: {top_prediction_name}")
            st.markdown(f"#### {animal_data['title']}")
            st.markdown("##### Key Features")
            st.info(animal_data['details']['features'])
            st.markdown("##### Population Insight")
            st.warning(animal_data['details']['population'])
            st.markdown("##### Preservation Focus")
            st.success(animal_data['details']['preservation'])