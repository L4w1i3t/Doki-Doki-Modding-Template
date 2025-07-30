##### GUI/Visual Settings #####

# Set init offset to -2 so these definitions happen before other init blocks
init offset = -2

init python:
    # Initialize the GUI with the game's resolution
    gui.init(1280, 720)

# Sound effects for UI interactions
define gui.hover_sound = "gui/sfx/hover.ogg"          # Sound when hovering over buttons
define gui.activate_sound = "gui/sfx/select.ogg"      # Sound when selecting buttons
define gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg"  # Glitched selection sound

# Color scheme for the interface
define gui.accent_color = '#ffffff'                   # Primary accent color
define gui.idle_color = '#aaaaaa'                     # Color for inactive elements
define gui.idle_small_color = '#333'                  # Color for small inactive elements
define gui.hover_color = '#cc6699'                    # Color when hovering over elements
define gui.selected_color = '#bb5588'                 # Color for selected elements
define gui.insensitive_color = '#aaaaaa7f'            # Color for disabled elements
define gui.muted_color = '#6666a3'                    # Color for background elements
define gui.hover_muted_color = '#9999c1'              # Hover color for background elements
define gui.text_color = '#ffffff'                     # Default text color
define gui.interface_text_color = '#ffffff'           # Color for interface text

# Fonts used throughout the game
define gui.default_font = "gui/font/Aller_Rg.ttf"     # Default dialogue font
define gui.name_font = "gui/font/RifficFree-Bold.ttf" # Font for character names
define gui.interface_font = "gui/font/Aller_Rg.ttf"   # Font for UI elements

# Text sizes for different parts of the interface
define gui.text_size = 24                             # Size of dialogue text
define gui.name_text_size = 24                        # Size of character names
define gui.interface_text_size = 24                   # Size of interface text
define gui.label_text_size = 28                       # Size of section labels
define gui.notify_text_size = 16                      # Size of notification text
define gui.title_text_size = 38                       # Size of title text

# Background images for menus
define gui.main_menu_background = "menu_bg"           # Main menu background
define gui.game_menu_background = "game_menu_bg"      # Game menu background

# Show game title in main menu
define gui.show_name = False

# Text box settings
define gui.textbox_height = 182                       # Height of dialogue box
define gui.textbox_yalign = 0.99                      # Vertical position of dialogue box

# Name box position and size
define gui.name_xpos = 350                            # Horizontal position of name box
define gui.name_ypos = -3                             # Vertical position of name box
define gui.name_xalign = 0.5                          # Horizontal alignment of name text
define gui.namebox_width = 168                        # Width of name box
define gui.namebox_height = 39                        # Height of name box
define gui.namebox_borders = Borders(5, 5, 5, 2)      # Border size around name box
define gui.namebox_tile = False                       # Whether to tile the namebox background

# Dialogue text position and size
define gui.text_xpos = 268                            # Horizontal position of dialogue text
define gui.text_ypos = 62                             # Vertical position of dialogue text
define gui.text_width = 744                           # Width of dialogue text area
define gui.text_xalign = 0.0                          # Horizontal alignment of dialogue text

# Button appearance settings
define gui.button_width = None                        # Default button width (None = auto)
define gui.button_height = 36                         # Default button height
define gui.button_borders = Borders(4, 4, 4, 4)       # Border size around buttons
define gui.button_tile = False                        # Whether to tile button backgrounds
define gui.button_text_font = gui.interface_font      # Button text font
define gui.button_text_size = gui.interface_text_size # Button text size
define gui.button_text_idle_color = gui.idle_color    # Button text color when inactive
define gui.button_text_hover_color = gui.hover_color  # Button text color when hovered
define gui.button_text_selected_color = gui.selected_color  # Button text color when selected
define gui.button_text_insensitive_color = gui.insensitive_color  # Button text color when disabled
define gui.button_text_xalign = 0.0                   # Button text horizontal alignment

# Radio and check buttons
define gui.radio_button_borders = Borders(28, 4, 4, 4)  # Radio button borders
define gui.check_button_borders = Borders(28, 4, 4, 4)  # Checkbox borders

# Confirm button text alignment
define gui.confirm_button_text_xalign = 0.5           # Center confirm button text

# Page navigation buttons
define gui.page_button_borders = Borders(10, 4, 10, 4)  # Page button borders

# Quick menu buttons (bottom of screen during gameplay)
define gui.quick_button_text_size = 14                # Quick button text size
define gui.quick_button_text_idle_color = "#522"      # Quick button inactive color
define gui.quick_button_text_hover_color = "#fcc"     # Quick button hover color
define gui.quick_button_text_selected_color = gui.accent_color  # Quick button selected color
define gui.quick_button_text_insensitive_color = "#a66"  # Quick button disabled color

# Choice buttons (dialogue choices)
define gui.choice_button_width = 420                  # Choice button width
define gui.choice_button_height = None                # Choice button height
define gui.choice_button_tile = False                 # Whether to tile choice backgrounds
define gui.choice_button_borders = Borders(100, 5, 100, 5)  # Choice button borders
define gui.choice_button_text_font = gui.default_font  # Choice text font
define gui.choice_button_text_size = gui.text_size     # Choice text size
define gui.choice_button_text_xalign = 0.5             # Choice text alignment
define gui.choice_button_text_idle_color = "#000"      # Choice text color when inactive
define gui.choice_button_text_hover_color = "#fa9"     # Choice text color when hovered

# Save/load slot buttons
define gui.slot_button_width = 276                     # Save slot width
define gui.slot_button_height = 206                    # Save slot height
define gui.slot_button_borders = Borders(10, 10, 10, 10)  # Save slot borders
define gui.slot_button_text_size = 14                  # Save slot text size
define gui.slot_button_text_xalign = 0.5               # Save slot text alignment
define gui.slot_button_text_idle_color = gui.idle_small_color  # Save slot inactive color
define gui.slot_button_text_hover_color = gui.hover_color      # Save slot hover color

# Save thumbnails
define config.thumbnail_width = 256                    # Save thumbnail width
define config.thumbnail_height = 144                   # Save thumbnail height

# Save/load screen grid layout
define gui.file_slot_cols = 3                          # Number of save slots per row
define gui.file_slot_rows = 2                          # Number of rows of save slots

# Positioning
define gui.navigation_xpos = 80                        # Position of navigation buttons
define gui.skip_ypos = 10                              # Position of skip indicator
define gui.notify_ypos = 45                            # Position of notifications

# Spacing
define gui.choice_spacing = 22                         # Spacing between choice buttons
define gui.navigation_spacing = 6                      # Spacing between navigation buttons
define gui.pref_spacing = 10                           # Spacing in preferences screens
define gui.pref_button_spacing = 0                     # Spacing between preference buttons
define gui.page_spacing = 0                            # Spacing between page buttons
define gui.slot_spacing = 10                           # Spacing between save slots

# Frames (borders around UI elements)
define gui.frame_borders = Borders(4, 4, 4, 4)         # Standard frame borders
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)  # Confirm dialog borders
define gui.skip_frame_borders = Borders(16, 5, 50, 5)  # Skip indicator borders
define gui.notify_frame_borders = Borders(16, 5, 40, 5)  # Notification borders
define gui.frame_tile = False                          # Whether to tile frame backgrounds

# Bars, scrollbars, and sliders
define gui.bar_size = 36                               # Size of bars (like health)
define gui.scrollbar_size = 12                         # Size of scrollbars
define gui.slider_size = 30                            # Size of sliders
define gui.bar_tile = False                            # Whether to tile bar images
define gui.scrollbar_tile = False                      # Whether to tile scrollbar images
define gui.slider_tile = False                         # Whether to tile slider images
define gui.bar_borders = Borders(4, 4, 4, 4)           # Bar borders
define gui.scrollbar_borders = Borders(4, 4, 4, 4)     # Scrollbar borders
define gui.slider_borders = Borders(4, 4, 4, 4)        # Slider borders
define gui.vbar_borders = Borders(4, 4, 4, 4)          # Vertical bar borders
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)    # Vertical scrollbar borders
define gui.vslider_borders = Borders(4, 4, 4, 4)       # Vertical slider borders
define gui.unscrollable = "hide"                       # What to do when scrolling not needed

# History screen settings
define config.history_length = 50                      # Number of dialogue lines to keep
define gui.history_height = None                       # Height of history entries
define gui.history_name_xpos = 150                     # Name horizontal position in history
define gui.history_name_ypos = 0                       # Name vertical position in history
define gui.history_name_width = 150                    # Name width in history
define gui.history_name_xalign = 1.0                   # Name horizontal alignment in history
define gui.history_text_xpos = 170                     # Text horizontal position in history
define gui.history_text_ypos = 5                       # Text vertical position in history
define gui.history_text_width = 740                    # Text width in history
define gui.history_text_xalign = 0.0                   # Text horizontal alignment in history

# NVL mode settings (full-screen text mode)
define gui.nvl_borders = Borders(0, 10, 0, 20)         # NVL screen borders
define gui.nvl_height = 115                            # Height of NVL entries
define gui.nvl_spacing = 10                            # Spacing between NVL entries
define gui.nvl_name_xpos = 430                         # NVL name horizontal position
define gui.nvl_name_ypos = 0                           # NVL name vertical position
define gui.nvl_name_width = 150                        # NVL name width
define gui.nvl_name_xalign = 1.0                       # NVL name horizontal alignment
define gui.nvl_text_xpos = 450                         # NVL text horizontal position
define gui.nvl_text_ypos = 8                           # NVL text vertical position
define gui.nvl_text_width = 590                        # NVL text width
define gui.nvl_text_xalign = 0.0                       # NVL text horizontal alignment
define gui.nvl_thought_xpos = 240                      # NVL thought horizontal position
define gui.nvl_thought_ypos = 0                        # NVL thought vertical position
define gui.nvl_thought_width = 780                     # NVL thought width
define gui.nvl_thought_xalign = 0.0                    # NVL thought horizontal alignment
define gui.nvl_button_xpos = 450                       # NVL button horizontal position
define gui.nvl_button_xalign = 0.0                     # NVL button horizontal alignment

# Mobile/small screen adaptations
init python:

    # Touch-based devices get wider button borders for easier tapping
    if renpy.variant("touch"):
        gui.quick_button_borders = Borders(60, 14, 60, 0)

    # Small screens get larger text and adjusted UI elements
    if renpy.variant("small"):
        
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 36
        gui.button_text_size = 34
        gui.label_text_size = 36
        
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100
        
        gui.choice_button_width = 1240
        
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        
        gui.history_height = 190
        gui.history_text_width = 690
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        gui.nvl_height = 170
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
        
        gui.quick_button_text_size = 20