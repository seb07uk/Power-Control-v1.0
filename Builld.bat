:: Created by Sebastian Januchowski
:: polsoft.its@fastservice.com
:: https://github.com/seb07uk
@echo off
title Powerr Control Tools 1.0 Builder
pip install pyinstaller
echo.
echo [1;3;32mStep 1/3 done![0m
echo.
pyinstaller --onefile --windowed staart.py
echo.
echo [1;3;32mStep 2/3 done![0m
echo.
pyinstaller --onefile --windowed --icon=ikona.ico --version-file=version.txt start.py
echo.
echo [1;3;32mStep 3/3 done!
echo.
echo [1;3;32mAll done![0m
echo.
timeout /t 4 >nul