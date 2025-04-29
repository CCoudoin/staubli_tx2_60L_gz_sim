from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    urdf_file = '/home/clement/ros2_ws/src/staubli_tx2_60l_gz_sim/urdf/tx2_60l.urdf'

    return LaunchDescription([
        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}],
        ),

        # Launch RViz
        ExecuteProcess(
            cmd=['rviz2'],
            output='screen'
        )
    ])
