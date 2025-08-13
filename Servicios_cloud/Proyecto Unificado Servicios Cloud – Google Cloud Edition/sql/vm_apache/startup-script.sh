#!/bin/bash
apt-get update
apt-get install -y apache2
systemctl enable apache2
systemctl start apache2
echo "<h1>It works - PUSC-GCE</h1>" > /var/www/html/index.html
