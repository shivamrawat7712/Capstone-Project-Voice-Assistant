<h2>The "Quick Start" Guide</h2>

<h3>1. Clone the Repo</h3>

Open the terminal and run:

PowerShell <br>
git clone https://github.com/shivamrawat7712/Capstone-Project.git <br>
cd Capstone-Project <br>

<h3>2. Create a Local Virtual Environment</h3>
Need to have own sandbox so it doesn't break your system's Python setup:
<br>
PowerShell <br>
python -m venv venv <br>
.\venv\Scripts\activate <br>

<h3>3. Install the Core Architecture</h3>
Since we didn't generate a requirements.txt file yet, just run this exact installation command to grab the libraries: <br>

PowerShell <br>
pip install SpeechRecognition openai-whisper edge-tts pygame <br>

<h3>⚠️ The Two "Gotchas"</h3>

Before you runs python test_voice.py, you need make sure about two things that will crash the system if you are'nt prepared: <br>

**The FFmpeg Requirement:** Whisper absolutely requires FFmpeg to translate the microphone audio. You must have FFmpeg downloaded and added to the Windows System Environment Variables, or the script will instantly throw an error.

**The Whisper Download:** The very first time you run the script, it is going to pause and download the 461MB small.en model. It might look frozen for a minute or two while it downloads. (If your C: drive is full like mine was, you will need to use your D: drive!).
