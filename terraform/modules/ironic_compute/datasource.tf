data "external" "openstack_baremetal" {
    program = ["${path.module}/baremetal.py"]

    query = {
        value = "id"
    }
}

