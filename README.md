# DFIR_Scripts
Scripts (shell, python, etc), I wrote for use in different DFIR related activities. These are things I wrote to improve my scripting skills and used for scratching repetitive itches.

## Computer Ping (Python).
  This script is designed to ping a host name or ip address for up to 60 minutes, once every 10 minutes. It stops when it can either ping the box, or when the hour is up. The script will load a text file when the script completes.

  This was rewritten to work on Windows10, Cygwin on Windows10, OSX and Linux.

  New version is under dfir_scripts>dfir_scripts>computer_ping.py - Still in testing for OSX. Other three have been shown to work.
 
  Have not tried on Windows Subsystem Linux yet, need to check that. Previous attempts to use ping under WSL failed.

  Original scripts under computer_ping folder are considered deprecated and will be removed when all updates are finished.

## Base64 and Hex decoders (Python and compiled exe for Windows).
  Similar to the 2 shell scripts below, but written in python and use a file instead of a command line argument (by request).
  
  These will convert base64 or hexadecimal in the associated text file (base64.txt or hex.txt) and make it human readable. The script and input files need to stay in the same folder, output file will also be in that folder. Note on the Hex, make sure there is no line breaks or spaces. All hex strings have to be one line for the script to work.
  
  Python scripts, run like all python scripts and require python 3.6 or higher to be installed.
  
  Exe versions are fully self-contained Windows executables. Change input file’s data to what needs to be decoded, save, and double click exe. Then check the generated output file.

## URI Extractor (Python).
  This script is designed to take a file containing URI links that need to have the host information extracted. It was originally designed to take the output of a web based tool (copied and pasted to a text file) and only show one host for all instances in the text file. It works on fanged and de-fanged URI, and catches HTTP, HTTPS, FTP, FTPS, LDAP, SFTP, etc.

Current versions of the scriptis modular. Still need to set up setup.py to import. 
 * uri_extrator.py - written for Python 3, needs to be called by python.
 * ~~lHttpExtractor.py~~ - REMOVED
 * ~~cyHttpExtractor.py~~ - REMOVED
 
## Other
  Scripts that are still being worked on, not quite ready - test at your own risk.
   * import_proxy_info.py - for those times when you're behind a proxy and have the proxy information to fill in. Usage: Put in to same directory you're working in.  from import_proxy_info.py import myProxy. Then when requests or other need proxy, proxy=myProxy
   * case_folder.py - Creates folder for the case on the user's desktop to track cases. If the user wants to store it somewhere other than the desktop, change the location variable under local_variables.
Requires that the folder Cases already exists at location.

## Shellscripts (Shell / Bourne-Again SHell)
* killSpam.sh - Works with files in SpamAssassin's quarantine folder. Shows the To, From, Date, and Subject lines, and then asks to release email to recipient or delete the email.
* b64Decode.sh - cli script to convert user supplied base64 text to ASCII
* hexDecode.bsh - cli script to convert user supplied hexadecimal to ASCII
* uHits.sh -  A quick script to take a file name from the user to sort, remove duplicates with count, and sort result. Looking for Unique Hits (uHits)
