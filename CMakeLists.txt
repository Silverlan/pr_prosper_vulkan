include(${CMAKE_SOURCE_DIR}/cmake/pr_common.cmake)

set(PROJ_NAME pr_prosper_vulkan)
pr_add_module(${PROJ_NAME} SHARED "modules/graphics/vulkan/")

pr_add_dependency(${PROJ_NAME} client TARGET PUBLIC)

pr_add_headers(${PROJ_NAME} "include/")
pr_add_sources(${PROJ_NAME} "src/")

add_subdirectory(external_libs/prosper_vulkan)

pr_add_dependency(${PROJ_NAME} prosper_vulkan TARGET PUBLIC)

pr_set_target_folder(prosper_vulkan modules/rendering/vulkan)
pr_set_target_folder(Anvil modules/rendering/vulkan)

pr_finalize(${PROJ_NAME} FOLDER "modules/rendering/vulkan")
