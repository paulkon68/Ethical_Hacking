from scapy.all import IP, ICMP, TCP, sr1, scapy
import sys


# We issue an ICMP packet to check whether the host is online.
def icmp_probe(ip):
	icmp_packet = IP(dst=ip)/ICMP()
	resp_packet = sr1(icmp_packet, timeout=10)
	return resp_packet != None


def syn_scan(ip, port):
	syn_packet = IP(dst=ip)/TCP(dport=int(port), flags='S')
	resp_packet = sr1(syn_packet, timeout=10)
	return resp_packet
		


if __name__ == '__main__':

	
	# set the system with ip address and the number of port to scan up to.
	ip, port = sys.argv[1:]
	service_list = []

	if icmp_probe(ip):
		for i in range(int(port)+1):
			syn_ack_packet = syn_scan(ip, i)
			if syn_ack_packet != None and syn_ack_packet.getlayer('TCP').flags == 0x12:
			# syn_ack_packet.show()
				service_list.append(i)

		if service_list != []:
			for i in service_list:
				print('Hehe Boi, service at port: ')
				print(f'  {i}')
			print(f'Hehe Boi, {len(service_list)} services are up!')
	else:
		print('ICMP Probe Failed')