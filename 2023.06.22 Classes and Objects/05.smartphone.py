class Smartphone:
    def __init__(self, memory):
        self.memory = memory

    apps = []
    is_on = False

    def power(self):
        if not Smartphone.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.is_on and self.memory >= app_memory:
            Smartphone.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(Smartphone.apps)}. Memory left: {self.memory}"
