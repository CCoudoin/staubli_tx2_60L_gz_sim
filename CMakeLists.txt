cmake_minimum_required(VERSION 3.8)
project(staubli_tx2_60l_gz_sim)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME})

install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME})

install(FILES package.xml
  DESTINATION share/${PROJECT_NAME})

ament_package()
