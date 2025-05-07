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
    
    return LaunchDescription([
        #lancer Gazebo
        ExecuteProcess(
            cmd=['gz','sim','-v4','empty.sdf'],
            output='screen'
        ),
    
        # Robot state publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        
        #Spawner dans gazebo
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name','staubli_tx2_60l',
                '-topic','robot_description'
            ],
            output='screen'
        ),
        
        #Bridge Ros <-> Gazebo
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
            '/world/default/model/staubli_tx2_60l/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model',
            '/world/default/model/staubli_tx2_60l/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V'
            ],
            output ='screen'
        )
    ])
