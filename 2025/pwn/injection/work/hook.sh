#!/bin/sh

FLAG=$(cat /flag)
cp /nsjail.cfg /tmp/nsjail.cfg
sed -i "s/FLAG_PLACEHOLDER/$FLAG/" /tmp/nsjail.cfg