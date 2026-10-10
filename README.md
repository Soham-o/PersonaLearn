# 🧠 PersonaLearn: The Adaptive AI Tutor

> A Streamlit prototype that explains study topics through analogies drawn
> from a learner's interests (Minecraft, Marvel, Cricket, Cooking, K-Pop),
> then quizzes them in the same context. Built by Team Innovsphere during a
> 3-hour team sprint.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-8E75B2)
![Status](https://img.shields.io/badge/status-prototype-orange)

## 💡 The Problem
New ideas are easier to remember when they are tied to something you already
know well. Standard textbooks explain every topic the same way for every
reader.

## 🛠️ The Solution
**PersonaLearn** sends each topic to Google Gemini with a prompt that asks for
an explanation framed around the learner's chosen interest.

* **Don't understand Trigonometry?** Read an explanation based on Cricket.
* **Confused by Blockchain?** Learn it through Minecraft block analogies.

## ✨ Key Features
* **Preset syllabi:** Topic lists for School, SSC, UPSC, and General Knowledge.
* **Interest mapping:** Choose an analogy theme (Minecraft, Cricket, Marvel, Cooking, K-Pop) plus length and complexity.
* **Two views:**
    * 🎓 **Student view:** Learn topics, mark them complete, and see a quiz score.
    * 👨‍🏫 **Professor view:** Add or remove syllabus topics.
* **AI quiz generator:** Generates a multiple-choice question from the explanation that was just shown.
* **Scoring:** Running score and quiz count for the current session.

## 🚀 Quick Start

### Prerequisites
* Python 3.9+
* A Google Gemini API key ([Google AI Studio](https://aistudio.google.com/))

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Soham-o/PersonaLearn.git
    cd PersonaLearn
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up credentials**
    Create a `.env` file in the root directory (do not commit it):
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    ```
    If no key is set, the sidebar asks for one when the app starts.

4.  **Run the app**
    ```bash
    streamlit run main.py
    ```

## 📸 Screenshots

![PersonaLearn landing page](Screenshot%202026-01-18%20122655.png)
![PersonaLearn explaining Trigonometry through a Cricket analogy](Screenshot%202026-01-18%20122834.png)

## 🏗️ How it Works
1.  **Input:** The user picks a topic (e.g., "Photosynthesis") and an interest (e.g., "Marvel").
2.  **Processing:** The app builds a prompt and sends it to Gemini through the `google-generativeai` SDK (`gemini-2.5-flash`).
3.  **Output:** The interest-based explanation is displayed.
4.  **Assessment:** Gemini generates a quiz question based on that explanation.

![PersonaLearn multiple-choice quiz generated from the Cricket explanation, answered correctly](Screenshot%202026-01-18%20123003.png)

## ⚠️ Limitations
* **Prototype:** built in a short sprint; there are no automated tests.
* **No accounts or persistence:** Student/Professor is a view toggle, not a login, and progress, scores and syllabus edits are lost when the session ends.
* **Deprecated SDK:** `google-generativeai` no longer receives updates. Migrating to Google's `google-genai` package is recommended.
* **AI output is not fact-checked:** explanations and quiz answers come straight from the model.

## 👥 Team Innovsphere
Built during a 3-hour rapid development sprint by:
* **Chaitanya**
* **Nishant**
* **Lavisha**
* **Ayush**
* **Soham**

## 📄 License
No license file has been added yet. Until one is, all rights are reserved by
the authors.
