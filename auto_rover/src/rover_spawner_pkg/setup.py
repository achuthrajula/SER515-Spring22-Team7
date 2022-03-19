from setuptools import setup
import os
from glob import glob

package_name = 'rover_spawner_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Path to the launch file      
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),
        # Path to the world file
        (os.path.join('share', package_name,'worlds/'), glob('./worlds/*')),

        # Path to the warehouse sdf file
        (os.path.join('share', package_name,'models/sample_maze/'), glob('./models/sample_maze/*')),

        # Path to the mobile robot sdf file
        (os.path.join('share', package_name,'models/2_rover/'), glob('./models/2_rover/*')),
        
        # Path to the world file (i.e. warehouse + global environment)
        (os.path.join('share', package_name,'models/'), glob('./worlds/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jnr',
    maintainer_email='pbumadi@asu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_demo = rover_spawner_pkg.spawn_demo:main'
        ],
    },
)
