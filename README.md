**The "Quick Start" Guide**

**1. Clone the Repo**
Open the terminal and run:

PowerShell
git clone https://github.com/shivamrawat7712/Capstone-Project.git
cd Capstone-Project

**2. Create a Local Virtual Environment**
Need to have own sandbox so it doesn't break your system's Python setup:

PowerShell
python -m venv venv
.\venv\Scripts\activate

**3. Install the Core Architecture**
Since we didn't generate a requirements.txt file yet, just run this exact installation command to grab the libraries:

PowerShell
pip install SpeechRecognition openai-whisper edge-tts pygame

⚠️ The Two "Gotchas"
Before you runs python test_voice.py, you need make sure about two things that will crash the system if you are'nt prepared:

The FFmpeg Requirement: Whisper absolutely requires FFmpeg to translate the microphone audio. You must have FFmpeg downloaded and added to the Windows System Environment Variables, or the script will instantly throw an error.

The Whisper Download: The very first time you run the script, it is going to pause and download the 461MB small.en model. It might look frozen for a minute or two while it downloads. (If your C: drive is full like mine was, you will need to use your D: drive!).
