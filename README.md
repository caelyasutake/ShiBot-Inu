# ShiBot-Inu

![](./media/cad_render.gif)

## Overview

ShiBot-Inu is a custom built quadruped robot designed for simulation and reinforcement learning. This repository includes the URDF description of ShiBot-Inu, Isaac Sim assets, and the control scripts.

## Simulation Demos

![](./media/robot_many.gif)

Training is done on thousands of robot environments in parallel to speed up training of the PPO algorithm.

![](./media/robot_single.gif)

After 5000 training iterations, the ShiBot-Inu was able to learn a fast walking gait.

## Training and Play

The following command is used to train the robot on 1000 environments without GUI.
```bash
python scripts/rsl_rl/train.py --task=Template-Shibot-Inu-Rl-Direct-v0 --num_envs=1000 --headless
```

The following command is used to test the learned policy of the robot with GUI.
```bash
python scripts/rsl_rl/play.py --task=Template-Shibot-Inu-Rl-Direct-v0 --num_envs=1000
```
