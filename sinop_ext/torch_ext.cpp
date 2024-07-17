#include <torch/extension.h>
#include <cstdint>
#include <cstdio>
#include <pybind11/pybind11.h>
#include <ATen/ATen.h>

void mysin(torch::Tensor a) {
    at::sin_(a);
}

void sin_pybind(torch::Tensor a) {
    at::sin_(a);
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("sin_pybind", &sin_pybind, "sin_pybind");
}

TORCH_LIBRARY(mycppops, m) {
  m.def("sin", &mysin);
}
