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
    i = 0
    for key in data:
        print (i)
        
        list_services.append(key.name)
        #if key.name == 'AutonomousDataWarehouse':
         #   list_services.append(key.fields[1])    
        #    print(key.fields[1])

    #print(list_services)

    for service, j in enumerate(list_services):
        list_all.append(service[j])

    print(len(list_services))
    return list_services

