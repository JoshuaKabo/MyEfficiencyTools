import ctypes, sys, os

# returns True if the user has admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# if not already admin (checked first), acquire admin privileges
# NOTE: if this method doesn't work, consider just re-running with "powershell -command "Start-Process cmd -ArgumentList '/c cd /d %CD% && COMMAND' -Verb runas"""
def acquire_admin_privileges():
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)