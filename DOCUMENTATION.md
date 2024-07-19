# DOCUMENTATION

Step 1: Clone the Repository
Open a terminal.
Navigate to the directory where you want to clone the repository.
bash
Copy code
cd path/to/your/directory
Clone the repository using git.
bash
Copy code
git clone https://github.com/jonathanerasmus0/nottodo_final.git
Step 2: Create a Virtual Environment
Navigate to the project directory.
bash
Copy code
cd nottodo_final
Create a virtual environment. You can use venv, which is included with Python 3. You may need to specify the path to your Python executable.
bash
Copy code
python3 -m venv venv
Step 3: Activate the Virtual Environment
On Windows:
cmd
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Step 4: Install the Requirements
Ensure you are in the project directory and the virtual environment is activated.
Install the dependencies listed in the requirements.txt file.
bash
Copy code
pip install -r requirements.txt
Step 5: Verify the Installation
Check if the packages are installed correctly.
bash
Copy code
pip list
Complete Steps:
Here’s a complete script you can run in the terminal for the whole process (assuming you have Python and git installed):

bash
Copy code
# Navigate to your desired directory
cd path/to/your/directory

# Clone the repository
git clone https://github.com/jonathanerasmus0/nottodo_final.git

# Navigate to the project directory
cd nottodo_final

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
# venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt
After completing these steps, you should have the project set up and ready to use on your local machine.




## install requirements file

## CELERY INSTRUCTIONS

## Installing Redis

## HEROKU deployment
