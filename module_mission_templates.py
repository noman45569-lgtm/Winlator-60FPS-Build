
(ti_on_agent_hit, 0, 0, [], 
  [
    (store_trigger_param_1, ":agent_id"),
    (store_distance_to_player, ":dist", ":agent_id"),
    (lt, ":dist", 1000), # Sirf 10 meter ke andar
    (particle_system_burst, "psys_blood", pos1, 50),
  ]),
