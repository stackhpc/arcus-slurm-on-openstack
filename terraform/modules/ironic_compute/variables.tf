#
# Required Parameters
#

variable "cluster_name" {
  description = "Name of the mangum cluster created"
  type        = string
}

#
# Optional Parameters
#

variable "public_key_file" {
  description = "Location of public_key_file"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}
