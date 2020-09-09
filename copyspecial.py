#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
import argparse
import subprocess
import shutil
import sys
import os
import re
__author__ = "Timothy La (tla111)"
"Received help from Mike B"


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here
    special_paths_list = []
    pattern_match = r'(\S*)__(\w+)__(\S*)'
    for file_name in os.listdir(dirname):
        if re.match(pattern_match, file_name):
            if file_name not in str(special_paths_list):
                special_paths_list.append(os.path.join(
                    os.path.abspath(dirname), file_name))
        else:
            continue
    return special_paths_list


def copy_to(path_list, dest_dir):
    """
    Given a path list & destination directory,
        copy all file into destination
    """
    os.makedirs(dest_dir)
    for path_name in path_list:
        shutil.copy(path_name, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """
    Creates a zip file containing all files from the list
    """
    hold_params = ["zip", "-j", dest_zip]
    for path in path_list:
        hold_params.append(path)
    print("Command I'm going to do: " + str(hold_params))
    subprocess.run(hold_params)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='from directory')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    if len(args) > 1:
        options = args[1]
        from_dir = args[2]
    else:
        from_dir = args[0]

    if ns.tozip:
        zip_to(get_special_paths(from_dir), options)
    if ns.todir:
        copy_to(get_special_paths(from_dir), options)
    else:
        special_paths_list = get_special_paths(from_dir)
        for path in special_paths_list:
            print(path)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
