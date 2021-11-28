from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.used_capacity = 0
        self.memory = memory
        self.used_memory = 0
        self.software_components = []

    def install(self, software: Software):
        if self.memory < software.memory_consumption or self.capacity < software.capacity_consumption:
            raise Exception("Software cannot be installed")

        self.used_memory += software.memory_consumption
        self.used_capacity += software.capacity_consumption
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.used_memory -= software.memory_consumption
            self.used_capacity -= software.capacity_consumption
            self.software_components.remove(software)