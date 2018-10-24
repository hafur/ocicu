import oci
"""This is a doc string test"""


def print_resources():
    """This is is an example docstring"""
    config = oci.config.from_file("~/dev/ocicu/.oci/config", "DEFAULT")
    identity = oci.identity.IdentityClient(config)
    user = identity.get_user(config["user"]).data
    print(user)
    resources_tenancy = oci.resource_search.ResourceSearchClient(config)
    resources = resources_tenancy.list_resource_types()
    data = resources.data
    # print(resources.data)
    for key in data:
        print(key.name)
        if key.name == 'AutonomousDataWarehouse':
            print(key.fields[1])


print_resources()
