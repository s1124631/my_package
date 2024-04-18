from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return_LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable = 'listener'
        )
    ])