cmake_minimum_required(VERSION 3.12)

include("./CMakeShared.txt")

set(PROJ_NAME pr_prosper_vulkan)

project(${PROJ_NAME} CXX)

# set(PRECOMPILED_HEADER "stdafx")




#set(DEPENDENCY_ANVIL_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/include CACHE PATH "Path to include directory." FORCE)
#set(DEPENDENCY_ANVIL_BUILD_INCLUDE ${CMAKE_CURRENT_BINARY_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/include CACHE PATH  "Path to include directory." FORCE)
#set(DEPENDENCY_ANVIL_DEPS_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/deps CACHE PATH "Path to include directory." FORCE)


#set(DEPENDENCY_PROSPER_VULKAN_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/include CACHE PATH "Path to include directory." FORCE)

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

link_generic_module_libraries()
register_pragma_module(${PROJ_NAME})

#

# add_subdirectory(external_libs/prosper_vulkan)
search_lib_recursive_ext(DEPENDENCY_PROSPER_VULKAN_LIBRARY prosper_vulkan)

set(DEPENDENCY_GLSLANG_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang CACHE STRING "" FORCE)
search_lib_recursive(DEPENDENCY_GLSLANG_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang glslang STATIC)

set(VULKAN_SDK "$ENV{VULKAN_SDK}" CACHE INTERNAL "Path to Vulkan SDK.")

if(WIN32)
        set(DEPENDENCY_VULKAN_INCLUDE "${VULKAN_SDK}/Include" CACHE PATH "Path to include directory." FORCE)
	search_lib_recursive(DEPENDENCY_SPIRV_TOOLS_LIBRARY third_party_libs/vulkan/spirv-tools/source/${BINARY_PRAGMA_DIR} SPIRV-Tools)
	search_lib_recursive(DEPENDENCY_SPIRV_TOOLS_OPT_LIBRARY third_party_libs/vulkan/spirv-tools/source/opt/${BINARY_PRAGMA_DIR} SPIRV-Tools-opt)
	search_lib_recursive(DEPENDENCY_GLSLANG_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/${BINARY_PRAGMA_DIR} glslang)
	search_lib_recursive(DEPENDENCY_GLSLANG_OGL_COMPILER_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/OGLCompilersDLL/${BINARY_PRAGMA_DIR} OGLCompiler)
	search_lib_recursive(DEPENDENCY_GLSLANG_MACHINE_INDEPENDENT_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/${BINARY_PRAGMA_DIR} MachineIndependent)
	search_lib_recursive(DEPENDENCY_GLSLANG_GENERIC_CODE_GEN_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/${BINARY_PRAGMA_DIR} GenericCodeGen)
	search_lib_recursive(DEPENDENCY_SPIRV_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/SPIRV/${BINARY_PRAGMA_DIR} SPIRV)
	search_lib_recursive(DEPENDENCY_GLSLANG_OS_DEPENDENT_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/OSDependent/Windows/${BINARY_PRAGMA_DIR} OSDependent)
	search_lib_recursive(DEPENDENCY_SPV_REMAPPER_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/SPIRV/${BINARY_PRAGMA_DIR} SPVRemapper)
	# search_lib_recursive(DEPENDENCY_HLSL_LIBRARY "${VULKAN_SDK}/glslang/${BINARY_PRAGMA_DIR}/hlsl/${BINARY_PRAGMA_DIR}/HLSL")

	search_lib_recursive_full(DEPENDENCY_VULKAN_LIBRARY "${VULKAN_SDK}/Lib/vulkan-1")
else()

    if(NOT "${VULKAN_SDK}" STREQUAL "")
        set(DEPENDENCY_VULKAN_INCLUDE "${VULKAN_SDK}/include" CACHE PATH "Path to include directory." FORCE) #linux or macs are case-sensitive.
    else()
        set(DEPENDENCY_VULKAN_INCLUDE "/usr/include" CACHE PATH "Path to include directory." FORCE)
    endif()
        #we do not know where the libraries live. They may be in /usr/lib, or /usr/lib/{gcc-arch-id},or /usr/local/lib (Or God knows where really) or at VULKAN_SDK. Hint the last one to the library searcher.
        #set(ENV{PKG_CONFIG_PATH} "${VULKAN_SDK}/lib/pkgconfig")
        #set(TMP_VAR "")
        #find_library(TMP_VAR NAMES vulkan HINTS "${VULKAN_SDK}/lib" NO_CACHE)
        #set(DEPENDENCY_VULKAN_LIBRARY "${TMP_VAR}" CACHE PATH "" FORCE)
        #unset(TMP_VAR)
	# search_lib_recursive_full(DEPENDENCY_GLSLANG_LIBRARY )
	# search_lib_recursive_full(DEPENDENCY_GLSLANG_OGL_COMPILER_LIBRARY )
	# search_lib_recursive_full(DEPENDENCY_GLSLANG_OS_DEPENDENT_LIBRARY )
	# search_lib_recursive_full(DEPENDENCY_HLSL_LIBRARY )




        search_lib_recursive(DEPENDENCY_SPIRV_TOOLS_LIBRARY third_party_libs/vulkan/spirv-tools/source/${BINARY_PRAGMA_DIR} SPIRV-Tools STATIC)
        search_lib_recursive(DEPENDENCY_SPIRV_TOOLS_OPT_LIBRARY third_party_libs/vulkan/spirv-tools/source/opt/${BINARY_PRAGMA_DIR} SPIRV-Tools-opt STATIC)
        search_lib_recursive(DEPENDENCY_GLSLANG_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/${BINARY_PRAGMA_DIR} glslang STATIC)
        search_lib_recursive(DEPENDENCY_GLSLANG_OGL_COMPILER_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/OGLCompilersDLL/${BINARY_PRAGMA_DIR} OGLCompiler STATIC)
        search_lib_recursive(DEPENDENCY_GLSLANG_MACHINE_INDEPENDENT_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/${BINARY_PRAGMA_DIR} MachineIndependent STATIC)
        search_lib_recursive(DEPENDENCY_GLSLANG_GENERIC_CODE_GEN_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/${BINARY_PRAGMA_DIR} GenericCodeGen STATIC)
        search_lib_recursive(DEPENDENCY_SPIRV_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/SPIRV/${BINARY_PRAGMA_DIR} SPIRV STATIC)
        search_lib_recursive(DEPENDENCY_GLSLANG_OS_DEPENDENT_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/glslang/OSDependent/Unix/${BINARY_PRAGMA_DIR} OSDependent STATIC)
        search_lib_recursive(DEPENDENCY_SPV_REMAPPER_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/deps/glslang/SPIRV/${BINARY_PRAGMA_DIR} SPVRemapper STATIC)
endif()


search_lib_recursive(DEPENDENCY_ANVIL_LIBRARY external_libs/prosper_vulkan/third_party_libs/anvil/${BINARY_PRAGMA_DIR} Anvil STATIC)

if(UNIX)
	# resolve_links(DEPENDENCY_VULKAN_LIBRARY)
	# resolve_links(DEPENDENCY_SPIRV_LIBRARY)
endif()

# Vulkan
set(SPIRV_SKIP_EXECUTABLES ON CACHE BOOL ON FORCE)
set(SPIRV_SKIP_TESTS ON CACHE BOOL ".." FORCE)
set(BUILD_SHARED_LIBS OFF CACHE BOOL OFF FORCE)


if("${VULKAN_SDK}" STREQUAL "")

    #don't even bother trying to find tools

    if("${DEPENDENCY_SPIRV_TOOLS_DIR}" STREQUAL "")
        message(ERROR "DEPENDENCY_SPIRV_TOOLS_DIR is not set! pr_prosper_vulkan will NOT be built!")
        return()
    else()

        # add_subdirectory("${DEPENDENCY_SPIRV_TOOLS_DIR}" third_party_libs/vulkan/spirv-tools)

    endif()
else()

    set(DEPENDENCY_SPIRV_TOOLS_DIR "${VULKAN_SDK}/SPIRV-tools" CACHE PATH "Path to spirv-tools repo" FORCE)
    # add_subdirectory(${DEPENDENCY_SPIRV_TOOLS_DIR} third_party_libs/vulkan/spirv-tools)
endif()

set(BUILD_SHARED_LIBS ON CACHE BOOL ".." FORCE)
