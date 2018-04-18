#!/usr/bin/env python

def log2dict(logfile):
	with open(logfile, "r") as file:
		file_content = file.read()

	lines = [ file_content.split('\n') ][0]
	formated_logs = []

	for tmp in lines:
		try:
			ip_date = tmp.split('"')[0]
			ipaddr = ip_date.split()[0]
			date = ip_date.split()[3][1:]

			method_path_ver = tmp.split('"')[1]
			method = method_path_ver.split()[0]
			path = method_path_ver.split()[1]
			ver = method_path_ver.split()[2]

			referer = tmp.split('"')[3]
			useragent = tmp.split('"')[5]

		except:
			continue

		formated_logs.append({
			'ipaddr'   : ipaddr,
			'date'     : date,
			'method'   : method,
			'path'     : path,
			'version'  : ver,
			'referer'  : referer,
			'useragent': useragent
		})

	return formated_logs


if __name__ == '__main__':

	dict_logs = log2dict(logfile="sports-access.log")

	# Get all ipaddrs
	ipaddrs = [ log['ipaddr'] for log in dict_logs ]

	# Get total
	# Python3) often_ipaddrs = { ip: ipaddrs.count(ip) for ip in set(ipaddrs) }
	often_ipaddrs = {}
	for ip in set(ipaddrs):
		often_ipaddrs[ip] = ipaddrs.count(ip)

	# Print ranking
	for k_ip, v_often in sorted(often_ipaddrs.items(), key=lambda x:x[1], reverse=True):
		print  v_often, k_ip
