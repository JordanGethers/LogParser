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

file_path = os.path.join(script_dir, "logFiles/sample_auth.log")
with open(file_path, 'r') as f: #Add encoding?
    log_txt = f.read()
    print(log_txt)
