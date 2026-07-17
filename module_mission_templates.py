# Blood optimization logic
# Only trigger blood particles within 10 meters of the player
(store_distance_to_player, ":dist", ":agent_id"),
(lt, ":dist", 1000), # 1000 units = 10 meters
(particle_system_burst, "psys_blood", pos1, 50),
