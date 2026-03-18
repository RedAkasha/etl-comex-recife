import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Extract:
    def __init__(self):
        self.url = "https://api-comexstat.mdic.gov.br/cities"

    def extract_comex_recife(self, flow, ano):
        payload = {
            "flow": flow,
            "monthDetail": True,  
            "period": {
                "from": f"{ano}-01",
                "to": f"{ano}-12"
            },
            "filters": [
                {
                    "filter": "city", 
                    "values": [2611606] 
                }
            ],
            "details": ["city"], 
            "metrics": ["metricFOB", "metricKG"]
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url, json=payload, headers=headers, verify=False)
        
        if response.status_code == 400:
            print(f"DEBUG - Resposta do Servidor: {response.text}")
            
        response.raise_for_status()
        return response.json()