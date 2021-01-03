#!/usr/bin/env python3
# coding=utf-8

import FlatFileRepo
import configparser
import re
from pathlib import Path
import os

# TODO make this a config option
debug=0

def main():
    # TODO Should make a class that that main uses.
    # TODO allow running pre, post, or file processing independently
    # TODO allow passing config file as an argument
    config = LoadConfig('testing.config')
    input_root_dir = config['Main']['input_root_dir']
    output_root_dir = config['Main']['output_root_dir']
    file_list = config['Main']['file_list']

    file_list = input_root_dir + config['Main']['file_list']

    file_repo = FlatFileRepo.FlatFileRepo(file_list)

    PreProcess(config)

    for file in file_repo.files():
        print(file)
        
        ProcessOneFile(file, input_root_dir, output_root_dir, config)

    PostProcess(config)

"""
Takes a single file to run through the commands specified in
configuration.
"""
def ProcessOneFile(file, input_root_dir, output_root_dir, config):
    # Consider having file list strip the input root dir
    # Or prepend it so it isn't needed in the file list
    input_full_path = Path(file).expanduser()
    if not input_full_path.exists():
        raise Exception("Unable to find the file " + str(input_full_path))

    if ('Tasks' not in config): return
    if ('per_file_task' not in config['Tasks']): return
    command = config['Tasks']['per_file_task']
    if (command == ""): return


    input_root_dir = Path(input_root_dir).expanduser()
    output_root_dir = Path(output_root_dir).expanduser()

    input_dir = input_full_path.parent
    input_file = input_full_path.name
    input_rel_dir = input_dir.relative_to(input_root_dir)
    _in_path_parts = input_rel_dir.parts
    input_base_file = input_full_path.stem

    # convert month piece and drop the day
    # TODO allow general output path manipulation.
    _out_path_parts = _in_path_parts[0:-2] + (MonthMap(_in_path_parts[-2]),)
    output_rel_dir = Path(*_out_path_parts)

    # TODO add means of generating output file name
    output_file = input_file
    output_base_file = input_base_file

    output_full_path = Path(output_root_dir, output_rel_dir, output_file)
    output_dir = output_full_path.parent

    # add trailing slashes
    input_root_dir=TermPath(input_root_dir)
    input_dir=TermPath(input_dir)
    output_root_dir=TermPath(output_root_dir)
    output_rel_dir=TermPath(output_rel_dir)
    output_dir=TermPath(output_dir)

    task_string = command.format(input_root_dir=input_root_dir,input_file=input_file,input_dir=input_dir,input_rel_dir=input_rel_dir,output_root_dir=output_root_dir,output_rel_dir=output_rel_dir,output_file=output_file,output_dir=output_dir,output_base_file=output_base_file,input_full_path=input_full_path,output_full_path=output_full_path)
    print(task_string) if debug else os.system(task_string)

"""
Read the PreTasks configuration and process them.
"""
def PreProcess(config):
    if ('PreTasks' not in config): return
    if ('command' not in config['PreTasks']): return
    command = config['PreTasks']['command']
    if (command == ""): return

    FilelessProcess(command, config)

"""
Read the PostTasks configuration and process them.
"""
def PostProcess(config):
    if ('PostTasks' not in config): return
    if ('command' not in config['PostTasks']): return
    command = config['PostTasks']['command']
    if (command == ""): return

    FilelessProcess(command, config)

"""
Take a command not specific to a file and process it.
"""
def FilelessProcess(command, config):
    input_root_dir = config['Main']['input_root_dir']
    output_root_dir = config['Main']['output_root_dir']
    input_root_dir = Path(input_root_dir).expanduser()
    output_root_dir = Path(output_root_dir).expanduser()

    task_string = command.format(input_root_dir=input_root_dir,output_root_dir=output_root_dir)
    print(task_string) if debug else os.system(task_string)


"""
Load configuration from a file name.
"""
def LoadConfig(configFile):
    config = configparser.ConfigParser()
    config.read(configFile)
    return config

"""
Put a trailing separator on a path string.
"""
def TermPath(path):
    return str(path) + os.sep

# I don't like this as it is strongly binding this to my gallery.
"""
Converts a month in form 'mm' to 'mm_Month'.
"""
def MonthMap(month_as_num):
    return {
        '01': '01_January',
        '02': '02_February',
        '03': '03_March',
        '04': '04_April',
        '05': '05_May',
        '06': '06_June',
        '07': '07_July',
        '08': '08_August',
        '09': '09_September',
        '10': '10_October',
        '11': '11_November',
        '12': '12_December',
    }[month_as_num]

if __name__ == '__main__':
    main()
