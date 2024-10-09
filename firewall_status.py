import subprocess

def check_firewall_status_windows():
    try:
        # Running the 'netsh advfirewall show allprofiles' command to check firewall status
        firewall_status = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)

        # Check if there's an error in the command (e.g., netsh not available)
        if firewall_status.returncode != 0:
            print("[ERROR] Failed to check firewall status: {firewall_status.stderr.strip()}")
            return
        
        # Output the firewall status based on the profiles
        output = firewall_status.stdout.lower()
        
        if "state on" in output:
            print("[INFO] Firewall is enabled.")
        elif "state off" in output:
            print("[INFO] Firewall is disabled")
        else:
            print("[INFO] Firewall status unknown:\n{firewall_status.stdout.strip()}")
        
    except Exception as e:
        print("[ERROR] An error occurred: {e}")

# Run the firewall check
if __name__ == '__main__':
    check_firewall_status_windows()
