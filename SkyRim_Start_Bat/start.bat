@echo off
setlocal enabledelayedexpansion

REM Set the source and destination directories
:: Set the source and destination directories
set "source_dir=I:\Games\Novuls\Instances\Nolvus Ascension\MODS\mods\MISC_Anime_Main_Menu_Replace_Collection\Pic"
REM set "dest_dir=I:\Games\Novuls\Instances\Nolvus Ascension\MODS\mods\MISC_Anime_Main_Menu_Replace_Collection\textures\interface\objects"
set "dest_dir=I:\Games\Novuls\Instances\Nolvus Ascension\MODS\mods\SOULWORKER MAINMENU\textures\interface\objects"

REM Set the new name for the copied file (without the path)
set "new_file_name=MAINMENUWALLPAPER.dds"

REM Check if the source directory exists
if not exist "%source_dir%" (
    echo Source directory does not exist: %source_dir%
    exit /b
)

REM Check if the destination directory exists
if not exist "%dest_dir%" (
    echo Destination directory does not exist: %dest_dir%
    exit /b
)

REM Delete all files in the destination directory before copying
echo Deleting files in %dest_dir%...
del /q "%dest_dir%\*"

REM Get a list of files in the source directory
set file_count=0
for %%f in ("%source_dir%\*") do (
    set /a file_count+=1
    set "file_!file_count!=%%f"
)

REM Check if there are any files in the source directory
if %file_count%==0 (
    echo No files found in the source directory.
    exit /b
)

REM Randomly select a file from the source directory
set /a random_index=%random%%%file_count+1
set "random_file=!file_%random_index%!"

REM Copy the randomly selected file to the destination directory and rename it
echo Copying file: !random_file!
copy /y "!random_file!" "%dest_dir%\%new_file_name%"

REM Wait for 5 seconds before launching the program to ensure copying is complete
timeout /t 5 /nobreak >nul

REM Launch the program (e.g., SKSE or any executable)
echo Starting the next program...
start "" "I:\Games\Novuls\Instances\Nolvus Ascension\STOCK GAME\skse64_loader.exe"

echo Done!
pause

