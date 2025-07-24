import subprocess
import os
import sys

print(sys.executable)
print(os.environ)

subprocess.run("sh autogen.sh", cwd="./ffms2")
