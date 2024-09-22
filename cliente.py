import base64, socket, sys
from dnslib import DNSRecord, DNSQuestion, QTYPE

def create_http_payload(host):
	http_payload = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
	encoded_payload = base64.urlsafe_b64encode(http_payload.encode('utf-8')).decode('utf-8')
	return encoded_payload

def split_payload(payload, max_length):
	return [payload[i:i+max_length] for i in range(0, len(payload), max_length)]

def create_dns_request(payload_segment):
	qname = payload_segment + ".example.com"
	question = DNSQuestion(qname, QTYPE.TXT)
	request = DNSRecord()
	request.add_question(question)
	return request.pack()

def send_dns_request(dns_request):
	server_address = (dnshost, 53)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		sock.sendto(dns_request, server_address)
		data, _ = sock.recvfrom(4096)
		return data
	finally:
		sock.close()

def extract_http_response(dns_response):
	response = DNSRecord.parse(dns_response)
	http_response = ""
	for rr in response.rr:
		if rr.rtype == QTYPE.TXT:
			http_response += str(rr.rdata).strip('"')

	formatted_response = http_response.replace('\\012', '\n').replace('\\015', '\r')
	return formatted_response

dnshost = sys.argv[1]
host = sys.argv[2]
http_payload = create_http_payload(host)
payload_segments = split_payload(http_payload, 63)  # Dividir em segmentos de até 63 caracteres
for segment in payload_segments:
	dns_request = create_dns_request(segment)
	dns_response = send_dns_request(dns_request)
	http_response = extract_http_response(dns_response)
	print(http_response)

