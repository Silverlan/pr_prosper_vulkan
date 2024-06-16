set(INSTALL_PATH "modules/graphics/vulkan")
pr_install_create_directory("${INSTALL_PATH}")
pr_install_targets(pr_prosper_vulkan prosper_vulkan INSTALL_DIR "${INSTALL_PATH}")
