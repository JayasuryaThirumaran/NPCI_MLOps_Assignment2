## Assignment-2 : Dockerizing Calculator application

In this task, you will containerize a Python-based calculator app Your objective is to check the provided calculator.py file, identify the required Python dependencies, document them in requirements.txt, and create a Dockerfile to containerize the application.

### Objective

1. Understand and document the Python dependencies for the calculator.py app.
2. Create a requirements.txt file with the required packages.
3. Write a Dockerfile to containerize the calculator app.
4. Build and run the Docker container, and interact with the calculator app.

### Steps to Complete the Assignment

1. Examine the calculator.py File
    - Open the calculator.py file provided in this repository.
    - Review the code and identify all the Python libraries used in the app.

2. Create the requirements.txt File
    - Write down the required dependencies for the app along with their versions (if applicable) in a file named requirements.txt.

3. Write a Dockerfile
Create a Dockerfile to containerize the app.

The Dockerfile should:
   - Use a Python base image (e.g., python:3.9-slim).
   - Copy the calculator.py and requirements.txt files into the container.
   - Install the dependencies using pip install -r requirements.txt.
   - Expose the required port (e.g., 5000 for Gradio apps).
   - Run the calculator.py script.
4.Build the docker image and run a container.

5.Test the calculator.


Note:
  - for testing functions like "sqrt", "sin", "cos", "tan" which takes single input , keep the second number as 0.
