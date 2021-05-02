# DiaScanner
This is a small python App using opencv that will preview the camera-feed, gives you the option to manipulate the image (e.g. rotate) and allows you to store images.

## Usage
~~~ bash
    pip3 install -r requiremetns.txt
    python3 main.py
~~~
Now you can define the basename for your images and a suffix if you wand to. The scheme is:
<code>{base_name}{incrementing_number}{suffix}.png</code>
Button mapping:
- ___esc___ : exit the app
- ___l___ : rotate left
- ___r___ : rotate right
- ___c / space___ : capture an image

## TODO
- add option to transform negatives into positives
- add option to remove borders
- maybe add option to improve image quality (e.g. brightness, saturation, ...)
