# import the necessary packages
import os
import gradio as gr

# import the model
from src.models.llama import LLaMA

# import the dotenv file
import src.utils.dotenv

# ===================================================================
# Initialize the model
# ===================================================================

model_name = os.environ.get("MODEL_NAME", None)
use_gpu = os.environ.get("USE_GPU", "false").lower() == "true"

# Initialize the model
model = LLaMA(model_name, use_gpu=use_gpu)

# ===================================================================
# Interface definition
# ===================================================================

# Define the gradio interface. Find more information here:
# https://www.gradio.app/docs/

# Define the interface inputs
gr_inputs = [
    gr.Textbox(lines=3, placeholder="Insert prompt here...", label="Prompt"),
    gr.Slider(minimum=20, maximum=512, value=100, label="Max Length"),
    gr.Slider(minimum=0, maximum=1, value=0.8, step=0.01, label="Temperature"),
    gr.Slider(minimum=0, maximum=1, value=0.95, step=0.01, label="Top P"),
]

# Define the interface outputs
gr_outputs = gr.Textbox(lines=10, label="Output")

# Define the interface examples
gr_examples = [
    ["The problem with entity coreference resolution is", 120, 0.8, 0.95],
    ["The paper that introduced Multi-Head Attention", 40, 0.8, 0.95],
    ["The Pythagorean Theorem is defined as", 40, 0.8, 0.95],
]

# Define the interface
gr_iface = gr.Interface(
    fn=model.generate_text,
    inputs=gr_inputs,
    outputs=gr_outputs,
    examples=gr_examples,
    allow_flagging="never",
    title=f"LLaMA Demo ({model_name.split('/')[-1]})",
    description="This demo allows you to interact with the LLaMA model.",
)

if __name__ == "__main__":
    # ===============================================================
    # Server configuration and launch
    # ===============================================================

    server_name = os.environ.get("SERVER_NAME")
    server_port = int(os.environ.get("SERVER_PORT"))
    server_share = os.environ.get("SERVER_SHARE").lower() == "true"

    auth_username = os.environ.get("AUTH_USERNAME", None)
    auth_password = os.environ.get("AUTH_PASSWORD", None)

    gr_iface.launch(
        server_name=server_name,
        server_port=server_port,
        auth=(auth_username, auth_password)
        if auth_username and auth_password
        else None,
        share=server_share,
    )
