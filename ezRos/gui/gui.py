from random import uniform
from tkinter import *
import tkinter as tk
import os
from _root_path import ROOT_DIRECTORY


class GUI():
    def __init__(self) -> None:
        pass

    def gui(self):

        window = tk.Tk()
        window.title("ezRos")
        window.geometry("300x300")

        frame = tk.Frame(window)
        frame.pack()

        def open_sensors():
            sensorwindow = Toplevel(window)

            sensorwindow.title("Select the sensor to mount")

            sensorwindow.geometry("200x200")

            def click(count):
                os.system(
                    f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/4_{count}_x_alpha_gazebo_environment.world")

            Grid.rowconfigure(sensorwindow, 0, weight=1)
            Grid.columnconfigure(sensorwindow, 0, weight=1)

            Grid.rowconfigure(sensorwindow, 1, weight=1)
            Grid.columnconfigure(sensorwindow, 1, weight=0)

            Grid.rowconfigure(sensorwindow, 2, weight=1)
            Grid.columnconfigure(sensorwindow, 1, weight=0)

            nosensors = tk.Button(
                sensorwindow, text="No sensors", bg="#DADAE6", command=lambda: click(0))
            nosensors.grid(row=0, column=0, columnspan=2,
                           sticky="NSEW", ipadx=50, ipady=50)

            laser = tk.Button(sensorwindow, text="Laser",
                              bg="#007FFF", command=lambda: click(1))
            laser.grid(row=1, column=0, sticky="NSEW", ipadx=50, ipady=50)

            camera = tk.Button(sensorwindow, text="Camera",
                               bg="#F6D55C", command=lambda: click(2))
            camera.grid(row=2, column=0, sticky="NSEW", ipadx=50, ipady=50)

            camlaser = tk.Button(sensorwindow, text="Camera and Laser",
                                 bg="#38a500", width=12, command=lambda: click(3))
            camlaser.grid(row=1, column=1, rowspan=2, sticky="NSEW")

            close = tk.Button(sensorwindow, text="Close",
                              bg="red", command=sensorwindow.destroy)
            close.grid(row=3, column=0, columnspan=2, sticky="NSEW")

            sensorwindow.mainloop()

        def installer():

            installerwindow = Toplevel(window)

            installerwindow.title("Installations")

            def select(path):
                os.system(
                    f"sudo bash {ROOT_DIRECTORY}/Installation-Scripts/{path}")

            Grid.rowconfigure(installerwindow, 5, weight=1)
            Grid.columnconfigure(installerwindow, 0, weight=1)

            python = tk.Button(
                installerwindow, text="Python", bg="#DADAE6", command=lambda: select("python/python.sh"))
            python.grid(row=0, column=0,
                        sticky="NSEW", ipadx=25, ipady=25)

            ros2 = tk.Button(installerwindow, text="Ros2",
                             bg="#DADAE6", command=lambda: select("ros2/ros2.sh"))
            ros2.grid(row=0, column=1, sticky="NSEW", ipadx=25, ipady=25)

            gazebo = tk.Button(installerwindow, text="Gazebo",
                               bg="#DADAE6", command=lambda: select("gazebo/gazebo.sh"))
            gazebo.grid(row=1, column=0, sticky="NSEW", ipadx=25, ipady=25)

            slam = tk.Button(installerwindow, text="Slam",
                             bg="#DADAE6", command=lambda: select("slam/SLAM.sh"))
            slam.grid(row=1, column=1, sticky="NSEW", ipadx=25, ipady=25)

            rviz2 = tk.Button(installerwindow, text="rviz2",
                              bg="#DADAE6", command=lambda: select("rviz2/rviz2.sh"))
            rviz2.grid(row=2, column=0, sticky="NSEW", ipadx=25, ipady=25)

            close = tk.Button(installerwindow, text="Close",
                              bg="#FF8C73", command=installerwindow.destroy)
            close.grid(row=2, column=1, columnspan=2, sticky="NSEW")

            installerwindow.mainloop()

        def installation_tester():

            testing_window = Toplevel(window)

            testing_window.title("Tests")

            def select(path):
                os.system(
                    f"sudo bash {ROOT_DIRECTORY}/Installation-Scripts/{path}")

            Grid.rowconfigure(testing_window, 5, weight=1)
            Grid.columnconfigure(testing_window, 0, weight=1)

            python = tk.Button(
                testing_window, text="Python", bg="#DADAE6", command=lambda: select("python/test_python.sh"))
            python.grid(row=0, column=0,
                        sticky="NSEW", ipadx=25, ipady=25)

            ros2 = tk.Button(testing_window, text="Ros2",
                             bg="#DADAE6", command=lambda: select("ros2/test_ros2.sh"))
            ros2.grid(row=0, column=1, sticky="NSEW", ipadx=25, ipady=25)

            slam = tk.Button(testing_window, text="Slam",
                             bg="#DADAE6", command=lambda: select("slam/slam_test.sh"))
            slam.grid(row=1, column=0, sticky="NSEW", ipadx=25, ipady=25)

            close = tk.Button(testing_window, text="Close",
                              bg="#FF8C73", command=testing_window.destroy)
            close.grid(row=1, column=1, columnspan=2, sticky="NSEW")

            testing_window.mainloop()

        install_button = tk.Button(frame,
                                   text="Install",
                                   command=installer)
        install_button.pack(pady=20, fill=BOTH)

        install_button = tk.Button(frame,
                                   text="Deploy Rover",
                                   command=open_sensors)

        install_button.pack(pady=20, fill=BOTH)

        install_button = tk.Button(frame,
                                   text="Test Installations",
                                   command=installation_tester)
        install_button.pack(pady=20, fill=BOTH)

        window.mainloop()
