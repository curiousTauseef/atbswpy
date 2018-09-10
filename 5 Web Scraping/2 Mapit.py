import webbrowser
import sys
import pyperclip

# implementing with command line arguments
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/'+address)

else:
    # implementing with pyperclip clipboard method
    address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/'+address)
