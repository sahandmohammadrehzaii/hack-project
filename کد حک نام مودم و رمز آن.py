import subprocess
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors='backslashreplace')
data = data.split('\n')
profiles = []
for i in data:
    if "All User Profile" in i:
        i = i.split(":")[1].strip()
        profiles.append(i)
print("{:<30}| {}".format("Wi-Fi Modem Name", 'Password'))
print("-"*46)
print('Hello SahandMohammadRezaiee')
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key', '=', 'clear'])
    results = results.decode('utf-8', errors='backslashreplace')
    results = results.split('\n')
    wifis = [item.split(":")[1].strip() for item in results if "Key Content" in item]
    try:
        print("{:<30}| {}".format(profile, wifis[0]))
    except:
        print("{:<30}| {}".format(profile, ""))

for i in range(1):
    print("Hello sahand mohammad rezaiee")
