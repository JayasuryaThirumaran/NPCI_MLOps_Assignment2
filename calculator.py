import gradio as gr
import math
import numpy as np
import sympy as sp
from scipy import integrate

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
        elif operation == "modulus":
            result = a % b
        elif operation == "exponentiate":
            result = a ** b
        elif operation == "sqrt":
            if a < 0:
                return "Error: Square root of negative number is not allowed"
            result = math.sqrt(a)  # Square root of first number (a)
        elif operation == "sin":
            result = np.sin(np.radians(a))  # Sin of angle (a)
        elif operation == "cos":
            result = np.cos(np.radians(a))  # Cosine of angle (a)
        elif operation == "tan":
            result = np.tan(np.radians(a))  # Tangent of angle (a)
        elif operation == "log":
            if a <= 0:
                return "Error: Logarithm of non-positive number is not defined"
            result = np.log(a)  # Natural log of a
        elif operation == "integrate":
            # Simple integration example using scipy
            result = integrate.quad(lambda x: x ** 2, 0, a)  # Integrate x^2 from 0 to a
            result = result[0]  # Take the result from the tuple       
        elif operation == "sympy_eq":
            # Symbolic equation solving using sympy
            x = sp.symbols('x')
            equation = sp.Eq(x**2 - a, 0)
            result = sp.solve(equation, x)
        else:
            return "Invalid operation"
        
        return f"{result}"
    except ValueError:
        return "Error: Please enter valid numbers."

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Advanced Calculator with Extra Features")
    with gr.Row():
        a_input = gr.Number(label="First Number")
        b_input = gr.Number(label="Second Number")
    operation_input = gr.Radio(
        [
            "add", "subtract", "multiply", "divide", "modulus", "exponentiate", 
            "sqrt", "sin", "cos", "tan", "log", "integrate", "plot", "sympy_eq"
        ],
        label="Operation"
    )
    result_output = gr.Textbox(label="Result")
    image_output = gr.Image(label="Plot Image", visible=False)
    calculate_button = gr.Button("Calculate")
    
    calculate_button.click(calculator, inputs=[a_input, b_input, operation_input], 
                           outputs=[result_output, image_output])

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=5000)
