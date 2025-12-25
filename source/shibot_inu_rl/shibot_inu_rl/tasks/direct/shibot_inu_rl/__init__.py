import gymnasium as gym

from . import agents

##
# Register Gym environments.
##


gym.register(
    id="Template-Shibot-Inu-Rl-Direct-v0",
    entry_point=f"{__name__}.shibot_inu_rl_env:ShibotInuEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.shibot_inu_rl_env_cfg:ShibotInuEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:PPORunnerCfg",
    },
)