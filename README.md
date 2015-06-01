# [ApiGen](https://github.com/ApiGen/ApiGen) support for Sublime Text 3

## Features
Currently The plugin allows click to run functunallity. Simply right click on any open file, or any filename in the sidebar to access the ApiGen options.


### Options
* **Generate** - Takes the clicked on file, and uses its path as a starting point to walk back to the filesystem root. The plugin checks each directory along the way for an *apigen.neon* file. It will halt it's walk if it finds a file, and call ApiGen passing the *apigen.neon* file path as the (--config) option.
* **Generate Freeform** - Works the same as the Generate option, but the user is prompted to provide additonal command line arguments.
* **Selfupdate** - Runs the ApiGen (selfupdate) option, to update the apigen.phar file to the latest revision.
* **Version** - Runs the ApiGen (-v) version option.
* **Freeform** - The usere is presented a prompt, and allowd to pass any arguments to ApiGen they wish.

## Instalation

### Requirements
* You must meet the requirements of, and have [ApiGen](https://github.com/ApiGen/ApiGen) instilled on your machine.


### Steps
1. Install the plugin using [Package Control](http://wbond.net/sublime_packages/package_control)
    1. From the main menu of Sublime Text go to **Preferences**
    2. Choose **Package Control**
    3. Choose **Install Package**
    4. Type **ApiGen**
2. Configure the plugin
    1. From the main menu of Sublime Text go to **Preferences**
    2. Choose **Package Settings**
    3. Choose **ApiGen**
    4. Choose **Settings - User**
    5. Set the setting to the approrite value for your machine.
        * **phpBin** - The location of the php executable on your machine.
        * **pharPath** - The location of apigen on your machine.
        * **configFileName** - The name of the config file to search for. The default is **apigen.neon**.
        * **additionalGenerateArgs** - Additonal command line arguments, to be appended to the end of the Generate command.


## Author
Sublime ApiGen was created & is maintained by [Daniel Sherman](https://github.com/dans98).


## License
Sublime ApiGen is open source software licensed under the [BSD 3-Clause license](http://opensource.org/licenses/BSD-3-Clause).

