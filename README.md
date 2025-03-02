# 🎭 Emoji Recommendation System via FaceMesh

## 📌 Overview
This project is an **AI-powered emoji recommendation system** that detects a user's facial emotions in real time using **MediaPipe FaceMesh** and **CNN-based emotion classification models**. Based on detected emotions, the system dynamically suggests relevant emojis.

## 🚀 Features
- **Real-time facial emotion detection** using **MediaPipe FaceMesh**.
- **CNN-based classification** for recognizing emotions (Happy, Sad, Angry, etc.).
- **Emoji recommendations** based on detected emotions.
- **User-friendly UI** for displaying detected emotions and suggested emojis.
- **Optimized for real-time processing** with low latency.

## 🛠️ Technologies Used
- **Python** (OpenCV, NumPy, TensorFlow, Keras)
- **MediaPipe FaceMesh** (for facial landmark detection)
- **Flask** (for backend API)
- **JavaScript, HTML/CSS** (for frontend UI)
- **TensorFlow/Keras** (for training the emotion classification model)

## 🔧 Installation & Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/adithyapranav/Application-for-Emoji-recommendations-based-on-facial-emotions.git
   cd Application-for-Emoji-recommendations-based-on-facial-emotions
2. **Install dependencies:**:
   ```sh
   pip install -r requirements.txt
3. **Run the application:**:
   ```sh
   python app.py
4. **Access the web interface:**:
   ```sh
   http://localhost:5000

## 📊 Model Training
- The emotion classification model was trained on the FER2013 dataset using a CNN architecture.
- Achieved high accuracy in recognizing emotions such as Happy, Sad, Angry, etc.
- Model fine-tuned using Transfer Learning for better results.

## 🏆 Future Improvements
- Enhance classification accuracy using RNN models.
- Optimize for mobile deployment.
- Deploy using FastAPI for better performance.

## 🤝 Contributing

- Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

- **MIT License © 2025 Adithya Mahesh**

