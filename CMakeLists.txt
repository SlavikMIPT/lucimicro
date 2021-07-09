# Copyright (c) 2021 ARM Limited. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.19.0)

set(LUCI_MICRO ON CACHE BOOL "LUCI_MICRO BUILD FLAG")
set(MBED_PATH ${CMAKE_CURRENT_SOURCE_DIR}/mbed-os CACHE INTERNAL "")
set(MBED_CONFIG_PATH ${CMAKE_CURRENT_BINARY_DIR} CACHE INTERNAL "")
set(COMPILERS_DIR_PATH /usr/local/bin)
set(CMAKE_C_COMPILER   ${COMPILERS_DIR_PATH}/arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER ${COMPILERS_DIR_PATH}/arm-none-eabi-g++)
set(CMAKE_C_COMPILER_WORKS 1)
set(CMAKE_CXX_COMPILER_WORKS 1)
set(APP_TARGET luci-micro)

set(FLATBUFFERS_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/flatbuffers/include CACHE INTERNAL "")
set(ONE_COMPILER_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/ONE/compiler CACHE INTERNAL "")
set(ONE_INFRA_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/ONE/infra CACHE INTERNAL "")
set(TensorFlowSource_DIR ${CMAKE_CURRENT_SOURCE_DIR}/tensorflow CACHE INTERNAL "")
set(TensorFlowGEMMLowpSource_DIR ${CMAKE_CURRENT_SOURCE_DIR}/gemmlowp CACHE INTERNAL "")
set(TensorFlowEigenSource_DIR ${CMAKE_CURRENT_SOURCE_DIR}/eigen CACHE INTERNAL "")
set(TensorFlowRuySource_DIR ${CMAKE_CURRENT_SOURCE_DIR}/ruy CACHE INTERNAL "")


set(CMAKE_CXX_STANDARD 17)
#set(CMAKE_CXX_EXTENSIONS OFF)

SET(GCC_COVERAGE_COMPILE_FLAGS "-fexceptions -Wno-register -frtti")
SET(GCC_COVERAGE_LINK_FLAGS    "")

SET(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}")
SET(CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}")

include(${MBED_PATH}/tools/cmake/app.cmake)

add_subdirectory(${MBED_PATH})
add_subdirectory(${ONE_COMPILER_SRC_DIR}/luci/lang)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/loco)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/angkor)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/oops)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/pepper-str)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/logo)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/logo-core)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/locomotiv)
add_subdirectory(${ONE_INFRA_SRC_DIR}/nncc)
add_subdirectory(${ONE_COMPILER_SRC_DIR}/luci-interpreter)

#add_subdirectory(${LIB_PATH}/luci/import)
#add_subdirectory(${LIB_PATH}/luci/env)

add_executable(${APP_TARGET}
        main.cpp
        )

project(${APP_TARGET})

# Add FlatBuffers directly to our build. This defines the `flatbuffers` target.
#include_directories(PRIVATE ${FLATBUFFERS_SRC_DIR})
#include_directories(PRIVATE ${ONE_COMPILER_SRC_DIR}/luci-interpreter/include)
#include_directories(PRIVATE ${ONE_COMPILER_SRC_DIR}/luci-interpreter/src)

target_link_libraries(${APP_TARGET} PRIVATE mbed-os)
target_link_libraries(${APP_TARGET} PRIVATE luci_lang)
target_link_libraries(${APP_TARGET} PRIVATE loco)
target_link_libraries(${APP_TARGET} PRIVATE angkor)
target_link_libraries(${APP_TARGET} PRIVATE oops)
target_link_libraries(${APP_TARGET} PRIVATE pepper_str)
target_link_libraries(${APP_TARGET} PRIVATE logo)
target_link_libraries(${APP_TARGET} PRIVATE logo_core)
target_link_libraries(${APP_TARGET} PRIVATE locomotiv)
target_link_libraries(${APP_TARGET} PRIVATE luci_interpreter)

mbed_set_post_build(${APP_TARGET})

option(VERBOSE_BUILD "Have a verbose build process")
if(VERBOSE_BUILD)
    set(CMAKE_VERBOSE_MAKEFILE ON)
endif()
