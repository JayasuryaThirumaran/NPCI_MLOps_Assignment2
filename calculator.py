import gradio as gr

# Function for performing calculations
def calculator(a, b, operation):
    try:
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
        else:
            return "Invalid operation"
        return f"{result}"
    except ValueError:
        return "Error: Please enter valid numbers."

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Simple Calculator ")
    with gr.Row():
        a_input = gr.Number(label="First Number")
        b_input = gr.Number(label="Second Number")
    operation_input = gr.Radio(
        ["add", "subtract", "multiply", "divide"], label="Operation"
    )
    result_output = gr.Textbox(label="Result")
    calculate_button = gr.Button("Calculate")
    calculate_button.click(calculator, inputs=[a_input, b_input, operation_input], outputs=result_output)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=5000)

