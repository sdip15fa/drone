import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from drone.main import main

main()
