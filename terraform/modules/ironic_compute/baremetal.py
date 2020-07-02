#!/usr/bin/env python3

from __future__ import print_function
import sys, json, pprint
import openstack
import pprint

from ClusterShell import NodeSet


def get_config():
    config = {}
    if len(sys.argv) == 1:
        # using from terraform
        config = json.load(sys.stdin)
        config["debug"] = False
    else:
        config = dict(
           zip(('os_cloud', 'hostname_pattern', 'cluster_name'),
               sys.argv[1:]))
        config["debug"] = True
        pprint.pprint(config)
    return config


def get_hostnames(host_pattern):
    return list(NodeSet.NodeSet(host_pattern))


def find_baremetal_nodes(conn, hostnames):
    found = []

    nodes = conn.baremetal.nodes()
    for node in nodes:
        if node.name in hostnames:
            found.append({
               "uuid": node["id"],
               "name": node["name"],
               "instance_uuid": node["instance_id"],
            })

    if len(found) != len(hostnames):
        print(found)
        print(hostnames)
        raise Exception("Unable to find all baremetal nodes")

    return found


def print_result(nodes):
    result = {}
    for node in nodes:
        result[node["name"]] = node["uuid"]
    print(json.dumps(result))


config = get_config()
conn = openstack.connection.from_config(cloud=config["os_cloud"])
found = find_baremetal_nodes(conn, get_hostnames(config["hostname_pattern"]))
print_result(found)
