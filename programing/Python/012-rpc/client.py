import Pyro4

def get_server_data():
    uri = "PYRO:obj_6570324c2e6049ebbaefd63d3fd8dd1a@localhost:65108"
    server = Pyro4.Proxy(uri)
    return server.get_data()

print(get_server_data())