# Odiva: The File Capturer


## IT'S MADE FOR EDUCATION PURPOSE USE ONLY YOUR OWN MACHINES

## Description

Odiva is made for capturing file from a machine and sending via email it to another machine.


Odiva searchs specified file in OS even in root folders

## Usage

run update_emailer.py script from terminal (depending your python version)

```sh
$ python3 update_emailer.py
```

after that program will ask you the name of a file to search in OS

```sh
name: file.txt
```

after enter file's name program will be look like it's frozen but do not worry at the moment it searchs specified file in your all of your folders.

there is some comment lines in **update_path_emailer.py** module that will work to print path of the file in each extension


## Customization

There is limited file extensions in application. And you able to add more extensions to app.

line 10-14 is contains defined format types

```py
text_formats = ['.txt', '.html', '.docx', '.xlsx', '.xml']
image_formats = [
                '.jpg', '.png', '.jpeg', '.svg', '.tif', '.tiff', '.bmp', '.gif', '.eps', '.raw', '.cr2', '.net', '.orf', '.sr2', '.PSD', '.XCF', '.AI', '.CDR'
      ]
```

and you can add more extension or extension list to program

***NOTE: SCRIPT WRITTEN IN PYTHON 3, THIS VERSION ONLY WORKS IN LINUX BASED SYSTEMS***

# email_sender2019
