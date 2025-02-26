# 🖐️ Finger Counting using OpenCV & MediaPipe

This project detects and counts the number of fingers shown using a webcam. It utilizes **OpenCV** for video processing and **MediaPipe Hands** for real-time hand tracking. The system is designed to recognize individual fingers and display separate finger counts for both hands.

---

## 🚀 Features  
- **Hand Detection:** Identifies left and right hands separately.  
- **Finger Counting:** Detects the number of fingers extended for each hand.  
- **Colored Markers:** Highlights fingertips for better visibility.  
- **Mirrored Display:** Applies a mirror effect for a more natural user experience.  
- **Real-time Processing:** Ensures smooth and accurate tracking.  

---

## 🖥️ How It Works?  
1. **Capture Webcam Feed**:  
   - The program starts the webcam and continuously captures video frames.  

2. **Detect Hands Using MediaPipe**:  
   - MediaPipe detects hands and assigns **21 landmarks** to each detected hand.  

3. **Apply a Mirror Effect**:  
   - The camera feed is flipped horizontally so it feels natural to the user.  

4. **Identify Fingers**:  
   - The program checks if each finger is **open or closed** by comparing the **tip position** with other finger joints.  

5. **Count Fingers Separately for Each Hand**:  
   - The number of extended fingers is displayed for both left and right hands.  

6. **Show Colored Fingertip Markers**:  
   - Colored circles are drawn on detected fingertips for better visualization.  

7. **Exit Condition**:  
   - The program keeps running until the user **presses 'Q'** to exit.  

---

## 📦 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/dishapawarkhausi/hand-tracking-ai.git
cd hand-tracking-ai/fingers-counting
