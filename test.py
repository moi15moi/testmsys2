import subprocess
import os

print(os.environ)

subprocess.run("sh autogen.sh", cwd="./ffms2")
