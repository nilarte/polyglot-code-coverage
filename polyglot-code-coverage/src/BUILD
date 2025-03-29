load("@io_bazel_rules_go//go:def.bzl", "go_binary", "go_library", "go_test")

go_library(
    name = "main_lib",
    srcs = ["main.go"],
    importpath = "polyglot/main",
    visibility = ["//visibility:public"],
)

go_binary(
    name = "main",
    embed = [":main_lib"],
)

go_test(
    name = "main_test",
    srcs = ["main_test.go"],  # Optional if you also want Go tests
    embed = [":main_lib"],
)
