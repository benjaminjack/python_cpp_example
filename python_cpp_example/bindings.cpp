#include <pybind11/pybind11.h>
#include "main.hpp"

namespace py = pybind11;

PYBIND11_PLUGIN(python_cpp_example)
{
    py::module m("python_cpp_example", R"doc(
        Pybind11 example plugin
        -----------------------
        .. currentmodule:: python_cpp_example
        .. autosummary::
           :toctree: _generate
           
           add
           subtract
    )doc");

    m.def("add", &add, R"doc(
        Add two numbers
        Some other explanation about the add function.
    )doc");

    m.def("subtract", &subtract, R"doc(
        Subtract two numbers
        Some other explanation about the subtract function.
    )doc");

#ifdef VERSION_INFO
    m.attr("__version__") = py::str(VERSION_INFO);
#else
    m.attr("__version__") = py::str("dev");
#endif

    return m.ptr();
}