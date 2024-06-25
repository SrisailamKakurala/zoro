import time
import pyautogui

def write(code):
    
    # Split the response into lines
    lines = code.strip().split('\n')

    # Remove the first and last lines
    if len(lines) > 1:
        filtered_lines = lines[1:-1]
    else:
        filtered_lines = []

    # Join the remaining lines into a single string
    filtered_output = '\n'.join(filtered_lines)

    # Write the filtered output to a file
    with open('code.txt', 'w') as f:
        f.write(filtered_output)

    time.sleep(1)
    # Read the content from the file
    with open('code.txt', 'r') as file:
        cont = file.read()
        
        print("===== file content ========")
        print(cont)

        # Type out the content using pyautogui
        for char in cont:
            pyautogui.write(char)
            time.sleep(0.02)  # Adjust the sleep time as needed

