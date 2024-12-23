import gradio as gr
import pandas as pd
import numpy as np
from statistics import mode, median

# Sample dataset for column operations
data = pd.read_csv("dataset.csv")
# Calculator function for basic arithmetic
def calculator(a, b, operation):
    try:
        if operation in ["sqrt", "tan", "sin", "cos"]:
            a = float(a)
            if operation == "sqrt":
                result = np.sqrt(a)
            elif operation == "tan":
                result = np.tan(np.radians(a))
            elif operation == "sin":
                result = np.sin(np.radians(a))
            elif operation == "cos":
                result = np.cos(np.radians(a))
        else:
            a = float(a)
            b = float(b)
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return "Error: Division by zero"
                result = a / b
            elif operation == "modulus":
                result = a % b
            else:
                return "Invalid operation"
        return f"{result}"
    except ValueError:
        return "Error: Please enter valid numbers."

# Column operations function
def column_operations(column, operation):
    try:
        col_data = data[column]
        if operation == "Standard Deviation":
            result = np.std(col_data)
        elif operation == "Mode":
            result = mode(col_data)
        elif operation == "Median":
            result = median(col_data)
        else:
            return "Invalid operation selected."
        return f"The {operation.lower()} of column '{column}' is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Combined Calculator App")

    # Section 1: Basic Arithmetic Calculator
    with gr.Row():
        gr.Markdown("### Arithmetic Calculator")
    with gr.Row():
        a_input = gr.Number(label="First Number")
        b_input = gr.Number(label="Second Number")
    operation_input = gr.Radio(
        ["add", "subtract", "multiply", "divide", "modulus", "sqrt", "tan", "sin", "cos"],
        label="Operation"
    )
    result_output = gr.Textbox(label="Result")
    calculate_button = gr.Button("Calculate")

    # Section 2: Column Operations
    gr.Markdown("### Column Operations")
    with gr.Row():
        column_dropdown = gr.Dropdown(choices=data.columns.tolist(), label="Select Column")
        column_operation_input = gr.Radio(
            ["Standard Deviation", "Mode", "Median"], label="Operation"
        )
    column_result_output = gr.Textbox(label="Result")
    column_calculate_button = gr.Button("Calculate Column Operation")

    # Link Functions to Buttons
    calculate_button.click(calculator, 
                           inputs=[a_input, b_input, operation_input], 
                           outputs=result_output)
    column_calculate_button.click(column_operations, 
                                  inputs=[column_dropdown, column_operation_input], 
                                  outputs=column_result_output)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=6080)
