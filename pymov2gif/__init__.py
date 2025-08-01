import os
import subprocess
from typing import Optional
from . import _version

__version__ = _version.__version__


def convert(
    file: str,
    resolution: str = "800x600",
    framerate: int = 10,
    output_file: Optional[str] = None,
) -> None:
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
