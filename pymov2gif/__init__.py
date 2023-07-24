import os
import subprocess


def convert(file, resolution="800x600", framerate=10, output_file=None):
    """
    Convert *.mov files to *.gif format

    Args:
        file (str): Input movie file in *.mov format
        resolution (str): Resolution of the output *.gif file - default: 800x600
        framerate (int): Framerate of the output *.gif file - default: 10
        output_file (str/None): Filename of the output *.gif file - optional
    """
    file = os.path.abspath(os.path.expanduser(file))
    if output_file is None:
        output_file = os.path.splitext(os.path.basename(file))[0] + ".gif"
    command_options = (
        "ffmpeg -i "
        + file
        + " -s "
        + resolution
        + " -pix_fmt rgb24 -r "
        + str(framerate)
        + " -f gif - | gifsicle --optimize=3 --delay=3 > "
        + output_file
    )
    subprocess.check_output(command_options, shell=True, universal_newlines=True)
