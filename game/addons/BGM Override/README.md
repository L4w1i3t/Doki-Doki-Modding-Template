# BGM Override Addon

This addon adds a collapsible BGM (Background Music) override button in the top-right corner of the screen that allows players to override the current background music with any available track in the game.

## Features

- **Collapsible Interface**: Click the button to expand/collapse the panel
- **Music Override**: Enable override mode to change the background music
- **Track Selection**: Choose from all available DDLC music tracks (OR custom tracks if you add them)
- **Original Music Restoration**: Automatically restores the original music when override is disabled
- **Stop Music Option**: Option to completely stop the background music

## Usage

### Basic Usage

To show the BGM override button, call this label in your script:

```renpy
call show_bgm_override
```

To hide the BGM override button:

```renpy
call hide_bgm_override
```

### Example Implementation

```renpy
label start:
    scene bg club_day
    
    # Show the BGM override button
    call show_bgm_override
    
    "The BGM override button is now available!"
    "Click the button in the top-right corner to access it."

    # Your story continues here...
    return
```

## Available Tracks

The addon includes all standard DDLC music tracks. You can also add custom tracks by modifying the `bgm_tracks` list in `index.rpy`. Each entry should be a tuple of `(display_name, audio_definition)`.

## How It Works

1. **Collapsed State**: Shows a small button with a capital "O" in the top-right corner
2. **Expanded State**: Shows a panel with override toggle and track selection
3. **Override Mode**: When enabled, stores the current track and allows music changes
4. **Restoration**: When disabled, restores the original music that was playing

## Technical Details

- Uses Ren'Py screen system for the UI
- Stores original track information for restoration
- Includes smooth fade transitions between tracks
- Zorder 100 ensures the button appears above other UI elements

## Customization

You can modify the `bgm_tracks` list in `index.rpy` to add custom music tracks or remove unwanted ones. Each entry should be a tuple of `(display_name, audio_definition)`.

## Integration

This addon is designed to work seamlessly with existing DDLC mods and doesn't interfere with normal music playback when not in override mode, nor does it require any integration via modifying the source files.
