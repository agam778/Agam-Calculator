import sys
from cx_Freeze import setup, Executable
sys.argv.append("build")
filename = "Agam's Calculator.py"
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name = "Agam's Calculator",
    version = "1.0",
    description = "cx_Freeze Tkinter script",
    executables = [Executable(filename, base=base)])
