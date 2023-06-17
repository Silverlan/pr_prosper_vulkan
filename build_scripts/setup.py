import os
import subprocess
from sys import platform
import tarfile
from pathlib import Path
import urllib.request

os.chdir(deps_dir)

# This script is based on https://github.com/humbletim/setup-vulkan-sdk

########## Vulkan SDK ##########
query_version = "1.3.250.0"
sdk_components = "Vulkan-Headers, Vulkan-Loader, Glslang"

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

print_msg("Configuring Vulkan SDK...")
subprocess.run(["cmake"] +args,check=True)
print_msg("Building Vulkan SDK...")
subprocess.run(["cmake","--build",normalize_path(vulkan_build_dir),"--config","Release"],check=True)
print_msg("Installing Vulkan SDK...")
subprocess.run(["cmake","--install",normalize_path(vulkan_build_dir),"--config","Release"],check=True)

cmake_args.append("-DVULKAN_SDK=" +normalize_path(vulkan_sdk_dir))
