import pytest
import ctypes

# Load the Go binary as a shared library
lib = ctypes.CDLL("./bazel-bin/src/main")

def test_add():
    assert lib.Add(2, 3) == 5
