# Run Bush

# Nginx
if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm -rf /etc/nginx/sites-enabled/default
fi
touch /home/box/nginx.log
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/ask.conf
sudo /etc/init.d/nginx restart
