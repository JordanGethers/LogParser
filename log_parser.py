#Log Parser Created (3/19)
#Commit 0 - Jordan Gethers - Initial Plan/Commit    

#TODO: Use the re module to extract failed SSH login lines
#TODO: Learn regex: re.search(), re.findall(), named groups

# Later TODO: Group failures by IP using a dict. COunt and sort Descending.
#             Output to CSV with a timestamp column using the csv module

#Imports
import re, os

#print(os.getcwd())
script_dir = os.path.dirname(__file__)
#print(script_dir)
#print(ip)
#print(f"-> {line}")

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
            
