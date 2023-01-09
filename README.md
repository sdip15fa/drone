# Drone

Python program to control a dji tello edu drone, using missions pads.

## Libraries

- [djitellopy](https://github.com/damiafuentes/DJITelloPy/)

## Mission pads

Upon detecting a new mission pad (must be of a different number), the drone would fly to the pad,
different pads would involve different actions.

By default, the drone would move according to as if the mission pad is [1](#1).

### 1

Move forwards, 30cm at a time, non-stop until detecting another pad

### 2

Move backwards, 30cm at a time, non-stop until detecting another pad

### 3

Move leftwards, 30cm at a time, non-stop until detecting another pad

### 4

Move rightwards, 30cm at a time, non-stop until detecting another pad

### 5

Move up 30cm, then do the previous action if previous mission pad is 1-4, else do [1](#1).

### 6

Move down 30cm, then do the previous action if previous mission pad is 1-4, else do [1](#1).

### 7

Move a left-right-left path to move around an obstacle, x and y distance and times can be adjusted using .env.

### 8

Land. Everything stops.

## Environmental variables

Copy the example to `.env`:

```bash
cp example.env .env
```

### TELLO_IP

Ip of the tello drone, usually `192.168.10.1`.

If not ping the addresses starting from `192.168.10.2`, `192.168.10.3` and so on.

```bash
ping 192.168.10.2
```

To make sure the ip belongs to the drone:

```bash
nmap 192.168.10.1 -p 8889
```

### TELLO_WIFI_PASSWORD

The password for the wifi you would setup when running the script [wifi](#wifi).

## Scripts

### Install

```bash
poetry install
```

### Start

Start up the drone, controlled using the [mission pads](#mission-pads).

```bash
poetry run start
```

### Wifi

Setup wifi password according to the env variable [`TELLO_WIFI_PASSWORD`](#tello_wifi_password).

```bash
poetry run wifi
```

### Land

Land the drone.

```bash
poetry run land
```

### Emergency

Emergency mode: stop the engines immediately.

```bash
poetry run emergency
```
