import argparse
import json

import requests


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch patient data from the public HAPI FHIR server."
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of patient records to request from the server (default: 1).",
    )
    return parser.parse_args()


def fetch_patient_data(count):
    url = f"https://hapi.fhir.org/baseR4/Patient?_count={count}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        entries = data.get("entry", [])
        if entries:
            for entry in entries:
                patient = entry["resource"]
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
    args = parse_args()
    fetch_patient_data(args.count)
