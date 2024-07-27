import time
import keyboard
import sys
import logging
from record import Record
from snap import is_Snap,Load
import torchaudio   
from homeassistant_api import Client   
api_server = 'localhost:8123/api' # Replace with your homeassistant_api url
access_token = ''# Replace with your home assistant token
light_entity_id = ''  # Replace with your light entity ID
def toggle_light():
        with Client(api_server, access_token) as client:
            light = client.get_domain("light")
            state=client.get_state(entity_id=light_entity_id)
            print('State:',state.state)
            if(state.state == 'off'):
                light.turn_on(entity_id=light_entity_id)
                print("Turning on the light.")
            else:
                light.turn_off(entity_id=light_entity_id)
                print("Turning off the light.")
class Analyze:
    def connect_target_device(self):
            Record("tmp/tmp.wav",debug=False)
            val=is_Snap("tmp/tmp.wav")
            if(val>0.8): #Customize the sensitivity
                print(val)
                print("Snap detected!")
                toggle_light()
                print("Detecting snaps...")

if __name__ == '__main__':
    Load('pth/best_pth','cpu')
    print("Detecting snaps...")
    while True:
        Analyze().connect_target_device()
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            print('程序终止')
            sys.exit(0)
