# Database Application for StoryTrack Pro
StoryTrack Pro is a system designed to help newsrooms efficiently track news stories from assignment to publication. It enables editors to manage reporter workloads, monitor story progress, and meet deadlines, while reporters can update their status and submit work seamlessly. Additionally, it will provide an interface for reporters to update their story status, request editorial reviews, and submit stories for publication.

The system will operate in a newsroom environment where multiple reporters work simultaneously on various stories across different media formats. The editor will assign stories based on priority and importance. Reporters will be able to update their story status, such as "researching," "interviewing," "writing," or "awaiting review." Editors can monitor the progress in real time and provide feedback or request changes as needed. The system will also store information about each story, including the date of assignment, expected publication date, the news category, and the media platform it is intended for. The environment reflects a newsroom handling breaking news, feature stories, and investigative reports simultaneously.

## Contributors
Sarah Culpepper C00302257 \
Scott Whitman C00453332

## Create Python Virtual Environment

```bash
virtualenv -p /usr/local/bin/python3.13 .venv   # for UNIX and MacOS bash/zsh
```

```bash
python -m virtualenv .venv                  # for Windows git bash and Windows CMD
```

## Activate Python Virtual Environment

```bash
source .venv/bin/activate                   # for UNIX and MacOS bash/zsh
```

```bash
source .venv/Scripts/activate               # for Windows git bash
```

```cmd
.venv\Scripts\activate.bat                  # for Windows CMD
```

For the following steps and for development, keep the virtual environment activated all the time.

## Install Python Requirements

```bash
pip3.13 install -r requirements.txt            # UNIX
```

```bash
pip install -r requirements.txt
```

## Start Local mysql Database

```bash
sudo service mysql start           # to start local mysql database
```

```bash
sudo service mysql stop            # to stop local mysql database
```

```bash
brew services start mysql          # UNIX start local mysql database
```

```bash
brew services stop mysql           # UNIX start local mysql database
```
## Configure Local Database

```bash
mysql -u root -p                   # login to database
```

```bash
CREATE DATABASE storytrack_pro;    # Create database
```

```bash
CREATE USER 'your_username'@'localhost' 
IDENTIFIED BY 'your_password';     # create local user
```

```bash
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
FLUSH PRIVILEGES;
```
## Run the Django Web Server

```bash
python3 manage.py runserver        # UNIX start web server 
```

```bash
python manage.py runserver         # start web server 
```

## Create Super User

```bash
python3 manage.py createsuperuser  # UNIX start web server 
```

```bash
python manage.py createsuperuser   # create super user
```