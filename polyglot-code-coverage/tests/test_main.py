import pytest
import ctypes
import os

# Bazel runfiles helper
def find_shared_lib():
    """Finds the correct path to the compiled Go shared library in the Bazel sandbox."""
    runfiles_dir = os.environ.get("RUNFILES_DIR")
    workspace_name = "polyglot_code_coverage"  # Replace with actual workspace name if different

    #if runfiles_dir:
    #    lib_path = os.path.join(runfiles_dir, workspace_name, "bazel-bin", "src", "main.so")
    #else:
    lib_path = os.path.abspath(os.path.join("/workspaces/polyglot-code-coverage/polyglot-code-coverage/bazel-bin", "src", "main.so"))

    print("DEBUG: Looking for shared lib at:", lib_path)
    return lib_path


# Get the absolute path to the compiled shared library
lib_path = find_shared_lib()

# Load the Go shared library
try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"ERROR: Failed to load shared library: {e}")
    raise

def test_add():
    assert lib.Add(2, 3) == 5
