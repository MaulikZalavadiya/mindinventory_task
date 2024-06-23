# Video management

### Run the following commands to get started:
```
git clonehttps://github.com/MaulikZalavadiya/mindinventory_task.git video_management
python3 -m venv venv
```

#### Activate the virtual environment

Mac OS / Windows
```source env/bin/activate```

Linux
```.\env\Scripts\activate```

```
cd flask_recipe
pip install -r requirements.txt
```


# Overview

This project is a Video management.
It was built using flask and contains the following:

* Allows new accounts upload video.

# Celery Setup
mack sure redis is install before run celery command.

```celery -A project.tasks worker --loglevel=info```


* [video upload](#CRUD)
  * POST video ```http://127.0.0.1:8000/upload```
  * GET video ```http://127.0.0.1:8000/search```


