#
# Required Parameters
#

variable "os_cloud" {
  description = "OpenStack creds in clouds.yaml"
  type = string
}

variable "cluster_name" {
  description = "Name of the mangum cluster created"
  type = string
}

variable "image_name" {
  description = "Name of image in openstack cloud"
  type = string
}

variable "flavor_name" {
  description = "Name of baremetal flavor. Must match hostnames."
  type = string
}

variable "key_pair" {
  description = "Name of key_pair to inject"
  type = string
}

variable "networks" {
  description = "List of network names"
  type = list(string)
}

#
# Optional Parameters
#

variable "public_key_file" {
  description = "Location of public_key_file"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}
