# 🏔️ Zenith AI Fitness Companion

**Live Demo:** [zenith-ai-fitness.streamlit.app](https://zenith-ai-fitness.streamlit.app/)

**Zenith AI** is a premium, 2026-standard fitness and nutrition agent built to help users reach their peak physical potential. Unlike static planners, Zenith adapts in real-time to your equipment, energy levels, and dietary preferences.

![Zenith AI Banner](https://img.icons8.com/fluency/96/mountain.png)

## 🚀 Key Features

- **Metabolic Autopilot**: Dynamically pivots your workout and diet plan based on daily recovery, soreness, and fatigue levels.
- **Omnichannel Training**: Instantly adapts your daily workout for "Gym Mode" or "Home/Hotel Mode" based on available equipment.
- **Global Dietary Support**: Native support for cultural diets like **Indian Vegetarian**, Jain, Vegan, and more.
- **Smart Meal Swapping**: High-precision meal replacements that maintain your specific macronutrient targets.
- **Premium Glassmorphism UI**: A high-visibility, dark-mode interface designed for use in active environments.

## 🛠️ Tech Stack

- **Core Engine**: [Llama 3.3-70B](https://groq.com/) via Groq Cloud
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Styling**: Custom CSS (Glassmorphism & High-Visibility Design)

## 📦 Installation & Setup

To run Zenith AI locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/manavmodi123/zenith-ai-fitness.git
   cd zenith-ai-fitness
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your **Groq API Key**:

   ```
   GROQ_API_KEY=your_groq_api_key
   ```

4. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

### Usage

- Enter your fitness and diet details, such as workout type, diet type, current weight, target weight, and other information.
- Click "Generate Plans" to receive personalized diet and workout plans.
- Use the interactive chat interface to ask questions and refine your plans further.

## Code Explanation

- **Streamlit UI**: The front-end of the app is created using Streamlit, which allows for easy deployment and a clean user interface.
- **LangChain**: We use LangChain to interface with the **llama-3.3-70b-versatile model** hosted on **Groq Cloud** to generate customized plans.
- **Chat Interface**: Users can ask the system questions about their plans, and the system provides real-time answers based on the generated plan.


## Contributing

Feel free to open issues or submit pull requests to improve this project. Contributions are welcome!





