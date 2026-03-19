#Log Parser Created (3/19)
#Commit 0 - Jordan Gethers - Initial Plan/Commit    

#TODO: Use the re module to extract failed SSH login lines
#TODO: Learn regex: re.search(), re.findall(), named groups

# Later TODO: Group failures by IP using a dict. COunt and sort Descending.
#             Output to CSV with a timestamp column using the csv module

#Imports
import csv, re, os
from datetime import datetime

#print(os.getcwd())
script_dir = os.path.dirname(__file__)
#print(script_dir)
#print(ip)
#print(f"-> {line}")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:S")
#timestamp is for time log_parser is run, not when IP failed authentication

file_path = os.path.join(script_dir, "logFiles/sample_auth.log")
with open(file_path, 'r') as f: #Add encoding?
    log_txt = f.readlines()     #print(log_txt)
    
    ip_counts = {}
    for line in log_txt:
        match = re.search(r"Failed password", line)
        if match: #TODO: add other user login ssh failure types
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line) #TODO:ProTip- consider a null check
            ip = ip_match.group(1)

            if ip not in ip_counts:
                ip_counts[ip] = 0
            ip_counts[ip] += 1

    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_ips)

with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)  
    writer.writerow(["ip", "fail_count", "timestamp"]) #header row

    for ip, count in sorted_ips:
        writer.writerow([ip, count, timestamp])