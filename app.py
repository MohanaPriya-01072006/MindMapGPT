import gradio as gr
import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate mind map using new OpenAI API
def generate_mindmap(topic):
    if topic.strip() == "":
        return "Please enter a topic."

    prompt = f"Create a detailed mind map with nodes, subnodes, and actionable steps for the topic: {topic}"

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates structured mind maps."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
with gr.Blocks(css="""
body {
    background: linear-gradient(120deg, #f6d365, #fda085);
    font-family: Arial, sans-serif;
}
.gradio-container {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 15px;
    padding: 25px;
    max-width: 800px;
    margin: auto;
}
h1 {
    color: #333;
    text-align: center;
}
button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 25px;
    font-size: 16px;
    border-radius: 8px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
""") as demo:

    gr.Markdown("# 🧠 MindMapGPT – AI-Powered Idea Brainstorming")
    
    with gr.Row():
        topic_input = gr.Textbox(label="Enter Your Topic", placeholder="Type your topic here...")
        generate_btn = gr.Button("Generate Mind Map")
    
    output_box = gr.Textbox(label="Generated Mind Map", lines=20)
    
    generate_btn.click(fn=generate_mindmap, inputs=topic_input, outputs=output_box)

demo.launch()
