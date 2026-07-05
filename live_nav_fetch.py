import requests
import pandas as pd
import os

print("Script Started")

os.makedirs("data/raw/live_nav", exist_ok=True)

schemes = {
    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        latest_nav = data["data"][0]

        df = pd.DataFrame([latest_nav])

        df.to_csv(
            f"data/raw/live_nav/{name}.csv",
            index=False
        )

        print(f"Saved {name}")