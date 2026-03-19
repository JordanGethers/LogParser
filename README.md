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

## Installation

\```bash
git clone https://github.com/yourusername/log-parser.git
cd log-parser
pip install -r requirements.txt
\```

## Usage

\```bash
python log_parser.py --file auth.log --threshold 5
\```

## Example Output

\```
IP Address       Failed Attempts
192.168.1.105    47
10.0.0.23        31
172.16.0.8       12
\```

## What I Learned

- Python regex with named groups
- File I/O and CSV generation
- argparse for CLI interfaces
- How SSH brute-force attacks appear in logs

## Tech Stack

Python 3.10+ · Standard library only (re, csv, argparse, os)
