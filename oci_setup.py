import oci
"""This is a doc string test"""

def print_resources():
    """This is is an example docstring"""
    config = oci.config.from_file("/mnt/c/Users/klazarz/Desktop/dev/ocicu/.oci/config", "DEFAULT")
    #identity = oci.identity.IdentityClient(config)
    #user = identity.get_user(config["user"]).data
    #print(user)
    resources_tenancy = oci.resource_search.ResourceSearchClient(config)
    resources = resources_tenancy.list_resource_types()
    data = resources.data
    #print(resources.data)
    list_services = []
    
    for key in data:
        list_services.append(key.name)
        #if key.name == 'AutonomousDataWarehouse':
         #   list_services.append(key.fields[1])    
        #    print(key.fields[1])

    #print(list_services)

    list_all = []
    for service in list_services:
        list_all.append(service)

    #    print(list_all)
    return list_all

