import subprocess

def test_sample_app():
    result = subprocess.run(["./sample"], capture_output=True)
    print(result.stdout.decode())
    assert result.returncode == 0