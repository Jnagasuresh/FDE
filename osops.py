"""
`os` is how Python talks to the operating system: files and folders, paths (`os.path`), environment variables and processes. 
The same code runs on Windows, macOS and Linux.

"""
import os

print(os.getcwd()) # current working directory
os.chdir("..") # move up one folder
print(os.listdir(".")) # names in a floder (no full paths, no fixed order)

"""
os.mkdir("reports")
os.makedirs("out/logs/2026", exist_ok= True) # nested folders; no errors if they exist

with open("out/notes.txt","w") as f:
    f.write("hello")

os.rename("out/notes.txt","out/readme.txt") #rename or move
os.remove("out/readme.txt") # delete a FILE
os.rmdir("reports") # delete an empty folder
"""

# `os.path` essentials
print("----------os.path essentials start")
p = os.path.join("cypress", "e2e", "login.spec.ts")   # uses the right separator for the OS
print(p)                         # cypress\e2e\login.spec.ts

print(os.path.exists(p))                # True / False
print(os.path.isfile(p))                # is it a file?
print(os.path.isdir("cypress"))         # is it a folder?
print("basename: ",os.path.basename(p))              # login.spec.ts
print("dir name: ",os.path.dirname(p))               # cypress\e2e
print(os.path.splitext(p))              # ('cypress\e2e\login.spec', '.ts')
print("absolute path: ",os.path.abspath(p))               # C:\...\cypress\e2e\login.spec.ts
print(os.path.expanduser("~"))          # C:\Users\<you>
# os.path.getsize(p)               # size in bytes
print("----------os.path essentials end---------")

print("----------os.path Environment variables start..........")
# home = os.environ["USERPROFILE"]          # KeyError if missing
env = os.getenv("TEST_ENV", "qa")         # returns the default if missing (safer)
retries = int(os.getenv("RETRIES", "3"))  # values are ALWAYS strings, so convert them
os.environ["TEST_ENV"] = "staging"        # set it for this process and any child it starts
del os.environ["TEST_ENV"]                # unset it
print("----------os.path Environment variables end..........")