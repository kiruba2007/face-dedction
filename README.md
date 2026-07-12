# 👤 Face Detection using OpenCV

A real-time face detection project built with Python and OpenCV, using the Haar Cascade Classifier algorithm to detect faces through a webcam feed.

---

## 📸 Demo

The program opens your webcam, detects faces in real time, and draws a red rectangle around each detected face.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV (cv2)** — Computer vision library
- **Haar Cascade Classifier** — Pre-trained face detection algorithm

---

## 📁 Project Structure

```
face-detection/
│
├── face_detection.py               # Main Python script
├── haarcascade_frontalface_default.xml  # Pre-trained Haar Cascade model
└── README.md                       # Project documentation
```

---

## ⚙️ Requirements

Install the required library using pip:

```bash
pip install opencv-python
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/face-detection.git
   cd face-detection
   ```

2. **Make sure the Haar Cascade XML file is in the same folder** as the script.
   You can download it from the [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) if it's missing.

3. **Run the script**
   ```bash
   python face_detection.py
   ```

4. **Press `Esc`** to close the webcam window and exit.

---

## 🧠 How It Works

1. The script loads the pre-trained `haarcascade_frontalface_default.xml` model.
2. It captures live video from your webcam using `cv2.VideoCapture(0)`.
3. Each frame is converted to grayscale for faster processing.
4. `detectMultiScale()` scans the frame and returns coordinates of detected faces.
5. A red rectangle is drawn around each detected face using `cv2.rectangle()`.
6. The processed frame is displayed in a window called **"FaceDetection"**.

---

## 🔧 Troubleshooting

| Problem | Solution |
|--------|----------|
| Camera not opening | Change `VideoCapture(0)` to `VideoCapture(1)` or `VideoCapture(2)` |
| `cv2.error: !_src.empty()` | Camera feed is empty — check camera index or permissions |
| XML file not found | Make sure `haarcascade_frontalface_default.xml` is in the same folder as the script |
| `ModuleNotFoundError: cv2` | Run `pip install opencv-python` |

---

## 📌 Notes

- Default camera index is `0` (built-in webcam). Change to `1` for an external webcam.
- Works best in good lighting conditions.
- The Haar Cascade method is fast but may have reduced accuracy compared to deep learning methods.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**R.kirubba sri**  
Feel free to connect or contribute!
