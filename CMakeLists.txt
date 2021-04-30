cmake_minimum_required(VERSION 3.12)

include("../CMakeShared.txt")

set(PROJ_NAME pr_prosper_vulkan)

project(${PROJ_NAME} CXX)

# set(PRECOMPILED_HEADER "stdafx")

link_external_library(iclient)
link_external_library(glfw)
link_external_library(iglfw)
link_external_library(vulkan)
link_external_library(prosper)
link_external_library(prosper_vulkan)
link_external_library(client)
link_external_library(wgui)
link_external_library(anvil)
add_include_dir(anvil_build)
add_include_dir(anvil_deps)
add_external_library(luajit)
if(WIN32)
	add_external_library(lua)
endif()

add_include_dir(glm)
add_include_dir(alsoundsystem)
add_include_dir(materialsystem)
add_include_dir(cmaterialsystem)

add_def(ALSYS_LIBRARY_TYPE)
add_def(ANVIL_VULKAN_CPP)

link_generic_module_libraries()
register_pragma_module(${PROJ_NAME})

add_dependencies(${PROJ_NAME} prosper_vulkan prosper)
