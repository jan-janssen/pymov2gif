"""
Convert *.mov files to *.gif format
"""
import argparse
from pymov2gif import convert


def command_line_parser():
    """
    Main function primarly used for the command line interface
    """
    parser = argparse.ArgumentParser(prog="pymov2gif")
    parser.add_argument(
        "file",
        help="Video file to be converted - in *.mov format.",
    )
    parser.add_argument(
        "-r",
        "--resolution",
        help="Resolution of the output *.gif file - default: 800x600",
    )
    parser.add_argument(
        "-f",
        "--framerate",
        help="Framerate of the output *.gif file - default: 10",
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        help="Name of the output file in *.gif format - optional",
    )
    args = parser.parse_args()
    if args.output_filename:
        output_file = args.output_filename
    else:
        output_file = None
    if args.resolution and args.framerate:
        convert(
            file=args.file,
            resolution=args.resolution,
            framerate=args.framerate,
            output_file=output_file,
        )
    elif args.resolution:
        convert(file=args.file, resolution=args.resolution, output_file=output_file)
    elif args.framerate:
        convert(file=args.file, framerate=args.framerate, output_file=output_file)
    elif args.file:
        convert(file=args.file, output_file=output_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    command_line_parser()
