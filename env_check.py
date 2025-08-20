#env_check.py
import sys
import pkgutil

print("Python path:", sys.executable)
print("Packages in this environment:", len(list(pkgutil.iter_modules())))