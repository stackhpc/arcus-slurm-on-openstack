data "external" "openstack_baremetal" {
    program = ["${path.module}/baremetal.py"]

    query = {
        os_cloud = var.os_cloud
        hostname_pattern = var.hostname_pattern
        cluster_name = var.cluster_name
    }
}

