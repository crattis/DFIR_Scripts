#!python3
"""case_folder.py
Creates folder for tracking individual cases on the user's desktop,
under a folder called 'Cases'. Concept from Don Murdoch's Blue Team
Handbook: Incident Response Edition.

Script only creates case_folder, case_notes.txt file, and
live_sample_folder.

Can be ran from icon on desktop or from command line. Opens local
terminal window for information from user.
"""

import os
import sys
import subprocess
from time import strftime

# import back space bug fix for Cygwin
if sys.platform == 'cygwin':
    import readline

def create_local():
    """Configure varables for working directory to store cases."""
    # TODO: Look in to setting this up to pull info from configuration
    _home_dir = os.path.expanduser('~')
    _location = 'Desktop'
    _case_dir = 'Cases'
    _combine = os.path.join(_home_dir, _location, _case_dir)
    return _combine


def test_case_num(_folder, _case_number):
    # TODO: create file and folder tests
    if _case_number in os.listdir(_folder):
        print(f'Case {_case_number} already exists in {_folder}. \n')
        dup_case = input('Do you want to create a second case? y/N: ')
        if dup_case.lower() == 'y':
            pass
        else:
            print(f'Please review {_folder} and run command again if needed.')
            sys.exit(1)
    return

def main():
    local_var = create_local()
    case_num = input('What is your ase number: ')
    test_case_num(local_var, case_num)


if __name__ == '__main__':
    main()