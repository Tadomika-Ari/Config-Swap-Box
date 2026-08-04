# Config-Swap-Box

## Description

Config-Swap-Box is a repository for Config Swap, a Noctalia plugin. It contains community-shared configurations that are made available through the store page.

## Repository structure

Each configuration lives in its own folder under the config directory. A typical contribution includes:

- settings.toml: the main configuration file
- info.json: metadata used by the store
- preview.png: preview image shown in the store
- wallpaper.png: wallpaper asset associated with the configuration

## How to share your configuration

You can contribute to Config Swap by adding your own configuration and assets so others can discover and use them.

To do so:

1. Install and open Config-Swap.
2. Go to the Settings section and save your configuration with a custom name. The plugin will create a configuration folder containing settings.toml and info.json.
3. Prepare a preview image and a wallpaper image, then copy them into the generated folder using the exact filenames preview.png and wallpaper.png.
4. Update info.json with relevant metadata such as the author, description, and paths.
5. Add your configuration folder to this repository and open a pull request.
6. Wait for review, and once approved your configuration can be shared.

> Note: the preview and wallpaper files must use the exact required filenames so they can be detected correctly by the store.

