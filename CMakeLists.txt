cmake_minimum_required(VERSION 3.12)

include("./CMakeShared.txt")

set(PROJ_NAME pr_prosper_vulkan)

project(${PROJ_NAME} CXX)

# set(PRECOMPILED_HEADER "stdafx")




set(DEPENDENCY_ANVIL_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/include CACHE PATH "Path to include directory." FORCE)
set(DEPENDENCY_ANVIL_BUILD_INCLUDE ${CMAKE_CURRENT_BINARY_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/include CACHE PATH  "Path to include directory." FORCE)
set(DEPENDENCY_ANVIL_DEPS_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/deps CACHE PATH "Path to include directory." FORCE)


set(DEPENDENCY_PROSPER_VULKAN_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/include CACHE PATH "Path to include directory." FORCE)

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
add_include_dir(anvil)
add_include_dir(materialsystem)
add_include_dir(cmaterialsystem)

add_def(ALSYS_LIBRARY_TYPE)
add_def(ANVIL_VULKAN_CPP)

search_lib_recursive_ext(DEPENDENCY_PROSPER_VULKAN_LIBRARY prosper_vulkan)

link_generic_module_libraries()
register_pragma_module(${PROJ_NAME})

#

add_subdirectory(external_libs/prosper_vulkan)
add_dependencies(${PROJ_NAME} prosper_vulkan)

if(UNIX)
	# resolve_links(DEPENDENCY_VULKAN_LIBRARY)
	# resolve_links(DEPENDENCY_SPIRV_LIBRARY)
endif()
