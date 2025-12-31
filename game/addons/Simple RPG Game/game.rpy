# Simple RPG Game Addon
# - Grid-based movement with collisions
# - External map loader
# - Renders inside a centered overlay panel (CRT-like)

# Tile/panel configuration first so images can reference these values
define rpg_tile_size = 64
# Base pixel size of source assets (8x8 sprites/tiles)
define rpg_asset_base = 8
# Precomputed scale factor (should be an integer for crispness, e.g., 8 when 64/8)
define rpg_scale = rpg_tile_size / rpg_asset_base
# Player collision box size (slightly smaller than tile to fit through corridors)
define rpg_player_size = 60  # 4 pixels smaller than tile (2px margin on each side)
# Size of the RPG panel viewport (maintain normal resolution of an old CRT TV)
define rpg_panel_width = 680
define rpg_panel_height = 520

define rpg_default_map = "addons/Simple RPG Game/maps/level1.txt"

init 1:
    # Image declarations for tiles and sprites
    image rpg_grass = "addons/Simple RPG Game/assets/grass.png"
    image rpg_sand  = "addons/Simple RPG Game/assets/sand.png"
    image rpg_wall  = "addons/Simple RPG Game/assets/wall.png"
    image rpg_breakable_wall = "addons/Simple RPG Game/assets/wall.png"
    image rpg_coin  = "addons/Simple RPG Game/assets/coin.png"
    image rpg_player = "addons/Simple RPG Game/assets/player.png"
    image rpg_enemy = "addons/Simple RPG Game/assets/enemy1.png"
    image rpg_enemyprojectile = "addons/Simple RPG Game/assets/enemyprojectile.png"
    image rpg_sword = "addons/Simple RPG Game/assets/sword.png"
    image rpg_warp = "addons/Simple RPG Game/assets/warpglitchthingy.png"
    image rpg_ourple = "addons/Simple RPG Game/assets/ourple.png"

    # Panel style for CRT-like overlay window
    style rpg_panel_frame is frame
    style rpg_panel_frame:
        background "#202020"
        padding (10, 10)

    # Note: rpg_tile_size and other defines are declared above

    # Pixel-perfect transform for crispy Atari-like look (Ren'Py 6.99)
    transform rpg_pixel:
        nearest True
        subpixel False
        zoom rpg_scale

init python:

    class RPGMap(object):
        """Loads a tile map from a simple text file."""
        def __init__(self, path):
            self.path = path
            self.width = 0
            self.height = 0
            self.tiles = []
            self.player_start = (0, 0)
            self.coins = set()
            self.enemy_spawns = []
            self.warp_tiles = set()  # Warp tile positions
            self.breakable_walls = set()  # Breakable wall positions
            self.mysterious_entity = None  # Position of the mysterious entity (M)
            self._load(path)

        def _load(self, path):
            try:
                f = renpy.file(path)
            except Exception as e:
                renpy.notify("RPG: Failed to open map: %s" % path)
                raise

            # Handle Python 2 vs Python 3 compatibility
            # renpy.file() returns bytes in both versions, but Python 3 needs explicit decoding
            raw_lines = f.readlines()
            if raw_lines and isinstance(raw_lines[0], bytes):
                # Python 3 or binary mode - decode bytes to strings
                lines = [line.decode('utf-8').rstrip("\n\r") for line in raw_lines]
            else:
                # Python 2 or already strings
                lines = [line.rstrip("\n\r") for line in raw_lines]
            self.height = len(lines)
            if lines:
                self.width = max(len(ln) for ln in lines)
            else:
                self.width = 0
            self.tiles = [["." for _ in range(self.width)] for _ in range(self.height)]
            self.coins = set()
            self.enemy_spawns = []
            self.player_start = (0, 0)
            found_player = False

            for r, ln in enumerate(lines):
                for c, ch in enumerate(ln):
                        t = ch
                        if ch == "P":
                            self.player_start = (r, c)
                            found_player = True
                            # Check underlying tile type for spawn
                            if c < len(ln) - 1 and ln[c+1] == "~":
                                t = "~"  # Sand spawn
                            elif c < len(ln) - 1 and ln[c+1] == ".":
                                t = "."  # Grass spawn
                            else:
                                t = "."  # Default to grass
                        elif ch == "C":
                            self.coins.add((r, c))
                            if c < len(ln) - 1 and ln[c+1] == "~":
                                t = "~"
                            elif c < len(ln) - 1 and ln[c+1] == ".":
                                t = "."
                        elif ch == "E":
                            self.enemy_spawns.append((r, c))
                            # Enemy spawns on walkable tile
                            if c < len(ln) - 1 and ln[c+1] == "~":
                                t = "~"
                            else:
                                t = "."
                        elif ch == "W":
                            self.warp_tiles.add((r, c))
                            t = "W"  # Warp tiles are walkable
                        elif ch == "B":
                            self.breakable_walls.add((r, c))
                            t = "B"  # Breakable walls start as solid
                        elif ch == "M":
                            self.mysterious_entity = (r, c)
                            # Entity spawns on walkable tile
                            if c < len(ln) - 1 and ln[c+1] == "~":
                                t = "~"
                            else:
                                t = "."
                        self.tiles[r][c] = t

            if not found_player:
                for rr in range(self.height):
                    for cc in range(self.width):
                        if self.tile_char(rr, cc) in (".", "~"):
                            self.player_start = (rr, cc)
                            found_player = True
                            break
                    if found_player:
                        break

        def in_bounds(self, r, c):
            return 0 <= r < self.height and 0 <= c < self.width

        def tile_char(self, r, c):
            if not self.in_bounds(r, c):
                return "#"
            return self.tiles[r][c]

        def is_solid(self, r, c):
            ch = self.tile_char(r, c)
            return ch == "#" or ch == "B" or ch == "B"  # Wall or Breakable wall

        def is_walkable(self, r, c):
            return not self.is_solid(r, c)


    class Enemy(object):
        """Enemy with random movement and shooting AI."""
        def __init__(self, r, c):
            self.px = c * rpg_tile_size
            self.py = r * rpg_tile_size
            self.speed_pps = 128.0  # Half player speed
            self.direction = (0, 0)  # Current movement direction
            self.move_timer = 0.0  # Time until next direction change
            self.shoot_cooldown = 0.0  # Time until can shoot again
            self.shoot_interval = 2.0  # Seconds between shots
            
        def update(self, dt):
            """Update enemy AI - random movement and shooting."""
            import random
            
            # Random movement
            self.move_timer -= dt
            if self.move_timer <= 0:
                # Pick new random direction
                directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]  # up, down, left, right, idle
                self.direction = random.choice(directions)
                self.move_timer = random.uniform(0.5, 2.0)
            
            # Move in current direction
            dx, dy = self.direction
            if dx != 0 or dy != 0:
                move_dist = self.speed_pps * dt
                step_x = dx * move_dist
                step_y = dy * move_dist
                
                # Try to move (with collision)
                if step_x != 0:
                    new_px = self.px + step_x
                    if not rpg_blocked_at(new_px, self.py):
                        self.px = new_px
                    else:
                        self.move_timer = 0  # Hit wall, pick new direction
                
                if step_y != 0:
                    new_py = self.py + step_y
                    if not rpg_blocked_at(self.px, new_py):
                        self.py = new_py
                    else:
                        self.move_timer = 0  # Hit wall, pick new direction
            
            # Shooting logic
            self.shoot_cooldown -= dt
            if self.shoot_cooldown <= 0:
                # Only shoot if enemy is on screen
                if self.is_on_screen():
                    # Check if player is visible in cardinal direction
                    direction = self.can_see_player()
                    if direction:
                        self.shoot(direction)
                        self.shoot_cooldown = self.shoot_interval
        
        def is_on_screen(self):
            """Check if enemy is visible in the current viewport."""
            if not rpg_xadj or not rpg_yadj:
                return True
            
            # Current viewport bounds
            view_left = rpg_xadj.value
            view_right = view_left + rpg_panel_width
            view_top = rpg_yadj.value
            view_bottom = view_top + rpg_panel_height
            
            # Enemy bounds
            enemy_left = self.px
            enemy_right = self.px + rpg_tile_size
            enemy_top = self.py
            enemy_bottom = self.py + rpg_tile_size
            
            # Check if enemy overlaps with viewport
            return (enemy_left < view_right and enemy_right > view_left and
                    enemy_top < view_bottom and enemy_bottom > view_top)
        
        def can_see_player(self):
            """Check if player is visible in a cardinal direction (no diagonals)."""
            if not rpg_state.map:
                return None
            
            # Enemy center
            ex = self.px + rpg_tile_size / 2
            ey = self.py + rpg_tile_size / 2
            # Player center
            px = rpg_state.player_px + rpg_tile_size / 2
            py = rpg_state.player_py + rpg_tile_size / 2
            
            # Check cardinal directions
            directions = [
                (0, -1, abs(ex - px) < rpg_tile_size / 2 and py < ey),  # up
                (0, 1, abs(ex - px) < rpg_tile_size / 2 and py > ey),   # down
                (-1, 0, abs(ey - py) < rpg_tile_size / 2 and px < ex),  # left
                (1, 0, abs(ey - py) < rpg_tile_size / 2 and px > ex)    # right
            ]
            
            for dx, dy, aligned in directions:
                if not aligned:
                    continue
                
                # Raycast to check for walls
                if dx != 0:  # Horizontal ray
                    step = 1 if dx > 0 else -1
                    start_x = int(ex)
                    end_x = int(px)
                    check_y = int(ey)
                    for x in range(start_x, end_x, step * 8):
                        tile_c = x // rpg_tile_size
                        tile_r = check_y // rpg_tile_size
                        if rpg_state.map.is_solid(tile_r, tile_c):
                            break
                    else:
                        return (dx, dy)
                else:  # Vertical ray
                    step = 1 if dy > 0 else -1
                    start_y = int(ey)
                    end_y = int(py)
                    check_x = int(ex)
                    for y in range(start_y, end_y, step * 8):
                        tile_c = check_x // rpg_tile_size
                        tile_r = y // rpg_tile_size
                        if rpg_state.map.is_solid(tile_r, tile_c):
                            break
                    else:
                        return (dx, dy)
            
            return None
        
        def shoot(self, direction):
            """Create a projectile moving in the given direction."""
            # Spawn projectile at enemy center
            proj_x = self.px + rpg_tile_size / 2 - 8
            proj_y = self.py + rpg_tile_size / 2 - 8
            proj = Projectile(proj_x, proj_y, direction[0], direction[1])
            rpg_state.projectiles.append(proj)
    
    class Projectile(object):
        """Enemy projectile that damages the player."""
        def __init__(self, px, py, dx, dy):
            self.px = px
            self.py = py
            self.dx = dx
            self.dy = dy
            self.speed = 300.0  # Fast projectile
            self.alive = True
        
        def update(self, dt):
            """Move projectile and check collisions."""
            # Move
            self.px += self.dx * self.speed * dt
            self.py += self.dy * self.speed * dt
            
            # Check wall collision
            if rpg_blocked_at(self.px, self.py):
                self.alive = False
                return
            
            # Check player collision (simple bounding box)
            player_left = rpg_state.player_px
            player_right = rpg_state.player_px + rpg_tile_size
            player_top = rpg_state.player_py
            player_bottom = rpg_state.player_py + rpg_tile_size
            
            proj_left = self.px
            proj_right = self.px + 16
            proj_top = self.py
            proj_bottom = self.py + 16
            
            if (proj_left < player_right and proj_right > player_left and
                proj_top < player_bottom and proj_bottom > player_top):
                self.alive = False
                rpg_state.game_over = True


    class RPGState(object):
        def __init__(self):
            self.map = None
            # Tile index position (integers for reference)
            self.player_r = 0
            self.player_c = 0
            # Pixel position (top-left of player sprite)
            self.player_px = 0
            self.player_py = 0
            # Movement speed in pixels per second (not per tick)
            self.speed_pps = 256.0  # pixels per second
            self.score = 0
            # Last tick time for delta calculation
            self.last_tick_time = None
            # Cached map rendering flag
            self.map_changed = True
            # Movement tracking for smart updates
            self.is_moving = False
            self.prev_px = 0
            self.prev_py = 0
            # Enemy and projectile lists
            self.enemies = []
            self.projectiles = []
            self.game_over = False
            self.game_won = False
            self.warping = False  # Flag for warp transition
            self.warp_target_map = None  # Path to map to warp to
            self.sinister_triggered = False  # Flag for mysterious entity attack
            # Player attack state
            self.player_facing = (0, 1)  # Direction player is facing (default: down)
            self.attack_active = False
            self.attack_timer = 0.0  # Time remaining in current attack
            self.attack_duration = 0.2  # Duration of attack animation in seconds
            self.attack_cooldown = 0.0  # Time until can attack again
            self.attack_cooldown_time = 0.3  # Cooldown between attacks
            self.prev_attack_pressed = False  # Track previous attack button state

    rpg_state = RPGState()

    # Viewport adjustments for camera control
    rpg_xadj = None
    rpg_yadj = None
    # Camera smoothing enabled
    rpg_smooth_camera = True
    rpg_camera_speed = 8.0  # Higher = snappier, lower = smoother

    def rpg_update_camera():
        """Keep player in frame with margins by adjusting viewport scroll.
        Supports both instant and smooth camera following."""
        m = rpg_state.map
        if not m:
            return
        # Dimensions
        vw = rpg_panel_width
        vh = rpg_panel_height
        cw = m.width * rpg_tile_size
        ch = m.height * rpg_tile_size
        max_x = max(0, cw - vw)
        max_y = max(0, ch - vh)
        # Current scroll
        sx = rpg_xadj.value if rpg_xadj else 0
        sy = rpg_yadj.value if rpg_yadj else 0
        # Player center from pixel position
        px = rpg_state.player_px + (rpg_tile_size // 2)
        py = rpg_state.player_py + (rpg_tile_size // 2)
        # Margins before we start scrolling
        mx = rpg_tile_size * 2
        my = rpg_tile_size * 2

        # Calculate target camera position
        target_x = sx
        target_y = sy

        # Horizontal
        if px < sx + mx:
            target_x = max(px - mx, 0)
        elif px > sx + vw - mx:
            target_x = min(px - (vw - mx), max_x)

        # Vertical
        if py < sy + my:
            target_y = max(py - my, 0)
        elif py > sy + vh - my:
            target_y = min(py - (vh - my), max_y)

        if rpg_xadj and rpg_yadj:
            if rpg_smooth_camera:
                # Smooth interpolation (lerp)
                lerp_factor = min(1.0, rpg_camera_speed * 0.0167)  # Approximate frame time
                rpg_xadj.value = sx + (target_x - sx) * lerp_factor
                rpg_yadj.value = sy + (target_y - sy) * lerp_factor
            else:
                # Instant snap
                rpg_xadj.value = target_x
                rpg_yadj.value = target_y

    def rpg_get_visible_tile_range(margin=1):
        """Return (start_col, end_col, start_row, end_row) for tiles visible in the panel.
        Extends range by 'margin' tiles to avoid pop-in during scroll."""
        if not rpg_state.map:
            return (0, 0, 0, 0)
        # Current scroll offsets
        sx = int(rpg_xadj.value) if rpg_xadj else 0
        sy = int(rpg_yadj.value) if rpg_yadj else 0
        # Visible tile bounds
        start_col = max(0, sx // rpg_tile_size)
        start_row = max(0, sy // rpg_tile_size)
        end_col = int((sx + rpg_panel_width - 1) // rpg_tile_size)
        end_row = int((sy + rpg_panel_height - 1) // rpg_tile_size)
        # Apply margin and clamp
        start_col = max(0, start_col - margin)
        start_row = max(0, start_row - margin)
        end_col = min(rpg_state.map.width - 1, end_col + margin)
        end_row = min(rpg_state.map.height - 1, end_row + margin)
        return (start_col, end_col, start_row, end_row)

    def rpg_load_map(path):
        global rpg_state
        rpg_state = RPGState()
        rpg_state.map = RPGMap(path)
        rpg_state.player_r, rpg_state.player_c = rpg_state.map.player_start
        # Initialize pixel position to tile position
        rpg_state.player_py = rpg_state.player_r * rpg_tile_size
        rpg_state.player_px = rpg_state.player_c * rpg_tile_size
        rpg_state.map_changed = True
        # Spawn enemies
        for r, c in rpg_state.map.enemy_spawns:
            enemy = Enemy(r, c)
            rpg_state.enemies.append(enemy)
        # Initialize adjustments based on map and viewport sizes
        global rpg_xadj, rpg_yadj
        cw = rpg_state.map.width * rpg_tile_size
        ch = rpg_state.map.height * rpg_tile_size
        max_x = max(0, cw - rpg_panel_width)
        max_y = max(0, ch - rpg_panel_height)
        
        # Calculate initial camera position to center on player
        player_center_x = rpg_state.player_px + (rpg_tile_size // 2)
        player_center_y = rpg_state.player_py + (rpg_tile_size // 2)
        initial_x = player_center_x - (rpg_panel_width // 2)
        initial_y = player_center_y - (rpg_panel_height // 2)
        # Clamp to valid range
        initial_x = max(0, min(initial_x, max_x))
        initial_y = max(0, min(initial_y, max_y))
        
        rpg_xadj = ui.adjustment(range=max_x, value=initial_x, step=rpg_tile_size)
        rpg_yadj = ui.adjustment(range=max_y, value=initial_y, step=rpg_tile_size)
        renpy.restart_interaction()

    def rpg_cleanup():
        """Clean up resources when exiting the RPG game."""
        global rpg_state, rpg_xadj, rpg_yadj
        if rpg_state:
            rpg_state.last_tick_time = None
        # Note: Ren'Py will handle most cleanup automatically

    def rpg_blocked_at(px, py):
        """Check collision for a player at pixel coords px,py against solid tiles.
        Player sprite renders at tile size but collision box is slightly smaller.
        Uses pixel-perfect bounding box collision - any overlap with a solid tile blocks movement."""
        if not rpg_state.map:
            return True
        
        # Calculate player collision box (centered within the sprite, slightly smaller)
        offset = (rpg_tile_size - rpg_player_size) / 2.0
        player_left = px + offset
        player_right = px + offset + rpg_player_size
        player_top = py + offset
        player_bottom = py + offset + rpg_player_size
        
        # Check if position would be out of map bounds
        if player_left < 0 or player_top < 0:
            return True
        max_x = rpg_state.map.width * rpg_tile_size
        max_y = rpg_state.map.height * rpg_tile_size
        if player_right > max_x or player_bottom > max_y:
            return True
        
        # Determine which tiles to check based on player collision box
        min_col = int(player_left // rpg_tile_size)
        max_col = int((player_right - 0.001) // rpg_tile_size)
        min_row = int(player_top // rpg_tile_size)
        max_row = int((player_bottom - 0.001) // rpg_tile_size)
        
        # Clamp to valid tile range
        min_col = max(0, min(min_col, rpg_state.map.width - 1))
        max_col = max(0, min(max_col, rpg_state.map.width - 1))
        min_row = max(0, min(min_row, rpg_state.map.height - 1))
        max_row = max(0, min(max_row, rpg_state.map.height - 1))
        
        # Check each tile the player overlaps with
        for r in range(min_row, max_row + 1):
            for c in range(min_col, max_col + 1):
                if not rpg_state.map.is_walkable(r, c):
                    # This tile is solid - check if player collision box overlaps it
                    tile_left = c * rpg_tile_size
                    tile_right = tile_left + rpg_tile_size
                    tile_top = r * rpg_tile_size
                    tile_bottom = tile_top + rpg_tile_size
                    
                    # Bounding box overlap test (touching edges doesn't count as overlap)
                    if (player_left < tile_right and player_right > tile_left and
                        player_top < tile_bottom and player_bottom > tile_top):
                        return True
        
        return False

    def rpg_move_to_contact(current_val, target_val, current_other, axis):
        """Move along one axis as far as possible without collision.
        Returns the furthest valid position between current and target.
        Optimized: single collision check for most cases.
        
        Args:
            current_val: Current position on the axis we're moving (x or y)
            target_val: Desired position on the axis we're moving
            current_other: Current position on the OTHER axis (stays constant)
            axis: 'x' or 'y' to specify which coordinate is changing
        """
        # If no movement needed, return current position
        if abs(target_val - current_val) < 0.01:
            return current_val
        
        # Check if the full movement is valid (most common case - fast path)
        if axis == 'x':
            blocked = rpg_blocked_at(target_val, current_other)
        else:  # axis == 'y'
            blocked = rpg_blocked_at(current_other, target_val)
        
        # If not blocked, move the full distance
        if not blocked:
            return target_val
        
        # Otherwise, we're blocked - just stay put (wall sliding removed for performance)
        return current_val

    def rpg_check_attack_hits():
        """Check if the player's sword attack hits any enemies or projectiles."""
        if not rpg_state.attack_active:
            return
        
        # Calculate sword hitbox based on player position and facing direction
        player_center_x = rpg_state.player_px + rpg_tile_size / 2
        player_center_y = rpg_state.player_py + rpg_tile_size / 2
        
        dx, dy = rpg_state.player_facing
        
        # Sword reach (extends from player in facing direction)
        sword_reach = rpg_tile_size * 1.2
        sword_width = rpg_tile_size * 0.8
        
        # Calculate sword hitbox rectangle
        if dx != 0:  # Horizontal attack
            sword_center_x = player_center_x + dx * sword_reach / 2
            sword_center_y = player_center_y
            sword_left = sword_center_x - sword_reach / 2
            sword_right = sword_center_x + sword_reach / 2
            sword_top = sword_center_y - sword_width / 2
            sword_bottom = sword_center_y + sword_width / 2
        else:  # Vertical attack
            sword_center_x = player_center_x
            sword_center_y = player_center_y + dy * sword_reach / 2
            sword_left = sword_center_x - sword_width / 2
            sword_right = sword_center_x + sword_width / 2
            sword_top = sword_center_y - sword_reach / 2
            sword_bottom = sword_center_y + sword_reach / 2
        
        # Check collision with enemies
        enemies_to_remove = []
        for enemy in rpg_state.enemies:
            enemy_left = enemy.px
            enemy_right = enemy.px + rpg_tile_size
            enemy_top = enemy.py
            enemy_bottom = enemy.py + rpg_tile_size
            
            if (sword_left < enemy_right and sword_right > enemy_left and
                sword_top < enemy_bottom and sword_bottom > enemy_top):
                enemies_to_remove.append(enemy)
                rpg_state.score += 10  # Bonus points for killing enemies
        
        for enemy in enemies_to_remove:
            rpg_state.enemies.remove(enemy)
        
        # Check collision with projectiles
        projectiles_to_remove = []
        for proj in rpg_state.projectiles:
            proj_left = proj.px
            proj_right = proj.px + 16
            proj_top = proj.py
            proj_bottom = proj.py + 16
            
            if (sword_left < proj_right and sword_right > proj_left and
                sword_top < proj_bottom and sword_bottom > proj_top):
                projectiles_to_remove.append(proj)
        
        for proj in projectiles_to_remove:
            rpg_state.projectiles.remove(proj)

        # Check collision with mysterious entity (ourple)
        if rpg_state.map and rpg_state.map.mysterious_entity:
            mr, mc = rpg_state.map.mysterious_entity
            entity_left = mc * rpg_tile_size
            entity_right = entity_left + rpg_tile_size
            entity_top = mr * rpg_tile_size
            entity_bottom = entity_top + rpg_tile_size
            
            if (sword_left < entity_right and sword_right > entity_left and
                sword_top < entity_bottom and sword_bottom > entity_top):
                # Trigger sinister effect
                rpg_state.sinister_triggered = True
                return

        # Check collision with breakable walls
        if not rpg_state.map:
            return
        walls_to_remove = []
        for r in range(rpg_state.map.height):
            for c in range(rpg_state.map.width):
                if rpg_state.map.tile_char(r, c) == "B":
                    wall_left = c * rpg_tile_size
                    wall_right = wall_left + rpg_tile_size
                    wall_top = r * rpg_tile_size
                    wall_bottom = wall_top + rpg_tile_size
                    
                    if (sword_left < wall_right and sword_right > wall_left and
                        sword_top < wall_bottom and sword_bottom > wall_top):
                        walls_to_remove.append((r, c))
                        
        for r, c in walls_to_remove:
            # Determine replacement tile based on surrounding tiles
            replacement_tile = "."
            # Check adjacent tiles for sand
            adjacent_tiles = [
                rpg_state.map.tile_char(r-1, c),
                rpg_state.map.tile_char(r+1, c),
                rpg_state.map.tile_char(r, c-1),
                rpg_state.map.tile_char(r, c+1)
            ]
            # If any adjacent tile is sand, make this sand too
            if "~" in adjacent_tiles:
                replacement_tile = "~"
            
            rpg_state.map.tiles[r][c] = replacement_tile
            if (r, c) in rpg_state.map.breakable_walls:
                rpg_state.map.breakable_walls.remove((r, c))
            rpg_state.map_changed = True
    
    def rpg_check_enemy_collision():
        """Check if player is touching any enemies (takes damage)."""
        if rpg_state.game_over:
            return
        
        # Player collision box
        offset = (rpg_tile_size - rpg_player_size) / 2.0
        player_left = rpg_state.player_px + offset
        player_right = rpg_state.player_px + offset + rpg_player_size
        player_top = rpg_state.player_py + offset
        player_bottom = rpg_state.player_py + offset + rpg_player_size
        
        # Check collision with each enemy
        for enemy in rpg_state.enemies:
            enemy_left = enemy.px
            enemy_right = enemy.px + rpg_tile_size
            enemy_top = enemy.py
            enemy_bottom = enemy.py + rpg_tile_size
            
            if (player_left < enemy_right and player_right > enemy_left and
                player_top < enemy_bottom and player_bottom > enemy_top):
                rpg_state.game_over = True
                return
    
    def rpg_collect_coin_if_any():
        """Check for coin collision using pixel-based bounding box overlap.
        This provides smoother coin collection than just tile-based checking."""
        if not rpg_state.map:
            return
        
        # Player collision box (centered within sprite, same as in rpg_blocked_at)
        offset = (rpg_tile_size - rpg_player_size) / 2.0
        player_left = rpg_state.player_px + offset
        player_right = rpg_state.player_px + offset + rpg_player_size
        player_top = rpg_state.player_py + offset
        player_bottom = rpg_state.player_py + offset + rpg_player_size
        
        # Check each coin for overlap
        coins_to_remove = []
        for r, c in rpg_state.map.coins:
            coin_left = c * rpg_tile_size
            coin_right = coin_left + rpg_tile_size
            coin_top = r * rpg_tile_size
            coin_bottom = coin_top + rpg_tile_size
            
            # Check if bounding boxes overlap
            if (player_left < coin_right and player_right > coin_left and
                player_top < coin_bottom and player_bottom > coin_top):
                coins_to_remove.append((r, c))
        
        # Remove collected coins and update score
        for coin in coins_to_remove:
            rpg_state.map.coins.remove(coin)
            rpg_state.score += 1
            rpg_state.map_changed = True
    
    def rpg_check_warp_tile():
        """Check if player is standing on a warp tile."""
        if not rpg_state.map or rpg_state.warping:
            return False
        
        # Player collision box center
        offset = (rpg_tile_size - rpg_player_size) / 2.0
        player_center_x = rpg_state.player_px + offset + rpg_player_size / 2
        player_center_y = rpg_state.player_py + offset + rpg_player_size / 2
        
        # Which tile is the player center on?
        tile_c = int(player_center_x // rpg_tile_size)
        tile_r = int(player_center_y // rpg_tile_size)
        
        # Check if this tile is a warp tile
        if (tile_r, tile_c) in rpg_state.map.warp_tiles:
            return True
        
        return False

    def rpg_tick():
        """Per-frame update for smooth movement and camera follow."""
        m = rpg_state.map
        if not m:
            return
        
        # Calculate time delta for frame-rate independent movement
        import time
        current_time = time.time()
        if rpg_state.last_tick_time is None:
            rpg_state.last_tick_time = current_time
            dt = 0.033  # assume 30fps for first frame
        else:
            dt = current_time - rpg_state.last_tick_time
            rpg_state.last_tick_time = current_time
            # Clamp dt to prevent huge jumps if game freezes briefly
            dt = min(dt, 0.1)
        
        # Poll current key state directly (works in Ren'Py 6.99)
        import pygame
        keys = pygame.key.get_pressed()
        
        # Check all movement keys (arrows and WASD)
        input_up = keys[pygame.K_UP] or keys[pygame.K_w]
        input_down = keys[pygame.K_DOWN] or keys[pygame.K_s]
        input_left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        input_right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        
        # Check attack keys (Z or Space)
        input_attack = keys[pygame.K_z] or keys[pygame.K_SPACE]

        dx = 0
        dy = 0
        if input_left:
            dx -= 1
        if input_right:
            dx += 1
        if input_up:
            dy -= 1
        if input_down:
            dy += 1
        
        # Update player facing direction based on movement input
        if dx != 0 or dy != 0:
            # Prioritize single direction for facing (no diagonals for attack)
            if dy != 0:
                rpg_state.player_facing = (0, dy)
            elif dx != 0:
                rpg_state.player_facing = (dx, 0)
        
        # Track if player moved this frame
        moved = False
        
        if dx != 0 or dy != 0:
            rpg_state.is_moving = True
            # Calculate movement distance based on time delta
            move_dist = rpg_state.speed_pps * dt
            
            # Normalize diagonal movement (sqrt(2) factor)
            if dx != 0 and dy != 0:
                move_dist *= 0.7071  # 1/sqrt(2)
            
            step_x = dx * move_dist
            step_y = dy * move_dist

            # Try X axis with sliding collision
            if step_x != 0:
                new_px = rpg_state.player_px + step_x
                rpg_state.player_px = rpg_move_to_contact(
                    rpg_state.player_px, new_px, rpg_state.player_py, 'x'
                )

            # Try Y axis with sliding collision (use updated X position)
            if step_y != 0:
                new_py = rpg_state.player_py + step_y
                rpg_state.player_py = rpg_move_to_contact(
                    rpg_state.player_py, new_py, rpg_state.player_px, 'y'
                )

            # Check if position actually changed
            if abs(rpg_state.player_px - rpg_state.prev_px) > 0.1 or abs(rpg_state.player_py - rpg_state.prev_py) > 0.1:
                moved = True
                rpg_state.prev_px = rpg_state.player_px
                rpg_state.prev_py = rpg_state.player_py

            # Collect coins and update camera
            rpg_collect_coin_if_any()
            rpg_update_camera()
            
            # Check for warp tile collision
            if rpg_check_warp_tile():
                rpg_state.warping = True
                return
        else:
            rpg_state.is_moving = False
        
        # Update attack cooldown
        if rpg_state.attack_cooldown > 0:
            rpg_state.attack_cooldown -= dt
        
        # Check for attack input (detect key press, not hold)
        attack_just_pressed = input_attack and not rpg_state.prev_attack_pressed
        rpg_state.prev_attack_pressed = input_attack
        
        if attack_just_pressed and rpg_state.attack_cooldown <= 0 and not rpg_state.attack_active:
            rpg_state.attack_active = True
            rpg_state.attack_timer = rpg_state.attack_duration
            rpg_state.attack_cooldown = rpg_state.attack_cooldown_time
        
        # Update attack timer
        if rpg_state.attack_active:
            rpg_state.attack_timer -= dt
            if rpg_state.attack_timer <= 0:
                rpg_state.attack_active = False
            # Check for hits during attack
            rpg_check_attack_hits()
        
        # Update enemies
        for enemy in rpg_state.enemies:
            enemy.update(dt)
        
        # Check win condition - all enemies defeated
        if len(rpg_state.enemies) == 0 and not rpg_state.game_won and not rpg_state.game_over:
            rpg_state.game_won = True
        
        # Check if player is touching enemies
        rpg_check_enemy_collision()
        
        # Update projectiles and remove dead ones
        for proj in rpg_state.projectiles[:]:
            proj.update(dt)
            if not proj.alive:
                rpg_state.projectiles.remove(proj)
        
        # Only force restart if something changed (huge performance gain)
        # Also restart if there are active enemies, projectiles, or attacks
        if moved or rpg_state.is_moving or rpg_state.enemies or rpg_state.projectiles or rpg_state.attack_active:
            renpy.restart_interaction()


# Overlay panel screen (CRT-like window)
screen rpg_screen():
    zorder 100
    modal True

    # Dim background to emphasize overlay panel
    add Solid("#00000080")

    frame:
        style "rpg_panel_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 8

            # Header
            hbox:
                spacing 12
                null width 30
                if rpg_state.map:
                    text "Score: [rpg_state.score]" size 16 color "#aaffaa"
                null width 20

            # Viewport
            if rpg_state.map:
                viewport:
                    xsize rpg_panel_width
                    ysize rpg_panel_height
                    draggable False
                    mousewheel False
                    xadjustment rpg_xadj
                    yadjustment rpg_yadj

                    fixed:
                        xminimum rpg_state.map.width * rpg_tile_size
                        yminimum rpg_state.map.height * rpg_tile_size

                        # Compute visible tile range for chunked rendering
                        $ sc, ec, sr, er = rpg_get_visible_tile_range(margin=2)

                        # Ground layer (batch render visible tiles)
                        for rr in range(sr, er + 1):
                            for cc in range(sc, ec + 1):
                                $ ch = rpg_state.map.tile_char(rr, cc)
                                $ tile_img = "rpg_sand" if ch == "~" else "rpg_grass"
                                add tile_img at rpg_pixel xpos cc * rpg_tile_size ypos rr * rpg_tile_size

                        # Wall layer (separate pass for z-ordering)
                        for rr in range(sr, er + 1):
                            for cc in range(sc, ec + 1):
                                if rpg_state.map.tile_char(rr, cc) == "#":
                                    add "rpg_wall" at rpg_pixel xpos cc * rpg_tile_size ypos rr * rpg_tile_size

                        # Breakable wall layer (separate pass for z-ordering)
                        for rr in range(sr, er + 1):
                            for cc in range(sc, ec + 1):
                                if (rr, cc) in rpg_state.map.breakable_walls:
                                    add "rpg_breakable_wall" at rpg_pixel xpos cc * rpg_tile_size ypos rr * rpg_tile_size

                        # Warp layer for secret zone (render warp tiles from set)
                        $ visible_warps = [(wr, wc) for (wr, wc) in rpg_state.map.warp_tiles if sr <= wr <= er and sc <= wc <= ec]
                        for wr, wc in visible_warps:
                            add "rpg_warp" at rpg_pixel xpos wc * rpg_tile_size ypos wr * rpg_tile_size

                        # Coins (only visible ones, pre-filtered)
                        $ visible_coins = [(cr, cc) for (cr, cc) in rpg_state.map.coins if sr <= cr <= er and sc <= cc <= ec]
                        for cr, cc in visible_coins:
                            add "rpg_coin" at rpg_pixel xpos cc * rpg_tile_size ypos cr * rpg_tile_size

                        # Enemies
                        for enemy in rpg_state.enemies:
                            add "rpg_enemy" at rpg_pixel xpos int(enemy.px) ypos int(enemy.py)
                        
                        # Mysterious entity (ourple)
                        if rpg_state.map.mysterious_entity:
                            $ mr, mc = rpg_state.map.mysterious_entity
                            add "rpg_ourple" at rpg_pixel xpos mc * rpg_tile_size ypos mr * rpg_tile_size
                        
                        # Projectiles
                        for proj in rpg_state.projectiles:
                            add "rpg_enemyprojectile" at rpg_pixel xpos int(proj.px) ypos int(proj.py)

                        # Player at pixel coordinates (convert to int for rendering)
                        add "rpg_player" at rpg_pixel xpos int(rpg_state.player_px) ypos int(rpg_state.player_py)
                        
                        # Sword attack rendering (spawns in facing direction)
                        if rpg_state.attack_active:
                            $ dx, dy = rpg_state.player_facing
                            
                            # Position sword so its center aligns with player's center
                            # Both sprites are 8x8 base (center at pixel 3.5), scaled by rpg_scale
                            # So we just offset by exactly one tile in the facing direction
                            if dx > 0:  # Right
                                $ sword_x = int(rpg_state.player_px + rpg_tile_size)
                                $ sword_y = int(rpg_state.player_py)
                                $ sword_rotation = 90
                            elif dx < 0:  # Left
                                $ sword_x = int(rpg_state.player_px - rpg_tile_size)
                                $ sword_y = int(rpg_state.player_py)
                                $ sword_rotation = 270
                            elif dy > 0:  # Down
                                $ sword_x = int(rpg_state.player_px)
                                $ sword_y = int(rpg_state.player_py + rpg_tile_size)
                                $ sword_rotation = 180
                            else:  # Up
                                $ sword_x = int(rpg_state.player_px)
                                $ sword_y = int(rpg_state.player_py - rpg_tile_size)
                                $ sword_rotation = 0
                            
                            add Transform("rpg_sword", rotate=sword_rotation, zoom=rpg_scale, nearest=True) xpos sword_x ypos sword_y

    # Per-frame tick for movement and camera follow (60fps for stable performance)
    timer 0.033 repeat True action Function(rpg_tick)
    
    # Check for game over and show game over screen
    if rpg_state.game_over:
        timer 0.1 action [Function(rpg_cleanup), Jump("rpg_game_over")]
    
    # Check for win and show win screen
    if rpg_state.game_won:
        timer 0.1 action [Function(rpg_cleanup), Jump("rpg_win")]
    
    # Check for warp trigger
    if rpg_state.warping:
        timer 0.1 action [Function(rpg_cleanup), Jump("rpg_warp_transition")]
    
    # Check for sinister trigger (attacking mysterious entity)
    if rpg_state.sinister_triggered:
        timer 0.1 action [Function(rpg_cleanup), Jump("rpg_sinister_event")]

    # ESC closes panel with cleanup
    key "K_ESCAPE" action [Function(rpg_cleanup), Return(None)]

define audio.gamemusic = "addons/Simple RPG Game/assets/game_music.ogg"
define audio.thgraze = "addons/Simple RPG Game/assets/th_graze.ogg"

# Game Over screen
screen rpg_game_over_screen():
    zorder 200
    modal True
    
    # Dim background
    add Solid("#000000C0")
    
    frame:
        style "rpg_panel_frame"
        xalign 0.5
        yalign 0.5
        xminimum 400
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "GAME OVER" size 32 color "#ff0000" bold True xalign 0.5
            
            text "Final Score: [rpg_state.score]" size 20 color "#ffffff" xalign 0.5
            
            null height 10
            
            vbox:
                spacing 10
                xalign 0.5
                
                textbutton "Retry" action Return("retry") xalign 0.5
                textbutton "Quit" action Return("quit") xalign 0.5

label rpg_game_over:
    stop music
    call screen rpg_game_over_screen
    
    if _return == "retry":
        jump rpg_retry
    else:
        # Quit - return to VN
        # If exiting from hidden map, restore background
        if rpg_state.map and "hidden.txt" in rpg_state.map.path:
            scene bg room_grayscale
        return

label rpg_retry:
    # Reload the current map
    $ rpg_load_map(rpg_state.map.path if rpg_state.map else rpg_default_map)
    # Only play music if not in hidden map
    if rpg_state.map and "hidden.txt" not in rpg_state.map.path:
        play music gamemusic fadein 0.5
    call screen rpg_screen
    return

# Win screen
screen rpg_win_screen():
    zorder 200
    modal True
    
    # Dim background
    add Solid("#000000C0")
    
    frame:
        style "rpg_panel_frame"
        xalign 0.5
        yalign 0.5
        xminimum 400
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "VICTORY!" size 32 color "#00ff00" bold True xalign 0.5
            
            text "All enemies defeated!" size 18 color "#ffffff" xalign 0.5
            
            text "Final Score: [rpg_state.score]" size 20 color "#ffffff" xalign 0.5
            
            null height 10
            
            vbox:
                spacing 10
                xalign 0.5
                
                # textbutton "Continue" action Return("quit") xalign 0.5 # we don't need this right now
                textbutton "Quit" action Return("quit") xalign 0.5

label rpg_win:
    stop music
    call screen rpg_win_screen
    
    if _return == "retry":
        jump rpg_retry
    else:
        # Quit - return to VN
        # If exiting from hidden map, restore background
        if rpg_state.map and "hidden.txt" in rpg_state.map.path:
            scene bg room_grayscale
        return

# RGB Flicker screen
default flicker_color = "#000"
screen rpg_rgb_flicker():
    zorder 200
    frame:
        style "rpg_panel_frame"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 8

            # Header (match RPG panel)
            hbox:
                spacing 12
                null width 30
                if rpg_state.map:
                    text "Score: [rpg_state.score]" size 16 color "#aaffaa"
                null width 20

            # Flicker viewport area sized like the game
            fixed:
                xmaximum rpg_panel_width
                ymaximum rpg_panel_height
                add Solid(flicker_color)

    # Update color rapidly (inside panel only)
    timer 1 repeat True action SetVariable("flicker_color", "#%02x%02x%02x" % (renpy.random.randint(0,255), renpy.random.randint(0,255), renpy.random.randint(0,255)))
    # Auto-advance after duration
    timer 5 action Return(None)

label rpg_flicker:
    $ flicker_color = "#000000"
    play sound thgraze
    call screen rpg_rgb_flicker
    return

# Warp transition - creepypasta element
label rpg_warp_transition:
    # Stop all music immediately for creepy effect
    stop music
    
    # Screen freeze effect - show static/glitch screen
    scene black
    $ flicker_color = "#000000"
    show screen rpg_rgb_flicker
    pause 3.0
    
    # Brief silence
    hide screen rpg_rgb_flicker
    scene black
    pause 3.0
    
    # Load the hidden map
    $ rpg_load_map("addons/Simple RPG Game/maps/hidden.txt")
    
    # No music in the hidden area for creepy atmosphere
    call screen rpg_screen
    return

# Sinister event - attacking the mysterious entity
label rpg_sinister_event:
    # Immediately go to full black - the ENTIRE game screen
    scene black
    hide screen rpg_screen
    
    # Play the stab sound effect and wait for it plus extra time
    play sound stab
    pause 8.0
    
    # Return to story after the sinister moment
    return

# Entrypoint label
label rpg_start(map_path=rpg_default_map):
    $ rpg_current_map_path = map_path  # Store for retry
    $ rpg_load_map(map_path)
    call screen rpg_screen
    return