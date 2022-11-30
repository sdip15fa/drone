from djitellopy import Tello
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    
    tello = Tello(host=os.getenv("TELLO_IP") or "192.168.10.1")
    
    tello.connect(True)
   
    tello.emergency()
    
main()