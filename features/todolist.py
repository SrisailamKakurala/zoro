import re
import datetime
import os
import platform
import subprocess

def add_reminder(to_do):
    try:
        with open('my1.txt', 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        content = []

    # Combine content into a single string to search for the date
    combined_content = ''.join(content)
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    
    # Match the pattern in the combined content
    matched = re.search(pattern, combined_content)
    today_str = str(datetime.date.today())
    
    if matched and matched.group() == today_str:
        with open('my1.txt', 'a+') as file:
            
            file.write('\nTask '+str(len(content))+': ' + to_do)
            return True

    else:
         
        with open('my1.txt', 'w') as file:
            
            file.write(today_str + '\nTask ' +'1: ' +to_do)
            



def show_todo():
    try:
        file_path = 'my1.txt'
        if platform.system() == 'Windows':
            os.startfile(file_path)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', file_path))
        else:  # Linux and other Unix-like systems
            subprocess.call(('xdg-open', file_path))
        return "File opened successfully."
    except Exception as e:
        return f"An error occurred: {e}"




def task_remover(task):
  with open('my1.txt','r') as file:
    cont = file.readlines()
  rem_tasks = [line for line in cont if task not in line]
  
  with open('my1.txt','w') as file:
    for i in rem_tasks:
      file.write(i)

#print(task_remover('Task 1'))
#print(add_reminder('learn Aws'))
#print(to_do())