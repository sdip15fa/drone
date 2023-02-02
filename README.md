# Drone

Python program to control a dji tello edu drone, using missions pads.

## Libraries

- [djitellopy](https://github.com/damiafuentes/DJITelloPy/)

## Mission pads

Upon detecting a new mission pad (must be of a different number), the drone would fly to the pad,
different pads would involve different actions.

By default, the drone would move according to as if the mission pad is [1](#1).

Upon detecting a new mission pad, the drone will go to the position (0,0,100) with respect to the mission pad.

### Functions

Forward, Backward, Leftward, Rightward: distance can be changed using the env variable `DISTANCE`.

Most one-time functions expect the mission pad to be placed in front of the center of the obstacle.

#### Forward

Move forwards, non-stop until detecting another pad

#### Back

Move backwards, non-stop until detecting another pad

#### Left

Move leftwards, non-stop until detecting another pad

#### Right

Move rightwards, non-stop until detecting another pad

#### Up

Move up, then do the previous action if previous mission pad is 1-4, else do [1](#1).

The z-coordinate of the position upon detecting a new mission pad would be increased by the configured height.

The move up height is configurable via the env variable `HEIGHT`

#### Down

Move down, then do the previous action if previous mission pad is 1-4, else do [1](#1).

The z-coordinate of the position upon detecting a new mission pad would be decreased by the configured height.

The move down height is configurable via the env variable `HEIGHT`

#### Around

Move a right-forward-left path to move around an obstacle, x (`AROUND_X`) and y (`AROUND_Y`) distance and (`AROUND`) times can be adjusted using .env.

If times is more than one the drone would move using an s-shape path (right-forward-left then left-forward-right).

If another mission pad is placed on its course the drone would reposition itself to that mission pad after a right-forward-left or left-forward-right path. The drone would then follow the instruction of that mission pad after this function is finished.

#### Tunnel

Move to a lowest possible height, and then
move in accordance if the previous mission pad has the instruction

- [Forward](#forward)
- [Back](#back)
- [Left](#left)
- [Right](#right)

Otherwise move in accordance with [Forward](#forward).

#### Go through

Rise to the height specified by the env variable `MAX_HEIGHT`.

Then move forward very slowly (0.1m/s) until a tof distance significantly less than the initial is detected (detection interval is 0.1s).

Initial tof distance - detected tof distance would be treated as the height of the obstacle.

The drone would then return to the mission pad and try to pass through the obstacle using the height obtained.

**_WARNING_**: DO NOT place any other mission pads between the mission pad for this function and the obstacle.

#### Rotate

Rotate 30 degrees clockwise. The times to rotate could be adjusted using the env variable `ROTATE`.

#### Snake

Move in an s-shape path (right-forward-left then left-forward-right).

Using [Around](#around) with `AROUND=2` can achieve the same result.

#### Circle (square)

Move a right-forward-left-back-right path (like a square), finally returns to the mission pad.

#### Land

Auto land. The program is exited after that.

### Mode 1

`MODE=1`

#### 1

[Forward](#forward)

#### 2

[Back](#back)

#### 3

[Left](#left)

#### 4

[Right](#right)

#### 5

[Up](#up)

#### 6

[Down](#down)

#### 7

[Around](#around)

#### 8

[Land](#land)

### Mode 2

`MODE=2`

#### 1

[Forward](#forward)

#### 2

[Tunnel](#tunnel)

#### 3

[Left](#left)

#### 4

[Right](#right)

#### 5

[Go through](#go-through)

#### 6

[Rotate](#rotate)

#### 7

[Around](#around)

#### 8

[Land](#land)

## Config (environmental variables)

Copy the example to `.env`:

```bash
cp example.env .env
```

The edit the .env file, e ven during runtime it would work (the config is re-read upon every operation).

Most variables are self-explanatory. Here are some of the variables you may find difficult to configure:

### TELLO_IP

Ip of the tello drone, usually `192.168.10.1`.

If not scan all the addresses on the network:

```bash
sudo nmap 192.168.10.0/24 -sU -p 8889
```

To make sure the ip belongs to the drone:

```bash
sudo nmap 192.168.10.1 -sU -p 8889
```

### TELLO_WIFI_PASSWORD

The password for the wifi you would setup when running the script [wifi](#wifi).

### Mode

- `1`: use [mode 1](#mode-1)
- `2`: use [mode 2](#mode-2)

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
