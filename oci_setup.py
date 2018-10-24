import oci
import json

config = oci.config.from_file("~/dev/ocicu/.oci/config", "DEFAULT")

# print(config)

identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
# print(user)


resources_tenancy = oci.resource_search.ResourceSearchClient(config)

resources = resources_tenancy.list_resource_types()

data = resources.data

# print(resources.data)

for key in data:
    print(key.name)
    if (key.name=='AutonomousDataWarehouse'):
        print(key.fields[1])




# instances = oci.core.ComputeClient(config)

# print(instances)

# inst = instances.list_images(config["compartment_id"]).data
# print(inst)


