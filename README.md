$ grep vm.max_map_count /etc/sysctl.conf
vm.max_map_count=262144

sysctl -w vm.max_map_count=262144