# 🤖 Android Kunjappan

Android Kunjappan is a **Malayalam-speaking AI chatbot** designed to help elderly people get accustomed to using Android phones without depending on others.  
It provides **simple text guidance** for common smartphone tasks, all in a warm and friendly tone.  

## ✨ Features

- 🗣 **Malayalam Voice Input** – Speak naturally and the bot understands you.  
- 🔊 **Malayalam Voice Output** – The bot replies with spoken Malayalam.  
- 💬 **Real-time AI Responses** – No fixed scripts; powered by AI for flexible answers.  
- 🖥 **Simple & Elder-Friendly UI** – Large buttons, clear text, and easy navigation.  
- 📜 **Chat History** – Messages appear like ChatGPT, newest at the bottom.  
- 🎨 **Custom Styling** – Transparent input background and neat help section.

## 🛠 Tech Stack

- **Python** – Core backend logic  
- **Streamlit** – User interface  
- **Anthropic Claude API** – AI-generated responses in Malayalam  
- **Text replies** – Malayalam  replies  



## 📂 Project Structure

```

android\_kunjappan/
├── app.py        # Main entry point
├── bot.py        # Chatbot logic and AI integration
├── ui.py         # UI elements and layout
├── requirements.txt
└── README.md

````

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/android_kunjappan.git
   cd android_kunjappan
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API keys**

   * Create a `.env` file and add your Claude API key:

     ```
     CLAUDE_API_KEY=your_api_key_here
     ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`

## 💡 Usage

* The bot replies in Malayalam text.
* Use it to learn everyday smartphone tasks, like:

  * 📸 How to take a photo
  * 📶 How to connect to Wi-Fi
  * 📞 How to make a call



**Made with ❤️ to bring technology closer to our elders.**

```




