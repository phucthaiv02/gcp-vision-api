import gradio as gr
from api import ocr

interface = gr.Interface(fn=ocr,
                         inputs=gr.Image(type="filepath"),
                         outputs=gr.Label(),
                         examples=[])

interface.launch()
