import base64
import socket
from dnslib import DNSRecord, QTYPE, RR, TXT

def extract_http_payload(dns_request):
	request = DNSRecord.parse(dns_request)
	qname = str(request.q.qname)
	encoded_payload = qname.split(".example.com")[0]
	http_payload = base64.urlsafe_b64decode(encoded_payload.encode('utf-8'))
	return http_payload

def create_dns_response(request, response_data):
	response = request.reply()
	max_length = 255
	segments = [response_data[i:i+max_length] for i in range(0, len(response_data), max_length)]
	for segment in segments:
		response.add_answer(RR(request.q.qname, QTYPE.TXT, rdata=TXT(segment)))
	return response.pack()

def make_request(packet):
	host = packet.decode().split("Host: ")[1].split("\r")[0]
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, 80))
	s.send(packet)
	data = s.recv(4096)
	s.close()
	return data.decode()

def start_dns_server():
	server_address = ('0.0.0.0', 53)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(server_address)
	print("DNS server is running...")

	while True:
		data, address = sock.recvfrom(4096)
		print("Received request from:", address)
		try:
			http_payload = extract_http_payload(data)
			print("HTTP payload:", http_payload)
			response_data = make_request(http_payload)
			response = create_dns_response(DNSRecord.parse(data), response_data)
			sock.sendto(response, address)
		except Exception as e:
			print("Error processing request:", e)

start_dns_server()
