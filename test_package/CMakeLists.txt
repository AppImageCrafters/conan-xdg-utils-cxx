cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)
set (CMAKE_CXX_STANDARD 11)

find_package(XdgUtils REQUIRED COMPONENTS BaseDir DesktopEntry)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE XdgUtils::DesktopEntry XdgUtils::BaseDir)
