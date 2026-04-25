def get_service(port):
    services = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS"
    }
    return services.get(port, "Unknown")


def try_banner(socket_obj):
    try:
        banner = socket_obj.recv(1024).decode().strip()
        return banner if banner else "No banner"
    except:
        return "No banner"