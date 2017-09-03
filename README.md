# i3-Blurrer
This script can be added to the Blurlock script to capture and lock the wallpaper of a desktop running i3. It's faster than using the imagemagick method for some reason. It also allows the flexibility to add text to it. 


## Example
Perhaps you were writing code in your favourite IDE before locking your laptop

Or browsing Instagram

Or even writing this commit message


##Blurlock
By having these lines in a file that's called when the desktop is locked from the i3 config menu, it allows the screen to be locked, and the personal information be rendered,
```
/usr/bin/i3_blurrer.py
i3lock -i /tmp/screenshotblur.png
```
