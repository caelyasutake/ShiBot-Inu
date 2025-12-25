"""Configuration for the shibot_inu robot.

The following configuration parameters are available:

"""

from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg
import isaaclab.sim as sim_utils

SHIBOT_INU_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="C:/dev/shibot_inu/shibot_inu/shibot_inu.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=100.0,
            enable_gyroscopic_forces=True,
            disable_gravity=False,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=1,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.1),
        rot=(0.0, 0.0, 0.0, 1.0),
        joint_pos={
            "l_hip_leg1_joint": 0.0,
            "r_hip_leg1_joint": 0.0,
            "l_hip_leg2_joint": 0.0,
            "r_hip_leg2_joint": 0.0,
            "l_foot_joint1": 0.0,
            "r_foot_joint1": 0.0,
            "l_foot_joint2": 0.0,
            "r_foot_joint2": 0.0,
        },
        joint_vel={
            "l_hip_leg1_joint": 0.0,
            "r_hip_leg1_joint": 0.0,
            "l_hip_leg2_joint": 0.0,
            "r_hip_leg2_joint": 0.0,
            "l_foot_joint1": 0.0,
            "r_foot_joint1": 0.0,
            "l_foot_joint2": 0.0,
            "r_foot_joint2": 0.0,
        },
    ),
    actuators={
        "leg_joints": ImplicitActuatorCfg(
            joint_names_expr=[
                "l_hip_leg1_joint",
                "r_hip_leg1_joint",
                "l_hip_leg2_joint",
                "r_hip_leg2_joint",
                "l_foot_joint1",
                "r_foot_joint1",
                "l_foot_joint2",
                "r_foot_joint2",
            ],
            effort_limit=2.0,
            velocity_limit=11.0,
            stiffness=100.0,
            damping=5.0,
        ),
    },
    soft_joint_pos_limit_factor=2,
)