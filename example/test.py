from ocp_practice_gu import ocp_helper
optimized_neb = ocp_helper.run_relaxation('IS.xsd','IS_relax.traj','IS_relaxed.xsd')
optimized_neb = ocp_helper.run_relaxation('FS.xsd','FS_relax.traj','FS_relaxed.xsd')
optimized_neb = ocp_helper.run_neb('IS_relax.traj','FS_relax.traj',8)