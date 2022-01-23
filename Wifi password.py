import subprocess


# Enter the network name
profile = input("Enter networks name: ")


try:
    password = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')

    password = [passwd.split(':')[1][1:-1]
                for passwd in password if "Key Content" in passwd]
except subprocess.CalledProcessError:
    print("Error: plz enter the a correct name.")


try:
    print("{:<30}|  {:<}".format(profile, password[0]))
except NameError:
    print("")

