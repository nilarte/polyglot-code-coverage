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

genrule(
    name = "main_so",
    srcs = ["main.go"],
    outs = ["main.so"],  # Generates shared library and header
    cmd = "mkdir -p /tmp/go-cache && GOCACHE=/tmp/go-cache go build -buildmode=c-shared -o $(location main.so) $(location main.go)",
    tools = ["@go_sdk//:bin/go"],
    visibility = ["//visibility:public"],
)
