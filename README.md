# Task Management System

### Run the following commands to get started:

```
git clone https://github.com/MaulikZalavadiya/mindinventory_task/tree/django_project Video_management
python3 -m venv venv
```
#### Activate the virtual environment

Mac OS / Windows
```source env/bin/activate```

Linux
```.\env\Scripts\activate```

```
cd Video_management
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

<a name="table-of-contents"></a>
## [Table of Contents](#table-of-contents)
  
* Task [CRUD Operations](#crud)
  * All Video ```http://127.0.0.1:8000/api/video_managemnt/```
  * Create Video ```http://127.0.0.1:8000/api/video_managemnt/```
  * Retrieve specific Video ```http://127.0.0.1:8000/api/video_managemnt/id/```
  * Update Video ```http://127.0.0.1:8000/api/video_managemnt/id/```
  * Delete Video ```http://127.0.0.1:8000/api/video_managemnt/id/```


* [Filter Tasks](#filter)
  * title ```http://127.0.0.1:8000/api/video_managemnt/?title=test2```

  
[Raseedi]: http://www.raseedi.co/


<a name="auth"></a>
<a name="all-tasks"></a>
<a name="crud"></a>
<a name="filter"></a>
<a name="export"></a>
