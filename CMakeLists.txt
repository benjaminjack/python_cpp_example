cmake_minimum_required(VERSION 2.8.12)
project(python_cpp_example)

SET(SOURCE_DIR "python_cpp_example")
SET(SOURCES "${SOURCE_DIR}/main.cpp")

add_subdirectory(lib/pybind11)
pybind11_add_module(python_cpp_example ${SOURCES} "${SOURCE_DIR}/bindings.cpp")