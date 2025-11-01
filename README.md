# Voice Assistant

A simple voice assistant built using Python that can recognize speech and execute various commands such as opening Google Chrome, telling the current time, and playing videos on YouTube.

## Features

- **Open Chrome**: Launch Google Chrome.
- **Tell Time**: Provide the current time.
- **Play YouTube Videos**: Search and play videos on YouTube.
- **Open YouTube**: Open YouTube homepage in the default web browser.

## Requirements

- Python 3.6+
- `speech_recognition` library
- `pyttsx3` library
- `pywhatkit` library
- `pyaudio` library (for microphone access)
- A working internet connection

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/voice-assistant.git
    cd voice-assistant
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure you have `PyAudio` installed. If not, you may need to install it separately. For Windows, you can download the appropriate `.whl` file from [PyAudio's website](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using:
    ```sh
    pip install path/to/downloaded/whl
    ```

## Usage

1. Run the voice assistant script:
    ```sh
    python voice_assistant.py
    ```

2. Speak commands clearly when prompted. For example:
    - "Open Chrome"
    - "What is the time?"
    - "Play Despacito on YouTube"
    - "Open YouTube"

## File Structure

- `voice_assistant.py`: The main script containing the voice assistant logic.

## Code Overview

### Initialization

- Initializes the text-to-speech engine (`pyttsx3`).
- Sets the voice property to the second available voice (usually female).

### Listening for Commands

- Uses the `speech_recognition` library to capture audio from the microphone and recognize speech.

### Command Handling

- Executes different commands based on recognized keywords:
  - **Chrome**: Opens Google Chrome.
  - **Time**: Announces the current time.
  - **Play**: Plays a video on YouTube using the `pywhatkit` library.
  - **YouTube**: Opens YouTube in the web browser.

### Continuous Listening

- A `while` loop keeps the assistant active and continuously listens for commands.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)

## Troubleshooting

If you encounter issues with the microphone or audio recognition, ensure that:
- Your microphone is properly connected and recognized by the system.
- You have installed `PyAudio` correctly.
- Background noise is minimized during the recognition process.

For further assistance, please open an issue on the GitHub repository.
