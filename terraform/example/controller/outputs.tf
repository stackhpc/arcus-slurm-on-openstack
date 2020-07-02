output login_ip {
  value       = module.virtual_controller.vms[0].network[0].fixed_ip_v4
  description = "IP of login node"
}
