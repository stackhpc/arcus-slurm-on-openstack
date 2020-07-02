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

  os_cloud = local.config.cloud.name
}
