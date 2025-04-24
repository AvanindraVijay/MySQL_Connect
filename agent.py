from langchain_community.llms import CTransformers
from db import fetch_user_details
import os

# Define the path to your local model
BASE_DIR = r"E:\DB_ChatLink"
MODEL_PATH = os.path.join(BASE_DIR, "model1", "llama-2-7b-chat.ggmlv3.q4_0.bin")

# Initialize the model with CTransformers
llm = CTransformers(
    model=MODEL_PATH,
    model_type="llama",
    config={
        'max_new_tokens': 256,
        'temperature': 0.7,
        'context_length': 2048
    }
)

def ask_ai(user_input):
    if "details of" in user_input.lower():
        # Extract the username from the input
        parts = user_input.lower().split("details of")
        if len(parts) > 1:
            user_name = parts[1].strip()
            user_info = fetch_user_details(user_name)
            
            if not user_info:
                return f"No record found for {user_name}"
                
            name, total_internships, companies, company_list, selected, rejected = user_info
            
            # Clean up None values in selected and rejected
            selected = selected if selected else "None"
            rejected = rejected if rejected else "None"
            
            return f"""
            Name: {name}
            Applied in {total_internships} internships across {companies} companies: {company_list}
            Selected in: {selected}
            Rejected in: {rejected}
            """
    else:
        # Use the local Llama model for general queries
        return llm.invoke(user_input)