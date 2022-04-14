from ezRos.modular_assembly.assembler import Assembler


class TestDrive:

    def __init__(self) -> None:
        pass

    def launch(self):
        wheel_input = input("""
        Enter the number of wheels for the rover\n
        [2] 2x wheels
        [4] 4x wheels
        [6] 6x wheels
        [8] 8x wheels
        """)

        available_sensors = ['laser','camera']
        required_sensors = []
        for sensor in available_sensors:
            sensor_input=  input(f"""
            Do you need the {sensor} sensor\n
            [0] No
            [1] Yes
            """)
            if(sensor_input=='1'):
                required_sensors.append(sensor)

        Assembler().assemble(wheel_input, required_sensors)