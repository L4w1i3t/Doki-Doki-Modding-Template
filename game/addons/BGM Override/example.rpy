# Example usage of BGM Override addon
# This file shows how to use the BGM Override functionality in your mod

# Example label that shows how to enable the BGM override button
label bgm_override_example:
    scene bg club_day
    
    "This is an example of using the BGM Override addon."
    
    # Show the BGM override screen
    call show_bgm_override

    "The BGM override button should now appear in the top-right corner."
    "You can now click the button in the top-right corner to access the BGM override panel."
    "From there, you can:"
    "- Enable/disable BGM override"
    "- Select any available background music track"
    "- Stop the music entirely"
    
    "When you disable the override, it will restore the original music that was playing."
    
    menu:
        "Try it out! What would you like to do?"
        
        "Continue with BGM override active":
            "Great! The BGM override will remain available."
            "You can use it anytime during your playthrough."
        
        "Hide the BGM override panel":
            call hide_bgm_override
            "The BGM override panel has been hidden."
            "You can show it again by calling 'show_bgm_override' in your script."
    
    "That's how you use the BGM Override addon!"
    return
