set /P working_directory=<working_directory_path.lock
cd %working_directory%
set /P haratyan_url=<url.lock
wget %haratyan_url% -O haratyan.html
nkf32 -w --overwrite haratyan.html
python main.py
%working_directory%Scheduler.bat