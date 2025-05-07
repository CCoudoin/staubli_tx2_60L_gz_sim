import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join (get_package_share_directory('staubli_tx2_60l_gz_sim'),
    'urdf',
    'tx2_60l.urdf'
    )
    #urdf_file = '/home/clement/ros2_ws/src/staubli_tx2_60l_gz_sim/urdf/tx2_60l.urdf'
    
    return LaunchDescription([
    
        # Joint State Publisher
        Node (
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen'
        ),
        # Robot state publisher
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
