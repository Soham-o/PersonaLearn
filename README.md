# 🧠 PersonaLearn: The Adaptive AI Tutor

> **Built in just 3 hours.** 🚀
> 
> A personalized learning platform that translates complex academic concepts into the language of your personal interests (Minecraft, Marvel, Cricket, and more).

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-8E75B2)

## 💡 The Problem
Cognitive science shows that retention improves significantly when new information is anchored to familiar mental models. However, standard textbooks are "one size fits all."

## 🛠️ The Solution
**PersonaLearn** uses Google's Gemini Pro to dynamically reframe syllabi (UPSC, School, General) into analogies based on the user's hobbies. 

* **Don't understand Trigonometry?** Read an explanation based on Cricket.
* **Confused by Blockchain?** Learn it through Minecraft block analogies.

## ✨ Key Features
* **Adaptive Syllabus:** Pre-loaded tracks for School, SSC, UPSC, and General Knowledge.
* **Interest Mapping:** Select your "lens" (e.g., K-Pop, Marvel, Cooking).
* **Dual Roles:** * 🎓 **Student Mode:** Learn and track progress.
    * 👨‍🏫 **Professor Mode:** Edit and curate the syllabus.
* **AI Quiz Generator:** Generates MCQs instantly based on the specific analogy used in the lesson.
* **Gamification:** Live scoring and progress tracking.

## 🚀 Quick Start

### Prerequisites
* Python 3.9+
* A Google Gemini API Key (Free tier available)

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/personalearn.git](https://github.com/yourusername/personalearn.git)
    cd personalearn
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up credentials**
    Create a `.env` file in the root directory:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    ```

4.  **Run the App**
    ```bash
    streamlit run main.py
    ```

## 📸 Screenshots

![image alt](https://github.com/Soham-o/PersonaLearn/blob/4ea980b69e0af30d47ec3894c9f0ff8d4977d9a3/Screenshot%202026-01-18%20122655.png)
![image alt](https://github.com/Soham-o/PersonaLearn/blob/4ea980b69e0af30d47ec3894c9f0ff8d4977d9a3/Screenshot%202026-01-18%20122834.png)

## 🏗️ How it Works
1.  **Input:** User selects a topic (e.g., "Photosynthesis") and an Interest (e.g., "Marvel").
2.  **Processing:** The app constructs a prompt for `gemini-pro` to explain the concept using the selected interest domain.
3.  **Output:** A translated explanation is displayed.
4.  **Assessment:** The AI dynamically generates a quiz based *only* on the explanation provided.
![image alt](https://github.com/Soham-o/PersonaLearn/blob/4ea980b69e0af30d47ec3894c9f0ff8d4977d9a3/Screenshot%202026-01-18%20123003.png)
## 👥 The Team
Built during a 3-hour rapid development sprint by:
* **[Innovsphere]** 
* **[Chaitanya]** 
* **[Nishant]** 
* **[Lavisha]** 
* **[Ayush]** 
* **[Soham]** 
## 📄 License
MIT License
