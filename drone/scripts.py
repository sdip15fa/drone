import os


def main():
    os.system("python3 ./drone/index.py")


def wifi():
    os.system("python3 ./drone/wifi.py")


def land():
    os.system("python3 ./drone/land.py")


def emergency():
    os.system("python3 ./drone/emergency.py")

def docker():
    os.system("docker build . -t wcyat/drone")

def docker_arm64():
    os.system("docker build . --platform=linux/arm64 -t wcyat/drone")

def docker_arm64_qemu():
    os.system("docker run --rm --privileged multiarch/qemu-user-static --reset -p yes && docker buildx build . --platform=linux/arm64 -t wcyat/drone")

def docker_i386():
    os.system("docker build . --platform=linux/i386 -t wcyat/drone")

def docker_i386_qemu():
    os.system("docker run --rm --privileged multiarch/qemu-user-static --reset -p yes && docker buildx build . --platform=linux/i386 -t wcyat/drone")

def docker_amd64():
    os.system("docker build . --platform=linux/amd64 -t wcyat/drone")

def docker_amd64_qemu():
    os.system("docker run --rm --privileged multiarch/qemu-user-static --reset -p yes && docker buildx build. --platform=linux/amd64 -t wcyat/drone")
