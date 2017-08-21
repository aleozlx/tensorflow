# Description:
#   Contains ops for superpixel pooling.

package(
    default_visibility = ["//visibility:private"],
    features = ["-parse_headers"],
)

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

load("//tensorflow:tensorflow.bzl", "tf_custom_op_library")
load("//tensorflow:tensorflow.bzl", "tf_gen_op_libs")
load("//tensorflow:tensorflow.bzl", "tf_gen_op_wrapper_py")
load("//tensorflow:tensorflow.bzl", "tf_kernel_library")
load("//tensorflow:tensorflow.bzl", "cuda_py_test")
# load("//tensorflow:tensorflow.bzl", "tf_custom_op_py_library")
# load("//tensorflow:tensorflow.bzl", "py_test")

tf_custom_op_library(
    name = "ops/_spfreq_ops.so",
    srcs = [
    ],
    gpu_srcs = [
        "ops/spfreq.cc",
        "kernels/spfreq_kernel.cu.cc",
        "include/spfreq.h",
    ],
)

tf_gen_op_libs(
    op_lib_names = ["spfreq_ops"],
)

cuda_py_test(
    name = "spfreq_ops_test",
    # size = "medium",
    srcs = ["python/spfreq_ops_test.py"],
    # additional_deps = [
    #     ":image_py",
    #     ":single_image_random_dot_stereograms_py",
    #     "//third_party/py/numpy",
    #     "//tensorflow/python:array_ops",
    #     "//tensorflow/python:framework_for_generated_wrappers",
    #     "//tensorflow/python:framework_test_lib",
    #     "//tensorflow/python:math_ops",
    #     "//tensorflow/python:platform_test",
    # ],
)

# tf_kernel_library(
#     name = "spfreq_kernel",
#     srcs = ["kernels/spfreq_kernel.cu"],
#     visibility = ["//visibility:public"],
#     # deps = [
#     #     "//tensorflow/core:framework",
#     #     "//tensorflow/core:lib",
#     #     "//tensorflow/core:lib_internal",
#     #     "//tensorflow/core/kernels:bounds_check_lib",
#     #     "//third_party/eigen3",
#     # ],
# )

# tf_custom_op_py_library(
#     name = "cudnn_rnn_py",
#     srcs = [
#         "__init__.py",
#         "python/ops/cudnn_rnn_ops.py",
#     ],
#     dso = [
#         ":python/ops/_cudnn_rnn_ops.so",
#     ],
#     kernels = [
#         ":cudnn_rnn_kernels",
#         ":cudnn_rnn_ops_op_lib",
#     ],
#     srcs_version = "PY2AND3",
#     visibility = ["//visibility:public"],
#     deps = [
#         ":cudnn_rnn_ops",
#         "//tensorflow/contrib/util:util_py",
#         "//tensorflow/python:array_ops",
#         "//tensorflow/python:control_flow_ops",
#         "//tensorflow/python:framework",
#         "//tensorflow/python:framework_for_generated_wrappers",
#         "//tensorflow/python:platform",
#         "//tensorflow/python:state_ops",
#         "//tensorflow/python:training",
#     ],
# )

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
        ],
    ),
    visibility = ["//third_party/tensorflow:__subpackages__"],
)
