#!/bin/sh
set -e

VERIFIER_HOST="${VERIFIER_HOST:-verifier}"
VERIFIER_PORT="${VERIFIER_PORT:-5000}"

echo "[entrypoint] Resolving verifier: $VERIFIER_HOST"

VERIFIER_IP="$(getent hosts "$VERIFIER_HOST" | awk '{print $1}' | head -n1)"

if [ -z "$VERIFIER_IP" ]; then
  echo "[entrypoint] ERROR: Could not resolve $VERIFIER_HOST"
  exit 1
fi

echo "[entrypoint] Verifier IP: $VERIFIER_IP"

echo "[entrypoint] Setting iptables rules..."

# Flush existing rules
iptables -F
iptables -X

# Default: drop all outbound
iptables -P INPUT  ACCEPT
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Allow established connections to continue
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow loopback (localhost)
iptables -A OUTPUT -o lo -j ACCEPT

# Allow outbound TCP only to verifier:port
iptables -A OUTPUT -p tcp -d "$VERIFIER_IP" --dport "$VERIFIER_PORT" -j ACCEPT

echo "[entrypoint] iptables ready. Starting app..."

exec node index.mjs
