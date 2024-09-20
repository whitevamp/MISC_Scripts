@echo off
setlocal enabledelayedexpansion

:: Set the source and destination directories
set "source_dir=C:\path\to\source\folder"
set "dest_dir=C:\path\to\destination\folder"

:: Delete all files in the destination directory before copying
echo Deleting all files in %dest_dir%
del /Q "%dest_dir%\*.*"

:: Check if the deletion was successful
if %errorlevel% neq 0 (
    echo Failed to delete files in the destination directory.
    exit /b 1
)

:: Get a count of files in the source directory
set count=0
for %%f in ("%source_dir%\*.*") do (
    set /a count+=1
    set "file[!count!]=%%f"
)

:: Generate a random number between 1 and the number of files
set /a rand=(%random% %% count) + 1

:: Copy the randomly selected file to the destination directory, with overwrite
echo Copying file !file[%rand%]! to %dest_dir% (overwriting if exists)
copy /Y "!file[%rand%]!" "%dest_dir%"

:: Check if the copy was successful
if %errorlevel% neq 0 (
    echo File copy failed.
    exit /b 1
)

:: Start another program (replace with your program path)
echo Starting the next program...
start "" "C:\path\to\your\program.exe"

pause
