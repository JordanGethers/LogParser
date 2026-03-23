#Log Parser Created (3/19)
#Commit 0 - Jordan Gethers - Initial Plan/Commit    

#TODO:  improve regex, likely need to look at oher examples (want production value/level)

#Imports
import argparse, csv, re, os
from datetime import datetime

# Set up argparse — reads flags the user types at the command line
parser = argparse.ArgumentParser(description="SSH Failed Login Parser")
parser.add_argument("--file", default="logFiles/sample_auth.log",
                    help="Path to the auth log file")
parser.add_argument("--threshold", type=int, default=1,
                    help="Only show IPs with this many failures or more")
args = parser.parse_args()

script_dir = os.path.dirname(__file__)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#timestamp is for time log_parser is run, not when IP failed authentication

# re.compile() builds the pattern object once here, outside the loop.
# re.search() inside a loop would re-parse the pattern string on every iteration —
# wasteful on large log files with thousands of lines.
# Using a compiled pattern also keeps pattern definitions in one place,
# separate from the logic that uses them, which is standard practice.
#
# Old approach (avoid in loops):
# match = re.search(r"failed password|authentication failure|invalid user", line, re.IGNORECASE)
FAILURE_PATTERN = re.compile(r"failed password|authentication failure|invalid user", re.IGNORECASE)

file_path = os.path.join(script_dir, args.file)
with open(file_path, 'r') as f: #Add encoding?
    log_txt = f.readlines()

    ip_counts = {}
    for line in log_txt:
        match = FAILURE_PATTERN.search(line)
        if match:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)| rhost=(\d+\.\d+\.\d+\.\d+)", line) 
            if ip_match:
                ip = ip_match.group(1) or ip_match.group(2)

                if ip not in ip_counts:
                    ip_counts[ip] = 0
                ip_counts[ip] += 1

    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)  
    writer.writerow(["ip", "fail_count", "timestamp"]) #header row

    for ip, count in sorted_ips:
        if count >= args.threshold:   # skip IPs below the threshold
            writer.writerow([ip, count, timestamp])

