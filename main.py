import requests
import sys
import concurrent.futures


#print(sys.argv[2])
if len(sys.argv) != 2:
	print("Usage: wp_plugin_scan.py http://site.com")
	sys.exit()

plugins = []
found = []
url = sys.argv[1]
print(f"Testing: {url}")

with open('plugins.txt','r') as f:
	for line in f:
		plugins.append(line.strip())

def request_plugin(plugin_test):
	print(f"Trying: {plugin_test:<100} ",end="\r")
	r = requests.get(f"{url}/wp-content/plugins/{plugin_test}")
	if r.status_code	 != 404:
		found.append(plugin_test)
		print(f"\r{url}/wp-content/plugins/{plugin_test}")

with concurrent.futures.ThreadPoolExecutor(100) as executor:  # THIS TOOK ME HOURS.
	results = executor.map(request_plugin,plugins)

for line in found:
	print(f"Found: {url}/wp-content/plugins/{line}")
