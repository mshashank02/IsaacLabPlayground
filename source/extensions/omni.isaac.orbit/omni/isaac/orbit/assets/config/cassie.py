# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for Agility robots.

The following configurations are available:

* :obj:`CASSIE_CFG`: Agility Cassie robot with simple PD controller for the legs

Reference: https://github.com/UMich-BipedLab/Cassie_Model/blob/master/urdf/cassie.urdf
"""

from __future__ import annotations

import omni.isaac.orbit.sim as sim_utils
from omni.isaac.orbit.actuators import ImplicitActuatorCfg
from omni.isaac.orbit.utils.assets import ISAAC_ORBIT_NUCLEUS_DIR

from ..articulation import ArticulationCfg

##
# Configuration
##


CASSIE_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ORBIT_NUCLEUS_DIR}/Robots/Agility/Cassie/cassie.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.9),
        joint_pos={
            "hip_abduction_left": 0.1,
            "hip_rotation_left": 0.0,
            "hip_flexion_left": 1.0,
            "thigh_joint_left": -1.8,
            "ankle_joint_left": 1.57,
            "toe_joint_left": -1.57,
            "hip_abduction_right": -0.1,
            "hip_rotation_right": 0.0,
            "hip_flexion_right": 1.0,
            "thigh_joint_right": -1.8,
            "ankle_joint_right": 1.57,
            "toe_joint_right": -1.57,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=["hip_.*", "thigh_.*", "ankle_.*"],
            effort_limit=200.0,
            velocity_limit=10.0,
            stiffness={
                "hip_abduction.*": 100.0,
                "hip_rotation.*": 100.0,
                "hip_flexion.*": 200.0,
                "thigh_joint.*": 200.0,
                "ankle_joint.*": 200.0,
            },
            damping={
                "hip_abduction.*": 3.0,
                "hip_rotation.*": 3.0,
                "hip_flexion.*": 6.0,
                "thigh_joint.*": 6.0,
                "ankle_joint.*": 6.0,
            },
        ),
        "toes": ImplicitActuatorCfg(
            joint_names_expr=["toe_.*"],
            effort_limit=20.0,
            velocity_limit=10.0,
            stiffness={
                "toe_joint.*": 20.0,
            },
            damping={
                "toe_joint.*": 1.0,
            },
        ),
    },
)