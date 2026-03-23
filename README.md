# LogParser
Creating a Log Parser to practice using python and enhance my hands-on security skills

<!-- Notes from Claude assessment, need to be modified -->
A Python CLI tool that parses SSH auth logs, identifies failed login 
attempts, groups them by IP address, and outputs a brute-force report as CSV.

## Features

- Parses standard auth.log / syslog format
- Groups failed SSH logins by IP address
- Sorts by attempt count descending
- Outputs timestamped CSV report
- Configurable threshold via CLI flag


## Usage

\```bash
python log_parser.py --file auth.log --threshold 5
\```

## What I Learned

- Python regex with named groups
- File I/O and CSV generation
- argparse for CLI interfaces
- How SSH brute-force attacks appear in logs

## Tech Stack

Python 3.10+ · Standard library only (re, csv, argparse, os)
