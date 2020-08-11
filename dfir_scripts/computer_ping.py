#! python3
"""computer_ping.py a simple ping to see if a box is up or not.
Why this script: This script was created to track if an employee's
computer was online or not. The script allowed monitoring employees
across timezones, when their computer had generated alerts.

This runs ping on the target computer for one hour, printing the
results to terminal, and either creating an alert when the employee's
computer has connected to the network, or the hour is up.
"""

import argparse
import ipaddress
import os
import sys
import subprocess
import time


def get_args():
    parser = argparse.ArgumentParser(description="Ping a computer's \
        hostname once every ten minutes to see if it is online. \n")
    parser.add_argument('hostname')
    _args = parser.parse_args()
    return _args


def get_env():
    """Gets the operating system platform for some platform specific
    options in other sections of the program
    """
    if sys.platform == 'win32':
        _env = 'win32'
    elif sys.platform == 'darwin':
        _env = 'darwin'
    elif sys.platform == 'cygwin':
        _env = 'cygwin'
    else:
        _env = 'linux'
    return(_env)


def ping_computer(_host, _sys):
    """Run platform specific ping command, different between windows
    and other other systems.

    For ping timeout: Windows/DOS uses -w for time out in Milliseconds.
    OSX and Cygwin use -W Milliseconds, Linux uses -W seconds
    """
    if _sys == 'win32':
        _resp = os.system('ping -4 -n 1 -w 1000 ' + _host + ' > nul 2>&1')
    elif _sys == 'cygwin':
        _resp = os.system('ping -4 -n 1 -w 1000 ' + _host + ' > nul 2>&1')
    elif _sys == 'linux':
        _resp = os.system('ping -c 1 -W 1 ' + _host + ' > /dev/null 2>&1')
    else:
        _resp = os.system('ping -c 1 -W 1000 ' + _host + ' > /dev/null 2>&1')
    return _resp


def alert_box(_result, _plat, _host):
    _fileout = _host + '_ping_result.txt'
    with open(_fileout, 'w') as f:
        f.write(_result)
    if _plat == 'win32':
        os.startfile(_fileout)
    elif _plat == 'darwin':
        subprocess.run(['open', _fileout], stderr=subprocess.DEVNULL)
    elif _plat == 'cygwin':
        subprocess.run(['cygstart', _fileout], stderr=subprocess.DEVNULL)
    elif _plat == 'linux':
        subprocess.run(['xdg-open', _fileout], stderr=subprocess.DEVNULL)
    else:
        pass
    time.sleep(5)
    os.remove(_fileout)
    return


def main():
    opts = get_args()
    try:
        ipaddress.ip_address(opts.hostname)
        print("\n Sorry you  must use a hostname not an IP address. \n")
        sys.exit(1)
    except ValueError:
        pass
    env = get_env()
    for i in range(1, 7):
        up_or_down = ping_computer(opts.hostname, env)
        if up_or_down == 0:
            print(f'Attempt {i}: {opts.hostname} is up!')
            alert_box(f'{opts.hostname} is up at this time!', env,
                      opts.hostname)
            break
        else:
            if i != 6:
                print(f'Attempt {i}: {opts.hostname} is down, trying again in '
                      '10 minutes.')
                time.sleep(6)
            else:
                print(f'Attempt {i}: {opts.hostname} is down! '
                      'Pings Ended after 1 hour of trying.')
                alert_box(f'{opts.hostname} is down at this time! '
                          'Tried for 1 hour.', env, opts.hostname)


if __name__ == '__main__':
    main()
