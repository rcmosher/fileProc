# fileProc
Version 0.1

Run commands on a set of files.

## Notice
It should first be said this was made to solve a specific problem for myself so it may have shortcomings that keep it from working for you. The most important one is that it expects input files to be in a path taken from a date (yyyy/mm/dd) and output them to a modified path (yyyy/mm\_Month). This is currently hard coded. Otherwise, I've kept it as general as possible.

Second, this was also an attempt to get my feet wet in Python. So it has much room for improvement. But it does the job. Since I was looking for practice I didn't look too hard for existing solutions, and there is likely something out there that does this better.

# Overview

fileProc.py allows configuring commands to run for a set of files. It provides a set of variables that can be used to help specify input directories and output directories within those commands, as well as a few others. It also provides commands to run before and after processing all files.

It was originally made to transcode a set of video files, then upload those files to a photo sharing site. It is likely limited by that goal in some ways, but I've attempted to make it fairly general.

# Requirements

python3

# Use
`python3 fileProc.py`

Reads `fileProc.config` for settings. See the example included in this directory. It does nothing without modification, but includes much documentation. See also piwigoExample.config for a "working" example. It is essentially what I use this for with some directories, hostnames, and users changed for use as an example.

# Needed improvements
* Allow specifying the configuration file.
* Allow the file list to contain paths relative to input\_root\_dir.
* Allow multiple tasks to be listed without joining them together with &&. Let the program take care running them together.
* More generic way to translate an input path/name to an output one. Ideally custom methods could be written and pulled in through configuration and dependency injection.
* A way to translate input file names to output file names.

# Desired improvements:
* Other ways to read in a list of files. E.g. from a database or a command.
* TODOs throughout the files.
