set(PCK "crash_diagnostic_layer")

if (${PCK}_FOUND)
  return()
endif()

find_library(${PCK}_LIBRARY
  NAMES VkLayer_crash_diagnostic
  HINTS
    ${PRAGMA_DEPS_DIR}/crash_diagnostic_layer/lib
)

find_path(${PCK}_RESOURCE_DIR
  NAMES VK_LAYER_LUNARG_crash_diagnostic.json
  HINTS
    ${PRAGMA_DEPS_DIR}/crash_diagnostic_layer/resources
)

set(REQ_VARS ${PCK}_RESOURCE_DIR ${PCK}_LIBRARY)

if(WIN32)
  find_file(
    ${PCK}_RUNTIME
    NAMES VkLayer_crash_diagnostic.dll
    HINTS
      ${PRAGMA_DEPS_DIR}/crash_diagnostic_layer/bin
  )
  set(REQ_VARS ${REQ_VARS} ${PCK}_RUNTIME)
endif()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(${PCK}
  REQUIRED_VARS ${REQ_VARS}
)
