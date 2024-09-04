Here's the updated README with the additional information about your Docker Hub repository:

---

# 🎲 Number Guessing Game

Welcome to my **Number Guessing Game**! This is my second Python project. In this game, you'll try to guess a randomly generated number between 1 and 10. 🎉

## Features

- 🎯 Generates a random number between 1 and 10.
- ✅ Validates user input to ensure it’s within the specified range.
- 🚫 Provides error messages for invalid input.
- 🚀 Can be run using Python or Docker.

## Getting Started

### Prerequisites

- **Python** (version 3.x) installed on your machine. You can download Python from the [official Python website](https://www.python.org/downloads/). 🐍
- **Docker** installed on your machine. Follow the installation guide on the [Docker website](https://docs.docker.com/get-docker/). 🐳

### Running the Game

#### Using Python
## Cloning the Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/Ayesha-Shakoor-94/python-learning-journey.git

2. **Navigate to the Project Directory**:
    ```bash
    
    cd python-learning-journey

    ```

#### Using Docker

1. **Build the Docker Image**: Create a Docker image from the Dockerfile provided in the project.
    ```bash
    docker build -t number-guessing-game .
    ```

2. **Run the Docker Container**: Start a container from the Docker image you built.
    ```bash
    docker run -it number-guessing-game
    ```

### Pulling the Docker Image from Docker Hub

1. **Pull the Image**: You can pull the image from Docker Hub if you want to test it without building it yourself. Run the following command:
    ```bash
    docker pull ashu2445/guessing_game:latest
    ```

2. **Run the Pulled Image**: Start a container from the pulled image.
    ```bash
    docker run -it ashu2445/guessing_game:latest
    ```

## Code Overview

- 🎲 **Random Number Generation**: Generates a random integer between 1 and 10 each time the game is played.
- 🤔 **User Input**: Prompts the user to guess a number and ensures it is within the valid range.
- 🚫 **Validation**: Shows an error message if the input is out of range and continues to ask for a valid input until the correct number is guessed.

## Example Code

Here’s a simple example of the game:

```python
import random

# 🎉 Welcoming message
print('Welcome to Code_With_Ashu Number Guessing Game')

def guessgame() -> None:
    while True:
        # 🎲 Generating a random number between 1 and 10
        random_number: int = random.randint(1, 10)
        
        # 🤔 Asking the user to guess a number
        user_guess: int = int(input('Guess a number between 1 & 10: '))

        # 🚫 Checking if the guessed number is out of range
        if user_guess < 1 or user_guess > 10:
            print('Error: Please enter a number between 1 and 10.')
            continue

        # 🎉 Checking if the guessed number is correct
        if random_number != user_guess:
            print('Wrong Guess. Please try again...!')
        else:
            print("Congrats! Your guessed number is correct. 🎉")
            break

# 🚀 Starting the game
guessgame()
```

## Docker Hub Repository

I have created and pushed this Docker image to Docker Hub for practice and learning purposes. You can pull the image and run it on your local machine from my Docker Hub profile: [ashu2445/guessing_game](https://hub.docker.com/r/ashu2445/guessing_game).

---