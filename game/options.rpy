##### ENGINE SETTINGS FOR YOUR MOD #####

# The formal name of the mod. Change the value of this to your mod's name
define config.name = "Doki Doki Modding Central Mod Template"

# Shows the name of the title in the bottom right corner of the main menu
# Set to True for templating purposes, but you can toggle it on or off as you see fit
define gui.show_name = True

# The version of the mod
define config.version = "0.1.0"

# The description of the mod. Typically not used, but you can set it to whatever you want
define gui.about = _("")

# What your mod's filename will be called when it is built
define build.name = "DDMCentral-Template"

# Toggles for different audio features.
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = audio.t1   # Set this to whatever you want the main menu music to be

# These settings control transitions between scenes
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)
define config.after_load_transition = None
define config.end_game_transition = Dissolve(.5)

# Window settings
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# Default text speed and auto-forward mode timing
default preferences.text_cps = 50          # Characters per second (bigger number = faster text)
default preferences.afm_time = 15          # Auto-forward mode wait time

# Default volume settings
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# Save directory - change to match your mod's name. This is located in AppData/Roaming/Ren'Py/ on Windows
# and in ~/.renpy/ on Linux.
define config.save_directory = "DDMCentral-Template"

# Window icon that appears in your taskbar
define config.window_icon = "gui/window_icon.png"

# Gameplay settings
define config.allow_skipping = True        # Allows player to skip unseen dialogue
define config.has_autosave = False         # Disables autosaving
define config.autosave_on_quit = False
define config.autosave_slots = 0

# Display Layers [defined order of foreground and background elements; do not edit unless you are familiar with ATL]
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# Performance settings
define config.image_cache_size = 64        # Number of images kept in active memory (higher = more memory usage)
define config.predict_statements = 50      # How many statements to look ahead
define config.rollback_enabled = config.developer  # Only enable rollback in dev mode

# Menu settings
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    # Removes persistent data from other Ren'Py games
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    
    # Disables gamepad support
    renpy.game.preferences.pad_enabled = False
    
    # Function to replace plain dashes with proper em dashes
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    # Function to handle game menu access
    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    # Forces integer scaling for better pixel art
    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

init python:
    # Build settings - defines how files are packaged when building your mod
    
    # Define the archives (packages) that will contain your mod's files
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    # Classify which files go into which archives
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")
    build.classify("game/**.gif", "images")
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")
    build.classify("game/story/**.rpyc", "scripts") # Custom partitioning for mod story files. Not required, but useful for larger mods
    build.classify("game/story/**.txt", "scripts")
    build.classify("game/story/**.chr", "scripts")
    build.classify("game/addons/**.rpyc", "scripts") # Custom partitioning for mod add-on files. Not required, but useful for larger mods
    build.classify("game/addons/**.txt", "scripts")
    build.classify("game/addons/**.chr", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")

    # Files that should be excluded from the build
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)           # Source files aren't included, only compiled .rpyc
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)

    # Documentation files to include
    build.documentation('*.html')
    build.documentation('*.txt')

    # Disables including old Ren'Py themes
    build.include_old_themes = False

##### Commented out as we have no use for this
# define build.itch_project = "teamsalvato/ddlc"

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc