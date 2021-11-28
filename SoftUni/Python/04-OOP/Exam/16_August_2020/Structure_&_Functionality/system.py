from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        new = PowerHardware(name, capacity, memory)
        System._hardware.append(new)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        new = HeavyHardware(name, capacity, memory)
        System._hardware.append(new)

    @staticmethod
    def _hardware_by_name(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System._hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
        except Exception:
            return "Software cannot be installed"

        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System._hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
        except Exception:
            return "Software cannot be installed"

        System._software.append(software)

    @staticmethod
    def _software_by_name(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

    @staticmethod
    def release_software_component(hardware_name, software_name):
        software = System._software_by_name(software_name)
        hardware = System._hardware_by_name(hardware_name)

        if software is None or hardware is None:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        memory_used = 0
        total_memory = 0
        capacity_used = 0
        total_capacity = 0

        for hardware in System._hardware:
            total_memory += hardware.memory
            total_capacity += hardware.capacity
            memory_used += hardware.used_memory
            capacity_used += hardware.used_capacity

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {memory_used} / {total_memory}\n" \
               f"Total Capacity Taken: {capacity_used} / {total_capacity}"

    @staticmethod
    def system_split():
        info = []
        for hardware in System._hardware:
            soft_components = [s.name for s in hardware.software_components]
            information = f"Hardware Component - {hardware.name}\n" \
                          f"Express Software Components: {len([s for s in hardware.software_components if s.software_type == 'Express'])}\n" \
                          f"Light Software Components: {len([s for s in hardware.software_components if s.software_type == 'Light'])}\n" \
                          f"Memory Usage: {hardware.used_memory} / {hardware.memory}\n" \
                          f"Capacity Usage: {hardware.used_capacity} / {hardware.capacity}\n" \
                          f"Type: {hardware.hardware_type}\n" \
                          f"Software Components: {', '.join(soft_components) if soft_components else 'None'}"

            info.append(information)

        return '\n'.join(info)