code.md
=======

code.md Page


Setup
---

1.   `git clone git@github.com:tim-md/code.md.git`
2.   `virtualenv codemd`
3.   `source codemd/bin/activate`
4.   `pip install -r requirements.txt`
5.   `cp codemd/sample_local_file.py codemd/local_file.py`
6.   fill the data in `local_file.py` file
7.   `chmod +x manage.py`
8.   Create database folder `mkdir db`
9.   run `./manage.py syncdb`
10.   run `./manage.py runserver`
12.  access [localhost:8000](localhost:8000)



