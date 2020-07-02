data "external" "openstack_baremetal" {
    program = ["${path.module}/baremetal.py"]

    query = {
        cloud = local.config.cloud.name
        resource_class = local.config.cluster.compute.resource_class,
        cluster = "${local.config.cluster.name}-${local.config.cluster.compute.name}-" ,
        value = "id"
        num_nodes = local.config.cluster.compute.num_nodes
    }
}

