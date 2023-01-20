from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    declared_arguments = []
    declared_env_vars = []
    declared_parameters = []

    params_file = LaunchConfiguration("params_file")

    declared_arguments.append(
        DeclareLaunchArgument(
            "params_file",
            default_value=os.path.join(
                get_package_share_directory("ira_laser_tools"),
                "launch",
                "laserscan_merge.yaml", #_real
            ),
            description="Path to param config in yaml format",
        ),
    )

    laser_merge = Node(
        package="ira_laser_tools",
        executable="laserscan_multi_merger",
        name="laserscan_multi_merger",
        parameters=[params_file],
        output="both",
        # respawn=True,
        # respawn_delay=2,
    )

    #Set transform
    tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        output="screen",
        arguments=["0", "0", "0", "0", "0", "0","base_link","base_laser_link"]
    )

    # laser_virtualizer = Node(
    #     package="ira_laser_tools",
    #     executable="laserscan_virtualizer",
    #     name="laserscan_virtualizer",
    #     #parameters=[params_file],
    #     output="both",
    #     # respawn=True,
    #     # respawn_delay=2,
    # )

    nodes = [laser_merge, tf]

    return LaunchDescription(
        declared_parameters + declared_arguments + declared_env_vars + nodes
    )
