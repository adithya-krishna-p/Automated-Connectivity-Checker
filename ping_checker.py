import subprocess
import platform

def check_reachability(ip_list):
    print(f"--- Starting Connectivity Check ---")
    
    # Determine the flag for ping based on Operating System
    # -n is for Windows, -c is for Linux/Mac
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    for ip in ip_list:
        # Construct the command (e.g., "ping -n 1 8.8.8.8")
        command = ['ping', param, '1', ip]
        
        # Run the command and capture the result
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if response.returncode == 0:
            print(f"[SUCCESS] {ip} is reachable.")
        else:
            print(f"[FAILURE] {ip} is down or unreachable.")

# List of IPs to check - you can add your gateway or local devices here
targets = ["8.8.8.8", "1.1.1.1", "127.0.0.1", "192.168.1.254"]

if __name__ == "__main__":
    check_reachability(targets)