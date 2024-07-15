import sys
import time

def app_header():
    input_str = '''===========================================\n\tMedia Search and Downloader\n==========================================='''
    sys.stdout.write('\n')
    for c in input_str:
        if c == '=':
            time.sleep(0.01)
        else:
            time.sleep(0.1)

        sys.stdout.write(c)
        sys.stdout.flush() 
    sys.stdout.write('\n')
