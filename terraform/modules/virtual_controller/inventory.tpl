[login]
%{ for login in logins}${login.name} ansible_host=${login.network[0].fixed_ip_v4} server_networks='${jsonencode({for net in login.network: net.name => [ net.fixed_ip_v4 ] })}'
%{ endfor ~}
