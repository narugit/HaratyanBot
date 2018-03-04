set today=%date%

rem 現在の時刻取得
for /f "delims=" %%i in ('time /t') do @set currenttime=%%i

set /P isNew=<log.txt

if %isNew% == New (
  call :set_new
) 
if %isNew% == Old (
  call :set_old
) 

rem タスクの削除
schtasks /delete /tn HaratyanCheck /F

rem タスクの生成
schtasks /create /tn HaratyanCheck /sd %nextdate% /st %nexttime% /sc once /tr  %working_directory%\HaratyanCheck.bat

rem 次回タスク日時のログ
echo; >> log.txt
echo %nextdate% %nexttime% >> log.txt

:set_new
set nexttime=17:00
powershell -command "(Get-Date).AddDays(1).ToString('yyyy/MM/dd')" > temp.txt
for /f %%i in (temp.txt) do SET nextdate=%%i
DEL temp.txt

:set_old
echo not new
for /f "delims=" %%i in ('time /t') do @set currenttime=%%i
if %currenttime:~3,1% == 0 (
  set /A nextminute=%currenttime:~4,1%+10
) else (
set /A nextminute=%currenttime:~3,2%+10
)
if %currenttime:~0,1% == 0 (
  set /A nexthour=%currenttime:~1,1%
) else (
set /A nexthour=%currenttime:~0,2%
)
if %nextminute% geq 60 (
  set /A nextminute=%nextminute%-60
  set /A nexthour=%nexthour%+1
)
set nexttime=%nexthour%:%nextminute%
set nextdate=%today%
