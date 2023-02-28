cmake_minimum_required(VERSION 3.22)

project(compSel_demo)


# Build flags and configs are target specific
include(build_configs.cmake)

# Clear shared library flags
set(CMAKE_SHARED_LIBRARY_LINK_C_FLAGS "")
set(CMAKE_SHARED_LIBRARY_LINK_CXX_FLAGS "")

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS_DEBUG}")
SET(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS_DEBUG}")
SET(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS_DEBUG}")

# Compiler selection
SET(CMAKE_FIND_ROOT_PATH ${TOOLCHAIN_DIR}/${TARGET_TRIPLET} ${EXTRA_FIND_PATH})
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

add_subdirectory(App)

add_executable(compSel_demo main.c)

target_link_libraries(
    compSel_demo
    # Dependencies #
    App
)