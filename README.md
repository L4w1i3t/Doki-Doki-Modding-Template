# Doki Doki Literature Club Modding Template

A comprehensive modding template for creating Doki Doki Literature Club mods using Ren'Py. This template provides all the necessary files, configurations, and structure to create professional DDLC mods with minimal setup.

## Table of Contents

- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Creating Your Mod](#creating-your-mod)
- [Asset Management](#asset-management)
- [Addon Creation and Management](#addon-creation-and-management)
- [Development Tools](#development-tools)
- [Building & Distribution](#building--distribution)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Quick Start

### Prerequisites

- **Ren'Py SDK** (Template works with ALL versions of Ren'Py from 6.99 onwards)
- Basic knowledge of Ren'Py scripting language
- Text editor (VS Code recommended with Ren'Py Language extension)
- A fresh copy of Doki Doki Literature Club!

### Setup

1. **Download the latest release of the template**
   - Visit the [GitHub releases page](https://github.com/L4w1i3t/Doki-Doki-Modding-Template/releases)
   - Download the ZIP file for the latest release
   - Extract the contents to a folder of your choice
   - Download and extract a fresh copy of Doki Doki Literature Club! (DDLC) to a separate folder
   - Transfer the following files from the DDLC folder to the template /game folder:
     - `images.rpa`
     - `fonts.rpa`
     - `audio.rpa`
       - Note: These aren't *technically* necessary to operate the template nor have a fully playable mod, but they ARE required to follow the Team Salvato IP guidelines for independent fangame usage (no amount of DRM can change that).

2. **Open with Ren'Py Launcher**
   - Launch Ren'Py
    - Note: Ren'Py 6 and 7 use Python 2.7, while Ren'Py 8 uses Python 3, meaning there is slight variation in syntax and available features. Additionally, Ren'Py 6 is as close to vanilla DDLC whereas Ren'Py 7 and 8 have more features and allow for more complex scripting.
   - Click "Projects"
   - Navigate to the template folder
   - Select the project
     - Tip: Putting the template in the same folder as the rest of your Ren'Py projects can help keep things organized, especially if you plan to create multiple mods.

3. **Configure your mod**
   - Edit `game/options.rpy` to set your mod's name, version, and settings
   - Replace placeholder content in `game/script.rpy`
   - Add your story files to `game/story/`

4. **Test your mod**
   - Click "Launch Project" in Ren'Py Launcher
   - Or run `runcode.bat` to open in VS Code

## Configuration

### Basic Settings (`game/options.rpy`)

```python
# Essential settings to customize for your mod
define config.name = "Your Mod Name Here"           # Display name
define config.version = "1.0.0"                     # Version number
define build.name = "YourModName"                    # Build filename
define config.save_directory = "YourModName"        # Save folder name
```

### Character Definitions

The template includes pre-configured character definitions in `game/definitions.rpy`:

```python
# Characters are already defined:
# m = Monika, s = Sayori, n = Natsuki, y = Yuri, mc = Main Character
```

### Audio Configuration

Audio files are defined in `game/definitions.rpy`. The template includes:
- Background music tracks (`audio.t1`, `audio.t2`, etc.)
- Sound effects (`audio.page_turn`, `audio.fall`, etc.)
- Main menu music setting in `options.rpy` and `screens.rpy`
  - Note: When changing the main menu music in one file, be sure to change it in the other as well.

## Creating Your Mod

### 1. Story Structure

Create your story files in the `game/story/` folder:

```python
# game/story/chapter1.rpy
label chapter1:
    scene bg residential_day
    show sayori 1a at t11
    s "Hello, [player]!"
    "This is how you write dialogue."
    return
```

### 2. Main Script Entry

Edit `game/script.rpy` to call your story:

```python
label start:
    # Template setup code (keep this)
    $ quick_menu = True
    # ... initialization code ...
    
    # Replace the template story call with your own
    if persistent.playthrough == 0:
        call chapter1 from _call_chapter1  # Your story here
```

### 3. Character Expressions

Use the pre-defined character poses and expressions:

```python
show sayori 1a    # Pose 1, expression a (happy)
show sayori 1b    # Pose 1, expression b (sad)
show monika 2a    # Different pose and expression
```

### 4. Backgrounds and Music

```python
scene bg club_day          # Show club room background
play music t3              # Play track 3
stop music fadeout 1.0     # Stop music with fadeout
```

## Asset Management

### Adding New Assets

1. **Images**: Place in `game/mod_assets/images/`
2. **Music**: Place in `game/mod_assets/bgm/`
3. **Sound Effects**: Place in `game/mod_assets/sfx/`
4. **Fonts**: Place in `game/mod_assets/fonts/`

### Asset Definition

Define new assets in `game/definitions.rpy`:

```python
# New background
image bg my_background = "mod_assets/images/my_bg.png"

# New music track
define audio.my_song = "mod_assets/bgm/my_song.ogg"

# New character sprite
image mychar happy = "mod_assets/images/mychar_happy.png"
```

## Addon Creation and Management

This template's selling point is its segregation between vanilla source files, mod asset files, and additional content that can be added via plug-and-play means. This allows you to create addons that can be easily integrated into the template without modifying the core files--just function calls are necessary (*1 whole extra line of code!*) Examples of addons include but are not limited to:

- **UI and menu additions**: Achievement systems, galleries, gender selection, etc.
- **Phone and social media interfaces**: Text threads, notifications, status updates, etc.
- **Jukebox and music players**: Custom music players, playlists, etc.
- **Overrides**: Physics, character behaviors, and other gameplay mechanics that can be toggled on or off.
- **"Mods within mods"**: Gameplay loops, interactive elements, sub-engines, etc.
- **Custom Python scripts**: For advanced features or integrations.

### Creating an Addon

You can either create an addon using Ren'Py language, Python, or a combination of both. It will also provide the option of JSON knowledge. The template provides a basic structure for creating addons:

1. **Create a new folder** in `game/addons/` with your addon name (e.g., `game/addons/My Addon/`)
2. **Add your addon files**:
   - Create a main script file (something like `index.rpy`)
   - Add any additional assets in `game/addons/My Addon/assets/` (I know there's a lot of nesting here, but bear with me)
3. **Create `addon.json`** in your addon folder to define metadata (OPTIONAL but recommended):

```json
{
    "name": "My Addon",
    "version": "1.0.0",
    "description": "A cool addon for my mod",
    "author": "Your Name",
    "dependencies": []
}
```

4. **Create your addon in any way you like**
    - 4.5. **Best Practice: Wrap the entirety of your addon logic in a Ren'Py label** to allow easy integration.

5. **Make a test file or test script** to ensure your addon works as expected. If you followed step 4.5, you can call your addon label from the main script:

```python
label test_my_addon:
    # Call your addon label here
    call my_addon_label
    return
```

6. **When you're satisfied, use or share it!** We here at ModCen love to see creativity and what modders can come up with.
    - If you so desire, you can submit your addon to the ModCen website for preservation and easy access by other modders. Just make sure to follow the submission guidelines.
        - URL: https://ddmc.site/pages/template/addons.html

## Development Tools

### Debug Mode

The template includes debugging tools in `game/dev.rpy`:

```python
# Enable during development (disable for release)
define config.developer = True      # Enables console and developer features
define config.autoreload = True     # Auto-reloads on file changes
```

- Note: When building your mod for release, set `config.developer = False` to disable these features. ALWAYS disable developer mode before building your mod to avoid including debug features in the final release (you have no idea how annoying it can get).

### Console Commands

With developer mode enabled, press `Shift+O` to open console:

```python
# Jump to specific labels
$ renpy.call("your_label_name")

# Check variables
$ persistent.playthrough

# Modify variables
$ chapter = 2
```

### Quick Launch

Use `runcode.bat` to quickly open the project in VS Code.

## Building & Distribution

### Building Your Mod

1. **Disable Development Features**:
   - Set `config.developer = False` in `game/dev.rpy`
   - Remove or comment out `config.autoreload = True`

2. **Build via Ren'Py Launcher**:
   - Select your project
   - Click "Build Distributions"
   - Choose "Mod Export (All Platforms)" option, as it includes all necessary files for Windows, macOS, and Linux
   - Wait for build completion
   - Congrats! Your mod is now ready for distribution.

3. **Output Location**:
   - Built files appear in project root folder
   - Distribute the `.zip` file using a file-sharing service or your preferred method.

### Build Configuration

The template includes optimized build settings in `game/options.rpy` under "Mod Export":

```python
# Files are automatically categorized for distribution
# Mod files go to "mod" archive
# Excludes source files (.rpy) and other development files
```

## Best Practices

### Code Organization

1. **Separate story files**: Use multiple `.rpy` files in `game/story/` to keep track of different chapters or sections
   - Example: `chapter1.rpy`, `chapter2.rpy`, etc.
2. **Consistent naming**: Use clear, descriptive names for labels and variables. You'll save future you a lot of headaches.
   - Example: `label chapter1_start` instead of `label c1`
3. **Comment your code**: Explain complex logic and story branches

### Performance

1. **Image optimization**: Compress images appropriately. Generally, PNG is best for sprites and backgrounds, while JPEG is suitable for photos.
   - Use tools like TinyPNG or ImageOptim to reduce file sizes without losing quality.
2. **Audio formats**: Use OGG for music and sound effects. It is the most quality-efficient format for Ren'Py.
3. **Preload important assets**: Use `image` statements for frequently used sprites

### DDLC Authenticity

1. **Character consistency**: Keep characters true to their personalities
2. **Art style**: Match the original game's visual style
3. **UI consistency**: Use the existing interface elements
4. **Content warnings**: Include appropriate warnings for mature content

### Version Control

```bash
# Initialize git repository
git init

# Exclude cache and save files
echo "game/cache/" >> .gitignore
echo "game/saves/" >> .gitignore
echo "*.rpyc" >> .gitignore
echo "*.rpyb" >> .gitignore
```

## Troubleshooting

### Common Issues

**"Story label not found"**
- Ensure you've created the story file and defined the label
- Check spelling and case sensitivity
- Verify the file is in the correct location

**Images not displaying**
- Check file paths and extensions
- Ensure images are properly defined in `definitions.rpy`
- Verify image dimensions and format

**Audio not playing**
- Confirm audio files are in correct format (OGG/WAV, etc.)
- Check audio definitions in `definitions.rpy`
- Verify file paths are correct

**Build errors**
- Ensure that developer mode is disabled in your build (PLEASE.)
- Check for syntax errors in `.rpy` files (these are more common than you think)
- Ensure all referenced files exist

### Performance Issues

- Reduce image file sizes
- Limit simultaneous animations
- Use `$ renpy.free_memory()` after intensive scenes
- Consider using image compression

### Compatibility

- Test on different screen resolutions
- Verify mod works with various Ren'Py versions
- Check save/load functionality
- Test skip and rollback features

## File Reference

### Key Files to Customize

| File | Purpose | Priority |
|------|---------|----------|
| `game/options.rpy` | Basic mod configuration | **High** |
| `game/script.rpy` | Main entry point | **High** |
| `game/story/*.rpy` | Your story content | **High** |
| `game/definitions.rpy` | Asset definitions | Medium |
| `game/gui.rpy` | UI customization | Variable |
| `game/dev.rpy` | Development tools | Low (until build) |
| `game/mod_assets/*` | Custom assets (optional) | Variable |

### Files and Folders to Leave Unchanged

- `game/screens.rpy` (unless doing advanced UI work)
- `game/transforms.rpy` (unless adding custom animations)
- `vanilla/` folder (reference materials only)
- `characters/` folder (original .chr files. Only modify if you know what you're doing or want to add new .chr files)

## Advanced Features

### Custom Minigames

Create interactive elements in your story or as standalone files to be called to:

```python
# Example: Simple choice-based minigame
label minigame:
    $ points = 0
    "Let's play a game!"
    
    menu:
        "Choice A":
            $ points += 1
        "Choice B":
            $ points += 2
    
    if points >= 2:
        "You won!"
    else:
        "GG EZ I WIN + I'M JUST BETTER"
    return
```

### Persistent Data

Save data across playthroughs:

```python
# Define persistent variables
default persistent.special_unlock = False

# Use in story
if persistent.special_unlock:
    "This ain't your first rodeo, is it?"
else:
    $ persistent.special_unlock = True
    "This is your first time playing."
```

### Multiple Endings

Implement branching storylines:

```python
# Track player choices
default ending_points = 0

# In story
menu:
    "Be kind":
        $ ending_points += 1
    "Be harsh":
        $ ending_points -= 1

# At story end
if ending_points >= 5:
    call good_ending
elif ending_points <= -5:
    call bad_ending
else:
    call neutral_ending
```

### Extracting .rpa Files

To extract `.rpa` files (Ren'Py archive files), you can use RPA Extract by iwanMods: https://iwanplays.itch.io/rpaex. Just drag a `.rpa` file onto the executable, and it will extract the contents to a folder with the same name as the `.rpa` file.

### Decompiling .rpyc Files

To decompile `.rpyc` files (compiled Ren'Py scripts), you can use unrpyc by CensoredUsername: https://github.com/CensoredUsername/unrpyc. Place .unrpyc in the same folder as your Ren'Py `/game` folder, run the project, and it will decompile the `.rpyc` files into `.rpy` files for easier editing.

- This is extremely useful for compiled projects when there are only `.rpyc` files available, as it allows you to view and edit the original script content.

## Contributing

This template is open-source and welcomes contributions from the community. Whether you're a seasoned modder or just starting, your input can help improve this template for everyone!

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Test thoroughly
5. Submit a pull request

### Areas for Contribution

- Additional example stories
- UI improvements
- Performance optimizations
- Documentation enhancements
- Addons
- Bug fixes

## License

This template is provided under the same terms as the original DDLC game. Please respect Team Salvato's IP guidelines when creating and distributing mods.

## Support

- **Issues**: Report bugs via GitHub Issues
- **Documentation**: Check the wiki for detailed guides
- **Community**: Join DDLC modding communities for support

## Credits

- **Original Game**: Team Salvato
- **Template**: DDMCentral Community
- **Engine**: Ren'Py Visual Novel Engine

---

**Happy Modding!**

Remember: Always respect the original game's content guidelines and create mods that honor the spirit of Doki Doki Literature Club!