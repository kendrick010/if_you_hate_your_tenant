# if_you_hate_your_tenant

Automate and control WiFi device connections using NETGEAR Gateway Portal and Selenium. 

## Setup

Install dependecies,
```
pip3 install -r requirements.txt
```

Create a `properties.json` file in the root project directory and populate your gateway credentials and the unwanted device IP addresses,
```
{
    "netgearPortal": "http://192.168.0.1/",
    "netgearUser": "******",
    "netgearPassword": "******"
    "blockIPAddresses": ["192.***.***.***", "192.***.***.***"]
}
```

Typically, your NETGEAR router's gateway portal is found on `http://192.168.0.1/` or `http://192.168.1.1/`. The default username and password is also typically `admin` and `password` respectively.

## Run

To block your listed devices, run
```
python3 wifi_block.py true
```

Else to allow access again,
```
python3 wifi_block.py false
```

For the blocked devices, their WiFi connection will still show "connected", but they won't be able to use internet.