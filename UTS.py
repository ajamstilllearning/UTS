import scapy.all as scapy

# ==============================
# MAN PAGE CONTENT
# ==============================

UTS_MAN = """
UTS - Uncomplicated Traffic Scanner

SYNOPSIS:
    [OPTIONS]

DESCRIPTION:
    UTS is a lightweight traffic monitoring tool designed
    to inspect and analyze network packets in a simplified way.

OPTIONS:
    -d(default)     Enable debug mode (show detailed packet info)
    -t [PORT]       Sniff HTTP/HTTPS traffic on specified port
    -T              Sniff HTTP/HTTPS traffic on default ports (80 and 443)
    -h              Show help menu
    
COMMANDS:
    man             Show full manual page
    help            Show help menu
    exit            Exit UTS shell
"""

# ==============================
# HELP FUNCTION
# ==============================

def show_help():
    print("Available commands:")
    print("  -d              Enable debug mode")
    print("  -t [PORT]       Sniff HTTP/HTTPS traffic")
    print("  -T              Sniff HTTP/HTTPS traffic (default ports 80 and 443)")
    print("  -h              Show help")
    print("  -o              Scan own network for active hosts")
    print("  man             Show manual page")
    print("  exit            Exit program")
    

def proses_paket(packet):
    if packet.haslayer('IP'):
        print(f"Deteksi Traffic: {packet['IP'].src} -> {packet['IP'].dst} | Protokol: {packet.summary()}")

# def tcp_sniffer(packet):
    if packet.haslayer('TCP'):
        print(f"Deteksi Traffic TCP: {packet['IP'].src} -> {packet['IP'].dst} | Protokol: {packet.summary()}")

def tcp_sniff_port(packet, port):
    if packet.haslayer('TCP') and (packet['TCP'].sport == port or packet['TCP'].dport == port):
        print(f"Deteksi Traffic TCP Port {port}: {packet['IP'].src} -> {packet['IP'].dst} | Protokol: {packet.summary()}")

def scan_own_network():
    scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="192.168.1.0/24"))
    

# ==============================
# COMMAND PARSER
# ==============================

def parse_command(command_line):
    args = command_line.strip().split()

    if not args:
        return

    #(no dash)
    if args[0] == "man":
        print(UTS_MAN)
        return

    if args[0] in ["exit", "quit"]:
        print("Exiting UTS...")
        exit()

    # Option parsing
    i = 0
    while i < len(args):
        arg = args[i]

        if str.strip(arg) == "-h" or str.strip(arg) == "help":
            show_help()
            return
        
        elif str.strip(arg) == "-d":
            try:
                scapy.sniff(prn=proses_paket, store=False)
            except KeyboardInterrupt:
                return

        elif str.strip(arg) == "-T":
            try:
                scapy.sniff(filter="tcp port 80 or port 443", prn=lambda x: x.summary(), store=False)
            except KeyboardInterrupt:
                return
            
        elif str.strip(arg) == "-t":
                try:
                    port = int(args[i + 1])
                    scapy.sniff(filter=f"tcp port {port}", prn=lambda x: tcp_sniff_port(x, port), store=False)
                except (IndexError, ValueError):
                    print("UTS error: -t requires numeric argument")
                    i += 1
                    return

        elif str.strip(arg) == "-o":
            try:
                scan_own_network() 
            except KeyboardInterrupt:
                return
            
        elif str.strip(arg) == "clear":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"UTS error: unknown option '{arg}'")
            return

        i += 1


# ==============================
# MAIN LOOP (INTERACTIVE SHELL)
# ==============================

def main():
    import pyfiglet
    ascii_art = pyfiglet.figlet_format("UTS")
    print(ascii_art)
    print("uncomplicated traffic scanner - by Ajam WHO HATES UTS DADAKAN HARI SENIN\n")
    print("Type 'help' or 'man' for commands.\n")

    while True:
        try:
            command = input("UTS > ")
            parse_command(command)

        except KeyboardInterrupt:
            exit()
        except EOFError:
            import time
            print("\nExiting UTS...")
            time.sleep(0.5)
            break


if __name__ == "__main__":
    main()