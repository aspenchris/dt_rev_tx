import requests
import json
from datetime import datetime, timedelta

address = "0xb44c0b55B437E394Ec32795A5A55e173683aa1FF"
tx_list = ""
start_time = str(datetime.now() - timedelta(minutes=14400))[:17] + '00'
end_time = str(datetime.now() - timedelta(minutes=1))[:17] + '00'
ether_api_key = "3SS6URPD8V8VVP5RJRE54KBGVA3E9E55UP"
base_api_key = "CPYADDR1PQXQX9Z7ZDUCSJHW7IYEG6N2E3"
arb_api_key = "FCY1H7DZHR5RGW8V21PDRJIKM7BZV9DWS1"

def get_ETH_transactions():
    global tx_list
    url = f"https://api.etherscan.io/v2/api?chainid=1&module=account&action=txlist&address={address}&startblock=0&endblock=latest&page=1&offset=1000&sort=asc&apikey={ether_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**18) + ' ETH(ERC20)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_ETH_internal_transactions():
    global tx_list
    url = f"https://api.etherscan.io/v2/api?chainid=1&module=account&action=txlistinternal&address={address}&startblock=0&endblock=latest&page=1&offset=1000&sort=asc&apikey={ether_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**18) + ' ETH(ERC20)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_ETH_erc20token_transactions():
    global tx_list
    url = f"https://api.etherscan.io/api?module=account&action=tokentx&address={address}&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey={ether_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  if str(loaded_detail['tokenSymbol']) == 'USDT' or str(loaded_detail['tokenSymbol']) == 'USDC':
                    tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**int(loaded_detail['tokenDecimal'])) + ' ' + str(loaded_detail['tokenSymbol']) + '(ERC20)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_base_transactions():
    global tx_list
    url = f"https://api.basescan.org/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={base_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**18) + ' ETH(base)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_base_internal_transactions():
    global tx_list
    url = f"https://api.basescan.org/api?module=account&action=txlistinternal&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={base_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**18) + ' ETH(base)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_base_erc20token_transactions():
    global tx_list
    url = f"https://api.basescan.org/api?module=account&action=tokentx&address={address}&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey={base_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  if str(loaded_detail['tokenSymbol']) == 'USDC':
                    tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**int(loaded_detail['tokenDecimal'])) + ' ' + str(loaded_detail['tokenName']) + '(base)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_arb_transaction():
    global tx_list
    url = f"https://api.arbiscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=latest&page=1&offset=10&sort=asc&apikey={arb_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**18) + ' ETH(arb)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

def get_arb_internal_transaction():
    global tx_list
    url = f"https://api.arbiscan.io/api?module=account&action=txlistinternal&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={arb_api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tx = []
            if data['status'] == '1':
              for record in data['result']:
                tx.append(record)
              for item in tx:
                detail = json.dumps(item)
                loaded_detail = json.loads(detail)
                if str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] >= start_time and str(datetime.fromtimestamp(int(loaded_detail['timeStamp'])))[:19] < end_time:
                  tx_list += ' time(UTC): ' + str(datetime.fromtimestamp(int(loaded_detail['timeStamp']))) + '\n amount: ' + str(int(loaded_detail['value'])/10**18) + ' ETH(arb)' + '\n txid: ' + str(loaded_detail['hash']) + '\n from: ' + str(loaded_detail['from']) +"\n\n"
        else:
            return "Error: Unable to fetch data"
    except Exception as e:
        return "Error: " + str(e)

get_ETH_transactions()
get_ETH_internal_transactions()
get_ETH_erc20token_transactions()
get_base_transactions()
get_base_internal_transactions()
get_base_erc20token_transactions()
get_arb_transaction()
get_arb_internal_transaction()

print("run success")
print(tx_list)