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
        """)

        Assembler().assemble(wheel_input)
