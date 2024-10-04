import json

NETGEAR_AUTH_URL = None
BLOCK_IP_ADDRESSES = None

def load(filename="properties.json"): 
    global NETGEAR_AUTH_URL, BLOCK_IP_ADDRESSES

    valid_portals = ["http://192.168.0.1/", "http://192.168.1.1/"]

    with open(filename, "r") as property_file:
        attributes = json.load(property_file)

        portal_url = attributes["netgearPortal"]
        netgear_user = attributes["netgearUser"]
        netgear_password = attributes["netgearPassword"]
        
        BLOCK_IP_ADDRESSES = attributes["blockIPAddresses"]

        if portal_url not in valid_portals:
            raise TypeError("Netgear portal invalid")
        
        if not isinstance(netgear_user, str) or not isinstance(netgear_password, str):
            raise TypeError("Netgear credentials must be type string")

        if not isinstance(BLOCK_IP_ADDRESSES, list) and all(isinstance(address, str) for address in BLOCK_IP_ADDRESSES):
            raise TypeError("Blocked IP addresses must be type list of strings")

        http = len("http://")
        access_page = "AccessControl.htm"
        auth = f"{netgear_user}:{netgear_password}@"
        auth_url = portal_url[:http] + auth + portal_url[http:] + access_page

        NETGEAR_AUTH_URL = auth_url
    
load()