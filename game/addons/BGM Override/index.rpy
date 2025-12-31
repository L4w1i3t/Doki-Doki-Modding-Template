# BGM Override Button
# This addon adds a button in the top right corner (can be collapsed or expanded)
# to override the background music with any available track in the game.
# To add the button, just call this addon in your story script.

init 1 python:
    # BGM Override variables
    bgm_override_active = False
    bgm_override_expanded = False
    bgm_original_track = None
    
    # Available BGM tracks with display names
    bgm_tracks = [
        ("None (Stop Music)", None),
        ("Title Theme", audio.t1),
        ("Ohayou Sayori!", audio.t2),
        ("Ohayou Sayori! (Wobbly 4 Second Section)", audio.t2g),
        ("Ohayou Sayori (Rapid Glitch Noise)", audio.t2g2),
        ("Ohayou Sayori (Gradual Pitch Increase)", audio.t2g3),
        ("Main Theme", audio.t3),
        ("Main Theme (Off-Key)", audio.t3g),
        ("Main Theme (Start From Weird Note)", audio.t3g2),
        ("Main Theme (Revert + Wet)", audio.t3g3),
        ("Main Theme (???)", audio.t3m),
        ("Dreams of Love and Literature", audio.t4),
        ("Static + Error Noise", audio.t4g),
        ("Okay, Everyone!", audio.t5),
        ("Okay, Everyone! (???)", audio.t5b),
        ("Okay, Everyone! (Why Do We Need 3 Versions?)", audio.t5c),
        ("Play With Me", audio.t6),
        ("Play With Me (Bitcrushed)", audio.t6g),
        ("Play With Me (Y)", audio.t6s),
        ("Poem Panic!", audio.t7),
        ("Poem Panic! (First Melody Loop)", audio.t7a),
        ("Poem Panic! (Act 2)", audio.t7g),
        ("Daijoubu!", audio.t8),
        ("My Feelings", audio.t9),
        ("My Feelings (Harpsichord)", audio.t9g),
        ("My Confession", audio.t10),
        ("My Confession (Y)", audio.t10y),
        ("Sayo-nara", audio.td),
        ("Just Monika.", audio.m1),
        ("I Still Love You", audio.mend),
        ("Ghost Menu Theme", audio.ghostmenu),
        ("Your Reality", "bgm/credits.ogg")
        # Add custom tracks here
    ]
    
    def toggle_bgm_override():
        global bgm_override_active, bgm_original_track
        
        if bgm_override_active:
            # Disable override - restore original music if available
            bgm_override_active = False
            if bgm_original_track:
                renpy.music.play(bgm_original_track, channel="music", fadeout=1.0, fadein=1.0)
            else:
                # If there was no original music, stop the current music to restore silence
                renpy.music.stop(channel="music", fadeout=1.0)
            bgm_original_track = None
        else:
            # Enable override - store current track
            bgm_override_active = True
            bgm_original_track = renpy.music.get_playing(channel="music")
    
    def play_bgm_override(track):
        if track is None:
            renpy.music.stop(channel="music", fadeout=1.0)
        else:
            renpy.music.play(track, channel="music", fadeout=1.0, fadein=1.0)

# Resizing the disc button
init python:
    disc_idle = im.Scale("addons/BGM Override/assets/disc.png", 60, 60)
    disc_hover = im.Scale("addons/BGM Override/assets/disc_hover.png", 60, 60)

# Slow clockwise spinning transform for the disc button (80x80 scaled images)
transform disc_spin:
    subpixel True
    rotate 0
    linear 12.0 rotate -360
    repeat

# BGM Override screen
screen bgm_override():
    zorder 100
    
    # Collapsed button in top-right corner
    if not bgm_override_expanded:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10
            padding (10, 5)
            # Semi-transparent black frame
            background "#000000cc"
            
            # the actual icon for the button is addons/BGM Override/assets/disc.png
            imagebutton:
                idle disc_idle
                hover disc_hover
                at disc_spin
                action SetVariable("bgm_override_expanded", True)
    
    # Expanded panel
    else:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10
            padding (15, 10)
            background "#000000dd"
            
            vbox:
                spacing 5
                
                # Header with close button
                hbox:
                    spacing 10
                    text "BGM Override" size 16 color "#ffffff"
                    textbutton "X":
                        text_size 18
                        text_color "#ffffff"
                        text_hover_color "#ff6666"
                        action SetVariable("bgm_override_expanded", False)
                
                null height 5
                
                # Override toggle
                textbutton ("Disable Override" if bgm_override_active else "Enable Override"):
                    text_size 14
                    text_color ("#ffaaaa" if bgm_override_active else "#aaffaa")
                    text_hover_color "#ffffff"
                    action Function(toggle_bgm_override)
                
                if bgm_override_active:
                    null height 5
                    text "Select Track:" size 12 color "#cccccc"
                    
                    # Scrollable track list
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        xsize 200
                        ysize 300
                        
                        vbox:
                            spacing 3
                            
                            for track_name, track_audio in bgm_tracks:
                                textbutton track_name:
                                    text_size 12
                                    text_color "#ffffff"
                                    text_hover_color "#ffdddd"
                                    xfill True
                                    action Function(play_bgm_override, track_audio)

# Label to show the BGM override screen
label show_bgm_override:
    show screen bgm_override
    return

# Label to hide the BGM override screen  
label hide_bgm_override:
    hide screen bgm_override
    return