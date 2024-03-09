import json

def sample_data_parser():
    try:
        with open('sample-data.json') as f:
            data = json.load(f)
            print("Interface Status")
            print("=" * 80)
            print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
            print(f"{'-'*50} {'-'*20} {'-'*8} {'-'*6}")

            for item in data["imdata"]:
                l1PhysIf = item["l1PhysIf"]["attributes"]
                print(f"{l1PhysIf['dn']:<50} {'':<20} {l1PhysIf['speed']:<8} {l1PhysIf['mtu']:<6}")
    except:
        print("json error")
# sample_data_parser()
        