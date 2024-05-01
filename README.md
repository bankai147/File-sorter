# File-sorter
File Sorter
=====================

This program helps you automatically sort files in a specified directory by their type.

Installation
------------

1. Download the sort\_files.py file from this repository.
2. Make sure you have Python version 3.6 or higher installed.

Usage
-----

1. Open the sort\_files.py file in a text editor.
2. Change the value of the `main_path` variable to the path of the directory where you want to sort files. For example: `main_path = 'C:\\Users\\Username\\Downloads'`.
3. Save the changes and close the file.
4. Open the terminal or command prompt and navigate to the directory where the sort\_files.py file is located.
5. Run the program by entering the command `python sort_files.py`.
6. The program will automatically create new directories for each file type, move files from the specified directory to the corresponding directories, and delete empty directories.

Available File Types
--------------------

By default, the program supports the following file types:

* video: mp4, mov, avi, mkv, wmv, 3gp, 3g2, mpg, mpeg, m4v, h264, flv, rm, swf, vob
* data: sql, sqlite, sqlite3, csv, dat, db, log, mdb, sav, tar, xml
* audio: mp3, wav, ogg, flac, aif, mid, midi, mpa, wma, wpl, cda
* image: jpg, png, bmp, ai, psd, ico, jpeg, ps, svg, tif, tiff
* archive: zip, rar, 7z, z, gz, rpm, arj, pkg, deb
* text: pdf, txt, doc, docx, rtf, tex, wpd, odt
* 3d: stl, obj, fbx, dae, 3ds, iges, step
* presentation: pptx, ppt, pps, key, odp
* spreadsheet: xlsx, xls, xlsm, ods
* font: otf, ttf, fon, fnt
* gif: gif
* exe: exe
* bat: bat
* apk: apk
