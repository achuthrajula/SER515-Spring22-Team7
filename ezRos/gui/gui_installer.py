from tkinter import *
import tkinter as tk
import os
from _root_path import ROOT_DIRECTORY


def installer(window):

    # window = Tk()

    installerwindow = Toplevel(window)

    installerwindow.title("Select the sensor to mount")

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
