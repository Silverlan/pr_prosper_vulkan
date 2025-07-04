set(INSTALL_PATH "modules/graphics/vulkan")
pr_install_create_directory("${INSTALL_PATH}")
pr_install_targets(pr_prosper_vulkan prosper_vulkan INSTALL_DIR "${INSTALL_PATH}")

set(LAYER_DIR "${INSTALL_PATH}/layers")
pr_install_create_directory("${LAYER_DIR}")
pr_install_binaries("crash_diagnostic_layer" INSTALL_DIR "${LAYER_DIR}")
pr_install_directory("${crash_diagnostic_layer_RESOURCE_DIR}/" INSTALL_DIR "${LAYER_DIR}")
