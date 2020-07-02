terraform {
  required_version = ">= 0.12, < 0.13"
}

provider "local" {
  version = "~> 1.4"
}


locals {
  config = yamldecode(file("../deploy.yml"))
}

module "cluster" {
  source = "../../modules/ironic_compute"

  os_cloud = local.config.cloud.name
}
