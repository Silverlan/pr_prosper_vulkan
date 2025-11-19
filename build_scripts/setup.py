import os
import subprocess
from sys import platform
import tarfile
from pathlib import Path
import urllib.request
import shutil
import config

os.chdir(deps_dir)

if build_all:
	# This script is based on https://github.com/humbletim/setup-vulkan-sdk

	########## Vulkan SDK ##########
	# Note: When updating to a newer version, make sure to update SPIRV-Tools in pragma/build_scripts/build.py accordingly.
	# Also, the new vulkan headers should be copied over to external_libs/prosper_vulkan/third_party_libs/anvil/include/vulkan
	# as well as the vk_enum_string_helper.h header, which can be found here:
	# https://github.com/KhronosGroup/Vulkan-Utility-Libraries/blob/vulkan-sdk-<query_version>/include/vulkan/vk_enum_string_helper.h
	query_version = "1.4.313.0"
	sdk_components = "Vulkan-Headers, Vulkan-Loader"

	if platform == "linux":
		sdk_platform = "linux"
	else:
		sdk_platform = "windows"

	def lunarg_fetch_sdk_config(platform,query_version):
		import urllib
		url = "https://vulkan.lunarg.com/sdk/config/" +query_version +"/" +platform +"/config.json"
		urllib.request.urlretrieve(url,"config.json")

	vulkan_build_dir = deps_dir +"/_vulkan_build"
	mkdir(vulkan_build_dir,cd=True)
	vulkan_config = os.getcwd() +"/config.json"
	print_msg("Fetching Vulkan SDK config...")
	lunarg_fetch_sdk_config(sdk_platform,query_version)

	if platform == "win32":
		vulkan_build_tools = vulkan_build_dir +"/tools"
		mkdir(vulkan_build_tools,cd=True)
		vulkan_bin_dir = vulkan_build_tools +"/bin"
		mkdir(vulkan_bin_dir,cd=True)
		print_msg("Downloading ninja...")
		http_extract("https://github.com/ninja-build/ninja/releases/download/v1.10.2/ninja-win.zip")

	vulkan_cmake = os.path.dirname(os.path.realpath(__file__)) +"/vulkan_sdk"
	vulkan_sdk_dir = deps_dir +"/VULKAN_SDK"
	os.environ["VULKAN_SDK"] = normalize_path(vulkan_sdk_dir)
	args = []
	args += ["-S",normalize_path(vulkan_cmake)]
	args += ["-B",normalize_path(vulkan_build_dir)]
	args += ["-DVULKAN_SDK=" +normalize_path(vulkan_sdk_dir)]
	args += ["-DVULKAN_SDK_CONFIG=" +normalize_path(vulkan_config)]
	args += ["-DVULKAN_SDK_COMPONENTS=" +normalize_path(sdk_components)]
	args += ["-DALLOW_EXTERNAL_SPIRV_TOOLS=1"]
	args += ["-DSPIRV_TOOLS_DIR=" +deps_dir +"/SPIRV-Tools"]
	args += ["-G",generator]

	print_msg("Configuring Vulkan SDK...")
	subprocess.run(["cmake"] +args,check=True)
	print_msg("Building Vulkan SDK...")
	subprocess.run(["cmake","--build",normalize_path(vulkan_build_dir),"--config","Release"],check=True)
	print_msg("Installing Vulkan SDK...")
	subprocess.run(["cmake","--install",normalize_path(vulkan_build_dir),"--config","Release"],check=True)

	copy_prebuilt_directory(vulkan_sdk_dir, "vulkan")

	########## CrashDiagnosticLayer ##########
	cdl_root_dir = deps_dir +"/CrashDiagnosticLayer"
	if not Path(cdl_root_dir).is_dir():
		print_msg("CrashDiagnosticLayer not found. Downloading...")
		os.chdir(deps_dir)
		git_clone("https://github.com/Silverlan/CrashDiagnosticLayer.git", branch = "fixes")

	os.chdir(cdl_root_dir)
	reset_to_commit("2e7398cbba93133dad7073d55550cb9cdfc1d114")

	# Build
	print_msg("Building CrashDiagnosticLayer...")
	mkdir("build",cd=True)
	cmake_configure("..",generator,["-DUPDATE_DEPS=ON", "-DCMAKE_BUILD_TYPE=" +build_config])
	cmake_build(build_config)

	copy_prebuilt_binaries(cdl_root_dir +"/build/src/" +build_config, "crash_diagnostic_layer")
	res_dir = get_library_root_dir("crash_diagnostic_layer") +"resources"
	mkpath(res_dir)
	cp(cdl_root_dir +"/build/src/json/crash_diagnostic_layer.json", res_dir +"/VK_LAYER_LUNARG_crash_diagnostic.json")

add_pragma_module(
    name = "pr_nsight_aftermath",
    repositoryUrl = "https://github.com/Silverlan/pr_nsight_aftermath.git",
    commitSha = "6c1c25eb04aa740f319cb5cedb8e21478346a93a"
)
