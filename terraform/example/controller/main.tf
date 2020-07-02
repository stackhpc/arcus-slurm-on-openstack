terraform {
  required_version = ">= 0.12, < 0.13"
}

provider "local" {
  version = "~> 1.4"
}


locals {
  config = yamldecode(file("../config.yml"))
}

module "virtual_controller" {
  source = "../../modules/virtual_controller"

  os_cloud = local.config.os_cloud
  cluster_name = local.config.cluster_name

  image_name = local.config.controller.image_name
  flavor_name = local.config.controller.flavor_name
  key_pair = local.config.controller.key_pair
  networks = local.config.controller.networks
  hostname_prefix = local.config.controller.hostname_prefix
  vm_count = local.config.controller.vm_count
}
