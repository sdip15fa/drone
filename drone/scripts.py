import os


def main():
    os.system("python3 ./drone/index.py")


def wifi():
    os.system("python3 ./drone/wifi.py")

def docker():
    os.system("docker build . -t wcyat/drone")

def docker_arm64():
    os.system("docker run --rm --privileged multiarch/qemu-user-static --reset -p yes && docker buildx build . --platform=linux/arm64 -t wcyat/drone")
