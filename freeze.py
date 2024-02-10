import subprocess

def print_pip_freeze():
    try:
        # Run the pip freeze command and capture its output
        pip_freeze_output = subprocess.check_output(['pip', 'freeze']).decode('utf-8')
        
        # Print the output
        print("List of installed packages:")
        print(pip_freeze_output)
    except subprocess.CalledProcessError:
        print("Error: Failed to execute 'pip freeze' command.")

# Call the function to print the list of installed packages
# print_pip_freeze()
