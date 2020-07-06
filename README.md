# arcus-slurm-on-openstack

## Building the OpenHPC image

- Load your openstack credentials into your environment: 

```
source ~/openrc
```

This is necessary so that the script can upload the images to glance.

- Run the playbook to build the image:

```
cd <GIT_CHECKOUT>/ansible/
ansible-galaxy install -r requirements.yml -p roles
ansible-playbook image-build.yml
```

You should now see the `arcus-openhpc` image registered in glance.
