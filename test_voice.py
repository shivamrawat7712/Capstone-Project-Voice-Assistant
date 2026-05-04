import speech_recognition as sr
import edge_tts
import asyncio
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class VoiceAssistant:
    def __init__(self):
        # --- TTS Settings ---
        # "en-US-AriaNeural" = Female (Friday vibes)
        # "en-GB-RyanNeural" = Male British (Jarvis vibes)
        self.voice = "en-US-AriaNeural" 
        
        # --- STT Settings ---
        self.recognizer = sr.Recognizer()

    def speak(self, text: str):
        """Generates AI audio and plays it instantly."""
        print(f"Assistant: {text}")
        
        audio_file = "response.mp3"
        
        # 1. Generate the audio file asynchronously
        asyncio.run(self._generate_audio(text, audio_file))
        
        # 2. Play the audio file
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # 3. Wait for the audio to finish playing before moving on
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # 4. Clean up the system by unloading and deleting the temp file
        pygame.mixer.music.unload()
        pygame.mixer.quit()
        if os.path.exists(audio_file):
            os.remove(audio_file)

    async def _generate_audio(self, text: str, output_file: str):
        """Calls the Edge-TTS API to generate the hyper-realistic voice."""
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)

    def listen(self) -> str:
        with sr.Microphone() as source:
            print("\nListening... (Speak now!)")
            self.recognizer.adjust_for_ambient_noise(source, duration=1.0)
            self.recognizer.dynamic_energy_threshold = True  
            self.recognizer.pause_threshold = 2.0 

            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=None)
                
                print("Processing with OpenAI Whisper...")
                text = self.recognizer.recognize_whisper(
                    audio, 
                    model="small.en", 
                    load_options={"download_root": "./models"}
                )
                
                print(f"You said: {text}")
                return text.lower().strip()
                
            except sr.UnknownValueError:
                print("Whisper could not understand the audio.")
                return ""
            except Exception as e:
                print(f"Error: {e}")
                return ""

# --- Test Execution ---
if __name__ == "__main__":
    agent = VoiceAssistant()
    
    agent.speak("System upgrade complete. I am now fully operational with AI voice capabilities. What would you like to test next?")
    
    user_input = agent.listen()
    
    if user_input:
        agent.speak(f"I processed your command. You said: {user_input}")
    else:
        agent.speak("I didn't catch that, but my audio output is working perfectly.")