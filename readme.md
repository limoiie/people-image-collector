## Readme


### Function implemented

- Monitoring through camera 1 frame every second (able to configure)
- Extract faces from the caught frame
- Identify face and classify it as a man
  - a man: created with a random name has a create_time and a list of face record
  - a face record: created with a record_time and has a image path (able to configure) pointing to the face image 
- Store info of mans created and images of the faces
- Load previous info of mans
- Some test case for unit code  

### How to run

First, you need install all the python libs listed in 'requirements' file

Next, change the var 'project_root_directory' in file 'app/collector/app.py' to your real project root dirctory;

Then, you can run in two ways:

#### 1. Run with pycharm

click the green triangle button in PyCharm IDE alongside the main function in file 'app/collector/app.py'


#### 2. Run in a shell

open a shell and type:

```bash
cd people-image-collector
python apps\collector\app.py
```
