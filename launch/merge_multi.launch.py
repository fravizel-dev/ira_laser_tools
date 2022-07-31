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
                "config",
                "laserscan_merge.yaml",
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

    nodes = [laser_merge]

    return LaunchDescription(
        declared_parameters + declared_arguments + declared_env_vars + nodes
    )
