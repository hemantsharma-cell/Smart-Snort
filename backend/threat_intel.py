import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Normally, you would sign up on AbuseIPDB for a free API Key and put it here
# For now, we will use a blank key just to learn the structure!
ABUSE_KEY = os.getenv("ABUSEIPDB_API_KEY")
VT_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def get_abuseipdb_score(ip_address: str):
    print(f"🕵️‍♂️ Checking IP {ip_address} against AbuseIPDB...")
    
    # 1. This is the exact URL AbuseIPDB provides in their documentation
    url = "https://api.abuseipdb.com/api/v2/check"
    
    # 2. arguments to send to the server (the IP we want to check)
    querystring = {
        "ipAddress": ip_address,
        "maxAgeInDays": "90"
    }
    
    headers = {
        "Accept": "application/json",
        "Key": ABUSE_KEY
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status() 
        
        data = response.json()
        
        score = data['data']['abuseConfidenceScore']
        return score
        
    except Exception as e:
        print(f"Could not connect to Threat Intel: {e}")
        return 0.0

def get_virustotal_score(ip_address: str):
    print(f"🕵️‍♂️ Checking IP {ip_address} against VirusTotal...")
    
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip_address
    
    headers = {
        "x-apikey": VT_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        malicious_votes = data['data']['attributes']['last_analysis_stats']['malicious']
        return malicious_votes
    except Exception as e:
        print(f"VirusTotal Error: {e}")
        return 0

if __name__ == "__main__":
    
    score = get_abuseipdb_score("118.25.6.39")
    print(f"Threat Score: {score}/100")
