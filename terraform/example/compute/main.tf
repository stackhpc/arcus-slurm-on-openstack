terraform {
  required_version = ">= 0.12, < 0.13"
}

provider "local" {
  version = "~> 1.4"
}

locals {
  config = yamldecode(file("../config.yml"))
}

module "ironic_compute" {
  source = "../../modules/ironic_compute"

  cluster_name = "jg"
}
