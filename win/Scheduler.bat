set today=%date%

rem 現在の時刻取得
for /f "delims=" %%i in ('time /t') do @set currenttime=%%i

set /P isNew=<log.txt

if %isNew% == New (
  call :set_new
) else (
  call :set_old
) 

rem タスクの削除
schtasks /delete /tn HaratyanCheck /F

rem タスクの生成
schtasks /create /tn HaratyanCheck /sd %nextdate% /st %nexttime% /sc once /tr %working_directory%win/HaratyanCheck.bat

rem 次回タスク日時のログ
echo; >> log.txt
echo %nextdate% %nexttime% >> log.txt
pause
exit /b

:set_new
set nexttime=17:00
powershell -command "(Get-Date).AddDays(1).ToString('yyyy/MM/dd')" > temp.txt
for /f %%i in (temp.txt) do SET nextdate=%%i
DEL temp.txt
exit /b

:set_old
for /f "delims=" %%i in ('time /t') do @set currenttime=%%i
call :delete_zero_add_ten_minute
call :delete_zero_hour
if %nextminute% geq 60 (
  set /A nextminute=%nextminute%-60
  set /A nexthour=%nexthour%+1
)
call :shape_zero_minute
call :shape_zero_hour
set nexttime=%nexthour%:%nextminute%
set nextdate=%today%
exit /b

:delete_zero_add_ten_minute
if %currenttime:~3,1% == 0 (
  set /A nextminute=%currenttime:~4,1%+10
) else (
set /A nextminute=%currenttime:~3,2%+10
)
exit /b

:delete_zero_hour
if %currenttime:~0,1% == 0 (
  set /A nexthour=%currenttime:~1,1%
) else (
set /A nexthour=%currenttime:~0,2%
)
exit /b

:shape_zero_minute
if %nextminute% lss 10 (
  set nextminute=0%nextminute%
)
exit /b

:shape_zero_hour
if %nexthour% lss 10 (
  set nexthour=0%nexthour%
)
exit /b