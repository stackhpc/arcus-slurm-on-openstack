output KUBECONFIG {
  value       = module.cluster.kubeconfig
  description = "location of kubectl configuration file"
}
