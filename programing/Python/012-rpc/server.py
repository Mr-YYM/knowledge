import Pyro4

@Pyro4.expose
class MyServer:
    def __init__(self):
        self.data = "Hello, world!"

    def get_data(self):
        return self.data

daemon = Pyro4.Daemon()
uri = daemon.register(MyServer)
print("Ready. Object uri = ", uri)
daemon.requestLoop()