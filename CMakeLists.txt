include(${CMAKE_SOURCE_DIR}/cmake/pr_common.cmake)

pr_fetch_module("pr_nsight_aftermath" "https://github.com/Silverlan/pr_nsight_aftermath" "e3fa11f0702f960bab614eb9ead5640ecc1bf48a")

set(PROJ_NAME pr_prosper_vulkan)
pr_add_module(${PROJ_NAME} "modules/graphics/vulkan/")

pr_add_dependency(${PROJ_NAME} client TARGET PUBLIC)

pr_add_sources(${PROJ_NAME} "src/")

add_subdirectory(external_libs/prosper_vulkan)

pr_add_dependency(${PROJ_NAME} prosper_vulkan TARGET PUBLIC)

pr_set_target_folder(prosper_vulkan modules/rendering/vulkan)
pr_set_target_folder(Anvil modules/rendering/vulkan)

pr_finalize(${PROJ_NAME} FOLDER "modules/rendering/vulkan")
