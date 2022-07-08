import json
import requests

api_url = "http://localhost:58000/api/v1"
user = "admin"
password = "admin1pass"

#Fungsi get ticket rest API
def get_ticket():
    headers = {"content-type": "application/json"}
    body_json = {"username": user, "password": password}
    resp = requests.post(api_url+"/ticket", json.dumps(body_json), headers=headers,  verify=False)
    ticket = resp.json()
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

#Fungsi get network device
def get_network_device():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    resp = requests.get(api_url+"/network-device", headers=headers,  verify=False)
    print("===Get Network Device===")
    print("Request status : ",resp.status_code)
    get_network = resp.json()
    networkDevices = get_network["response"]

    for networkDevice in networkDevices:
        print(networkDevice["hostname"], "\t\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])

#Fungsi get host
def get_host():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    resp = requests.get(api_url+"/host", headers=headers, verify=False)
    print("===Get Host===")
    print("Request status : ",resp.status_code)
    get_host = resp.json()
    hosts = get_host["response"]
    print("Device Name \t IP Address \t MAC Address \t Connected Port")
    for host in hosts:
        print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t\t", host["connectedInterfaceName"])

# Membuat fungsi get network health
def get_network_health():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    resp = requests.get(api_url+"/assurance/health", headers=headers, verify=False)
    get_network_health = resp.json()
    network_health = get_network_health['response'][0]['networkDevices']['totalPercentage']
    return network_health

if __name__ == "__main__":
    print("========REST APIs- Network Controller=======")
    print("===Muhammad Risqi Ramadhan | 190533646857===")
    print("============================================")
    print("Service Ticket REST APIs : " + get_ticket())
    get_network_device()
    get_host()
    print("Persentase Network Health: "+ get_network_health() +"%")
    
