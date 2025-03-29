load("@rules_python//python:defs.bzl", "py_test")

filegroup(
    name = "requirements_lock",
    srcs = ["requirements_lock.txt"],
    visibility = ["//visibility:public"],
)

py_test(
    name = "python_tests",
    srcs = ["test_main.py"],
    main = "test_main.py", 
    deps = [
        "@pypi//pytest",
    ],
    data = ["//src:main_so"],
)
