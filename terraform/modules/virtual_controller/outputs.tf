output "login_ip_addr" {
  value = openstack_compute_instance_v2.login[0].network[0].fixed_ip_v4
}
