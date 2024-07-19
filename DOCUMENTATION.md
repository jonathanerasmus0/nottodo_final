# DOCUMENTATION

## Step 1: Clone the Repository
Open a terminal.
Navigate to the directory where you want to clone the repository.

```shell
cd path/to/your/directory
```

Clone the repository using git.

```shell
git clone https://github.com/jonathanerasmus0/nottodo_final.git
```

## Step 2: Create a Virtual Environment
Navigate to the project directory.

```shell
cd nottodo_final
```

Create a virtual environment. You can use venv, which is included with Python 3. You may need to specify the path to your Python executable.

```shell
python3 -m venv venv
```

## Step 3: Activate the Virtual Environment

```shell
# On Windows
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

## Step 4: Install the Requirements
Ensure you are in the project directory and the virtual environment is activated.
Install the dependencies listed in the requirements.txt file.

```shell
pip install -r requirements.txt
```

## Step 5: Verify the Installation
Check if the packages are installed correctly.

```shell
pip list
```

# To install Celery and Redis for your project, follow these steps:

### Step 1: Install Redis

Redis is an in-memory data structure store used as a database, cache, and message broker. You need to install it on your system.

#### On Windows:

1. **Download Redis** from [this link](https://github.com/microsoftarchive/redis/releases) (look for the latest `MSOpenTech` Redis release).
2. **Extract the zip file** and run `redis-server.exe`.

   Example:

   ```shell
   cd path\to\redis\folder
   redis-server.exe
   ```

#### On macOS:

1. **Use Homebrew** to install Redis.
   ```shell
   brew install redis
   ```
2. **Start Redis server.**
   ```shell
   brew services start redis
   ```

#### On Linux (Ubuntu):

1. **Install Redis using apt.**
   ```shell
   sudo apt update
   sudo apt install redis-server
   ```
2. **Start Redis server.**
   ```shell
   sudo systemctl start redis
   ```
3. **Verify Redis Installation**
	Once installed, you can check that Redis is running with:
	
	```shell
	redis-cli ping
	```
	
	If Redis is running, it will return a PONG response.

 
### Step 2: Install Celery

Celery is a distributed task queue that allows you to execute tasks asynchronously. To install Celery, follow these steps:

1. **Activate your virtual environment** (if it's not already activated).
   ```shell
   # On Windows
   venv\Scripts\activate

   # On macOS and Linux
   source venv/bin/activate
   ```

2. **Install Celery using pip.**
   ```shell
   pip install celery
   ```

3. **Monitor Celery Tasks.**
	Run the Celery worker and beat scheduler to monitor tasks:

   ```shell
   celery -A nottodo_final worker --loglevel=info
   ```
   
   ```shell
   celery -A nottodo_project beat --loglevel=info
   ```


# Deploy Django App to Heroku
 
This is a part of YouTube Tutorial video on How to Deploy a Django Application to Heroku.
https://youtu.be/V2rWvStauak

## Usage

* If you don't have git installed, follow this [Tutorial](https://www.atlassian.com/git/tutorials/install-git) and come back here.

* Make a copy of your project or use a seperate git branch.

* Make sure your virtual environment is activated.

* Add your dependencies to requirements.txt by typing in the terminal,
```shell
pip freeze > requirements.txt
```

* Add this in settings.py
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

* [Make a Heroku account](https://signup.heroku.com/)

* [Download Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

* [Configure Django Heroku](https://devcenter.heroku.com/articles/django-app-configuration)

* In your terminal, type in
 ```shell
git init
git add .
git commit -m "first commit"

heroku login
heroku create app_name
git push heroku main
heroku open

heroku run python manage.py migrate
```
** PS: if Heroku isn't recognized as a command, please close your terminal and editor and then re-open it.

* DEBUG = False in settings.py

* ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost', '127.0.0.1'] in settings.py

* If you make edits, then just type in the terminal,
```shell
git add .
git commit -m "edit"
git push heroku main
```

