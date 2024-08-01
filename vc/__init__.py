# coding: utf-8

import argparse
import os
import shlex


cmd_tmpl = 'ffmpeg -i {input} -c:v libx264 -tag:v avc1 -movflags faststart -crf 30 -preset superfast {output}'

__version__ = '0.1.0'


def compress_video(input, output):
    cmd = cmd_tmpl.format(input=shlex.quote(input), output=shlex.quote(output))
    print(f'Running: {cmd}')
    os.system(cmd)


def main():
    parser = argparse.ArgumentParser(
        prog='vc',
        description='Compression video using ffmpeg',
    )
    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s ' + __version__
    )
    parser.add_argument('inputs', metavar='<video path>', nargs='*')

    args = parser.parse_args()
    print(f'Got {len(args.inputs)} input videos')
    for input in args.inputs:
        (root, ext) = os.path.splitext(input)
        output = root + '-compressed.mp4'
        print(f'Compressing {input} to {output}...')
        compress_video(input, output)


if __name__ == '__main__':
    main()
