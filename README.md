# ShiBot-Inu

!(media/cad_image.png)

!(media/cad_render.gif)

## Overview

ShiBot-Inu is a custom built quadruped robot trained using NVIDIA's Isaac Sim and Isaac Lab for reinforcement learning.

## Installation

### Installing Isaac Lab

- Install Isaac Lab by following the [installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html).
  We recommend using the conda or uv installation as it simplifies calling Python scripts from the terminal.

- Clone or copy this project/repository separately from the Isaac Lab installation (i.e. outside the `IsaacLab` directory):

- Using a python interpreter that has Isaac Lab installed, install the library in editable mode using:

    ```bash
    # use 'PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
    python -m pip install -e source/shibot_inu_rl

## Simulation and Learning in Isaac Lab

!(media/robot_many.gif)

!(media/robot_single.gif)

## Usage

Run the following command to train the ShiBot-Inu:
```bash
python scripts/rsl_rl/train.py --task=Template-Shibot-Inu-Rl-Direct-v0 --num_envs=1000 --headless
```

To evaluate play and visualize robot movement, run the following command:
```bash
python scripts/rsl_rl/play.py --task=Template-Shibot-Inu-Rl-Direct-v0 --num_envs=1000
```
