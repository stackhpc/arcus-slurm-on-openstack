#!/usr/bin/env python3

""" Terraform external data source to provide mapping of required baremetal nodes.
    Should be passed a json dict on stdin containing (keys/values as strings):
        cloud: name of cloud to query
        resource_class: NB this is case-sensitive!
        cluster: string to look for in instance display name to find existing nodes
        value: property to return for each node, e.g. id
        num_nodes: number of nodes to return - use a -ve value to get all available
    
    Can be used from the command-line by passing values in order above too.
    Note that:
    - `cluster` must be chosen carefully so that this is only instances in this cluster contain this string.
    - Baremetal nodes MUST have their name property set for this to be useful.
    Returns a dict describing baremetal nodes which are either already in the cluster or available to add to it,
    where:
        keys:= node.name
        values:= node.<value>
    This is suitable for using as the `for_each` value for a openstack_compute_instance_v2 resource group.
 """

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
#hostpattern = "sv-b17-u37"
found = find_baremetal_nodes(conn, get_hostnames(config["hostname_pattern"]))
print_result(found)

exit(0)

free_nodes = []
existing_nodes = []
for node in nodes:
    if node.provision_state == 'available':
        free_nodes.append(node)
    elif query['cluster'] in node.instance_info.get('display_name', ''):
        existing_nodes.append(node)
if len(sys.argv) != 1: # using from shell
    print('free:', ', '.join(n.name for n in free_nodes))
    print('existing:', ', '.join(n.name for n in existing_nodes))

# now make this the right length:
nodes = existing_nodes + free_nodes  # want to preserve existing, if any, so those are first
if num_nodes >= 0:
    if len(nodes) < num_nodes:
        raise ValueError('Not enough nodes available: requested %i nodes, %i existing/free' % (num_nodes, len(nodes)))
    nodes = nodes[:num_nodes]
    
if len(sys.argv) != 1: # using from shell
    print('nodes:', ', '.join(n.name for n in nodes))

result = {} # for tf, must return a json dict containing only strings as both keys and values:
for n in nodes:
    if n.name == '' or n.name is None:
        raise ValueError('node does not have name attribute set: %s' % n)
    result[n.name] = getattr(n, query['value'])
if len(sys.argv) == 1: # using from terraform
    print(json.dumps(result))
else:
    pprint.pprint(result)
