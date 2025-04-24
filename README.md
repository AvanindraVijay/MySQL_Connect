# MySQL_Connect

A terminal-based AI assistant that interacts with users to provide internship application details using natural language. It combines the power of a locally hosted LLaMA model via `CTransformers` and a MySQL backend to fetch internship data in real time.

---

## 🚀 Features

- 🔍 Query internship details using prompts like `show details of PMIS2025001`.
- 🧠 Uses LLaMA 2 model locally with `CTransformers` for natural language understanding.
- 🗄️ Fetches data from a MySQL database containing user and internship details.
- 🧑‍💻 Terminal-based interactive chatbot.
- 📦 Environment-friendly with offline model support.

---

## 📁 Project Structure

. ├── agent.py # Core logic to handle AI response and DB lookup ├── db.py # MySQL database connector and query executor ├── main.py # Entry-point CLI application ├── requirement.txt # Python dependencies └── README.md # You are here

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/internship-ai-chatbot.git
cd internship-ai-chatbot
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies
bash
Copy
Edit
pip install -r requirement.txt
4. Configure Environment
Create a .env file in the root directory (if needed for your setup).

5. Set up MySQL
Make sure your MySQL database is set up with:

Host: localhost

Port: 3306

User: bisag

Password: pmis

Database: pmis

And contains relevant tables:

user_details

user_internship

internship_details

6. Download LLaMA Model
Update the model path in agent.py:

python
Copy
Edit
BASE_DIR = r"E:\DB_ChatLink"
MODEL_PATH = os.path.join(BASE_DIR, "model1", "llama-2-7b-chat.ggmlv3.q4_0.bin")
Ensure the model file exists in that path.

🧠 Usage
Run the chatbot from the terminal:

bash
Copy
Edit
python main.py
Example prompts:

show details of PMIS2025001

What is AI?

📋 Sample Output
yaml
Copy
Edit
🤖 Internship AI Chatbot (Type 'exit' to quit)
--------------------------------------------------
You: show details of PMIS2025001
AI: 
Name: John Doe
Applied in 5 internships across 3 companies: Google, Microsoft, Amazon
Selected in: Google
Rejected in: Microsoft, Amazon
📜 License
This project is open-source and free to use under the MIT License.

🙋‍♂️ Author
Created by Avanindra Vijay

Feel free to connect or contribute!

yaml
Copy
Edit

---

Let me know if you want to tweak the tone, add badges, or make it suitable for Streamlit deployment too
