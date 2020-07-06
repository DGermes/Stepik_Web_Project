# Run Bush

# Nginx
if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm -rf /etc/nginx/sites-enabled/default
fi
touch /home/box/nginx.log
# sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
