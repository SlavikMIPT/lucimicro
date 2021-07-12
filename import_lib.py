import subprocess

print("Mbed deploy")
subprocess.run(["mbed-tools", "deploy", "-f"])

print("Clone flatbuffers")
subprocess.run(["git", "clone", "https://github.com/google/flatbuffers.git"])

print("Clone ONE")
subprocess.run(["git", "clone", "https://github.com/Samsung/ONE.git"])

print("Clone eigen")
subprocess.run(["git", "clone", "https://gitlab.com/libeigen/eigen.git"])

print("Clone gemmlowp")
subprocess.run(["git", "clone", "https://github.com/google/gemmlowp.git"])

print("Clone tensorflow")
subprocess.run(["git", "clone", "https://github.com/tensorflow/tensorflow.git"])

print("Clone ruy")
subprocess.run(["git", "clone", "https://github.com/google/ruy.git"])
