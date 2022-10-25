ssh pi@192.168.0.17
pw: defaults to raspberry, changed to the plant we're watering


To check for devices on network:
? not working: arp -a | grep raspberry
sudo nmap -sP 192.168.0.0/24
>   Starting Nmap 7.60 ( https://nmap.org ) at 2022-10-20 14:35 CDT
    Nmap scan report for _gateway (192.168.0.1)                                 (router?)
    Host is up (0.0028s latency).
    MAC Address: 5C:E3:0E:40:41:15 (Arris Group)
    Nmap scan report for 192.168.0.3                                             ?
    Host is up (0.083s latency).
    MAC Address: 58:2F:40:0B:4C:E5 (Unknown)
    Nmap scan report for 192.168.0.4                                             ?
    Host is up (0.084s latency).
    MAC Address: 88:66:5A:36:CC:AD (Unknown)
    Nmap scan report for 192.168.0.9                                             ?
    Host is up (0.0032s latency).
    MAC Address: 04:D9:F5:7E:0B:17 (Unknown)
    Nmap scan report for 192.168.0.17                                            pi!
    Host is up (0.014s latency).
    MAC Address: B8:27:EB:80:7C:09 (Raspberry Pi Foundation)
    Nmap scan report for 192.168.0.254                                           ?
    Host is up (-0.16s latency).
    MAC Address: 5C:E3:0E:40:41:19 (Arris Group)
    Nmap scan report for rachel-GS65-Stealth-Thin-8RF (192.168.0.12)             this comp
    Host is up.
    Nmap done: 256 IP addresses (7 hosts up) scanned in 10.86 seconds



i2cdetect 1
>>> with soil sensor plugged in it shows 36!

ran this:
https://github.com/adafruit/Adafruit_CircuitPython_seesaw/blob/main/examples/seesaw_soil_simpletest.py
though the while loop got stuck, had to modify

Download data from pi to local:
scp pi@192.168.0.17:Documents/soil_sensor_readings.csv ~/Code/PlantWaterer/data

### Watering notes
2022-10-07 morning watered plant fully
2022-10-11         watered base
2022-10-14 14:33   watered base
2022-10-17  9:00   watered pot
2022-10-20 14:25   watered pot and base
2022-10-24 14:25   watered pot and base