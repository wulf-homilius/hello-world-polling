import requests
import json

def fetch_patient_data():
    url = "https://hapi.fhir.org/baseR4/Patient?_count=1"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("entry") and len(data["entry"]) > 0:
            patient = data["entry"][0]["resource"]
            name = patient.get("name", [{}])[0].get("given", ["Unknown"])[0]
            family_name = patient.get("name", [{}])[0].get("family", "")
            full_name = f"{name} {family_name}".strip()
            
            print(f"Hello World, Patient: {full_name}")
        else:
            print("Hello World, Patient: No data found")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    fetch_patient_data()

