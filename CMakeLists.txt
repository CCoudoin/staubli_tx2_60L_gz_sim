cmake_minimum_required(VERSION 3.8)
project(staubli_tx2_60l_gz_sim)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/launch)

install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}/urdf)

install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME}/meshes)

install(FILES package.xml
  DESTINATION share/${PROJECT_NAME})

ament_package()
