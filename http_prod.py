log_takens= "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2".split()
ip = log_takens[9]
month, day, time, host, *message_ports= log_takens

print(f"[PARSED] Date: {month} {day} {time}, Host: {host}")
print(f"[MESSAGE]: {"".join(message_ports)}")
print(f"[IP]: {" ".join(ip)}")
