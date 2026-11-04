from __future__ import annotations
import msvcrt
import sys
 
from gump.core.agent_orc import Agent

class GumpUi:
    def __init__(self):
        self.running=True

    def get_sentence(self, prompt="Enter text: "):
        print(prompt, end="", flush=True)
        sentence = []

        while True:
            char_byte = msvcrt.getch()

            # Ctrl+Q: Exit immediately
            if char_byte == b'\x04':
                print("\nGoodbye!")
                self.running = False
                return None

            # Enter
            elif char_byte == b'\r':
                print()
                break

            # Backspace
            elif char_byte == b'\x08':
                if sentence:
                    sentence.pop()
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()

            # CRT+N Next line        
            elif char_byte == b'\x0e':
                sentence.append('\n')
                print()

            # Printable ASCII
            elif b' ' <= char_byte <= b'~':
                char = char_byte.decode('ascii')
                sentence.append(char)
                sys.stdout.write(char)
                sys.stdout.flush()

        return "".join(sentence)
    def start_gump(self):
        print("GUMP interactive mode. Type a request and press Enter; Ctrl-D or 'exit' to exit.")

        while self.running:
            command=self.get_sentence("GUMP >")
            if command is None:
                break
            self.handle_start(command)

    def handle_start(self,command):
        agent=Agent()
        if command=="help":
            print("bro you are on you'er own")
        elif command=="exit":
            self.running=False
            print("bye Nigga....")
        else:
            agent.agent_loop()
        