from threading import threading
import os
import sys
import subprocess


def _main_function_():
    command  = subprocess.subprocess(["ls"], capture_output=True, shell=True).stdout
    
if __main__ == '__main__':
    _main_function_()