from djitellopy import Tello
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    
    tello = Tello(host=os.getenv("TELLO_IP") or "192.168.10.1")
    
    tello.connect(True)
    print("Tello connected")
    
    print("setting up wifi")
    
    ssid = f"tello-{tello.query_serial_number()}"
    password = os.getenv("TELLO_WIFI_PASSWORD")
    
    tello.set_wifi_credentials(ssid, password)
    
    print(f"ssid: {ssid}")
    print(f"password: {password}")
    