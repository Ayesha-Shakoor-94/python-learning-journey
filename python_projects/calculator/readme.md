
# 🧮 Python Calculator

## Overview

Welcome to my Python calculator project! 🖥️ This repository features a simple calculator application written in Python. It supports basic arithmetic operations like addition, subtraction, multiplication, division, modulus, exponentiation, and floor division. The project also includes a Docker setup for easy containerized execution. 🚀

## Project Files

- **`calculator.py`**: Contains the core logic of the calculator. 📝
- **`Dockerfile`**: Defines the Docker image setup. 🐳
- **`.devcontainer/devcontainer.json`**: Configuration for Visual Studio Code Dev Containers. 🛠️

## Setup

### Local Setup

1. **Clone the Repository** 🖱️

   ```sh
   git clone https://github.com/yourusername/python_calculator.git
   cd python_calculator
   ```

2. **Run the Application** 🏃‍♂️

   Make sure Python 3.12 is installed, then execute:

   ```sh
   python calculator.py
   ```

### Docker Setup (Optional)

1. **Build the Docker Image** 🏗️

   ```sh
   docker build -t python_calculator .
   ```

2. **Run the Docker Container** 🚢

   ```sh
   docker run -it python_calculator
   ```

### Development with VS Code

1. **Open the Project in VS Code** 💻

   Open the project directory in Visual Studio Code.

2. **Use the Dev Container** 🧩

   If you have the Remote - Containers extension installed, you can open the project in a containerized environment:

   - Press `F1` or `Ctrl+Shift+P`, type `Remote-Containers: Reopen in Container`, and select it.

## Usage

Run the application and select an operation from the menu:

```
1 - Addition ➕
2 - Subtraction ➖
3 - Multiplication ✖️
4 - Division ➗
5 - Modulus 🔢
6 - Exponentiation ʸ
7 - Floor Division ⌊ ⌋  
8 - Exit 🚪
```

Input two numbers to perform the selected operation.

## About Me

I’m a beginner learning Python 🐍 and this is my first project. I’m excited to explore Python and build more applications as I progress. 🚀
