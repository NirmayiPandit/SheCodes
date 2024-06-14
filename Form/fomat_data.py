import pandas as pd
from gradio_client import Client

def read_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")

def format_data(data):
    formatted_data = []
    for _, row in data.iterrows():
        prompt = (f"I am a student with a CGPA of {row['CGPA']}, and I have completed courses in "
                  f"{row['Courses_Completed']}. My preferred field is {row['Preferred_Field']}, and my learning style is "
                  f"{row['Learning_Style']}. I would like to know what career goals I should aim for based on my academic "
                  f"performance and interests. My marks in DSA are {row['DSA_Marks']}, DBMS are {row['DBMS_Marks']}, "
                  f"ML are {row['ML_Marks']}, and Microcontroller are {row['Microcontroller_Marks']}. Can you suggest some "
                  f"relevant courses on Coursera or Udemy that align with my goals and interests with links? Can you give me some "
                  f"insights on what career goals I should aim for based on my academic performance and interests?")
        formatted_data.append(prompt)
    return formatted_data

def get_llm_response(prompt, client):
    try:
        result = client.predict(
            prompt, 
            "LLM Chat (no context from files)", 
            "You are a helpful assistant.", 
            api_name="/chat"  
        )
        return result
    except Exception as e:
        return f"An error occurred: {e}"

file_path = 'data\submissions.csv'  

data = read_file(file_path)
formatted_data = format_data(data)

client = Client("http://127.0.0.1:8001/")

responses = []

for prompt in formatted_data:
    response = get_llm_response(prompt, client)
    responses.append(response)

with open('llm_responses.txt', 'w') as f:
    for response in responses:
        f.write(response + '\n')

print("Responses saved to 'llm_responses.txt'")
