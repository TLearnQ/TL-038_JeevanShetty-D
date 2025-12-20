echo "Hostname:"
hostname | sed 's/$//'

echo "Active Interface:"
ip route | grep default | awk '{print $5}'

echo "Local IPs:"
ip addr | grep inet | awk '{print $2}' | cut -d/ -f1 | grep -v 127.0.0.1

echo "Gateway:"
ip route | awk '/default/ {print $3}'

echo "DNS Servers:"
cat /etc/resolv.conf | grep nameserver | awk '{print $2}'

echo "TCP Established Connections:"
awk 'NR>1 { if ($4 == "01") count++ } END { print count+0 }' /proc/net/tcp