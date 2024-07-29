import requests
import json
import gradio as gr


url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(current_degree, family_condition, career_choice, current_skills):
    prompt = f"Current Degree: {current_degree}\nFamily Condition: {family_condition}\nCareer Choice: {career_choice}\nCurrent Skills: {current_skills}"
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "alvaron",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("error:", response.text)


# Custom CSS for the Gradio interface

# custom_css = """
# /* Background color of the interface */
# .gradio-container {
#     background-color: #4a148c; /* Light purple background */
#     color: #4a148c; /* Dark purple text color */
# }

# /* Style the input boxes */
# .gradio-container input[type="text"] {
#     border: 2px solid #4a148c; /* Dark purple border */
#     background-color: #e1bee7; /* Light purple input background */
#     color: #4a148c; /* Dark purple text color */
# }

# /* Style the output box */
# .gradio-container .output_text {
#     border: 2px solid #4a148c; /* Dark purple border */
#     background-color: #ede7f6; /* Lighter purple background */
#     color: #4a148c; /* Dark purple text color */
# }
# """



interface = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Textbox(lines=1, placeholder="Enter your Age/current degree", label="Age/Current Degree"),
        gr.Textbox(lines=1, placeholder="Describe your family condition", label="Family Condition"),
        gr.Textbox(lines=1, placeholder="What is your career choice?", label="Career Choice"),
        gr.Textbox(lines=1, placeholder="List your current skills", label="Current Skills")
    ],
    outputs="text",
    title="Code-Geass",
    # description="Enter your current degree, family condition, career choice, and current skills to receive personalized career advice.",
    # css=custom_css
)

interface.launch()