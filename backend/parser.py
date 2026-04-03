import re

def parse_snort_alert(line: str):
    parsed_data = {
        "rule_id": 0,
        "rule_name": "",
        "priority": 0,
        "protocol": "",
        "source_ip": "",
        "source_port": 0,
        "destination_ip": "",
        "destination_port": 0,
        "raw_text": line.strip()
    }

    protocol_match = re.search(r'\{(.*?)\}',line)
    if protocol_match:
        parsed_data["protocol"] = str(protocol_match.group(1))
    rule_id_priority_match = re.search(r'\[(\d+):(\d+):(\d+)\]',line)
    if rule_id_priority_match:
        parsed_data["rule_id"] = int(rule_id_priority_match.group(2))
        parsed_data["priority"] = int(rule_id_priority_match.group(3))
    ip_port_match = re.search(r'(\d+\.\d+\.\d+\.\d+):(\d+)\s+->\s+(\d+\.\d+\.\d+\.\d+):(\d+)' , line)
    if ip_port_match:
        parsed_data["source_ip"] = ip_port_match.group(1)
        parsed_data["source_port"] = int(ip_port_match.group(2))
        parsed_data["destination_ip"] = ip_port_match.group(3)
        parsed_data["destination_port"] = int(ip_port_match.group(4))
    rule_name_match = re.search(r'\[\*\*\]\s\[\d+\:\d+\:\d+\]\s+(.*?)\s+\[' , line)
    if rule_name_match:
        parsed_data["rule_name"] = rule_name_match.group(1)
    return parsed_data

if __name__ == "__main__":
    test_line = "09/30-20:01:15.123456 [**] [1:2010935:5] ET SCAN Nmap Scripting Engine User-Agent Detected [**] {TCP} 192.168.1.25:34567 -> 192.168.1.10:80"
    result = parse_snort_alert(test_line)
    for key,value in result.items():
        print(f"{key}: {value}")
