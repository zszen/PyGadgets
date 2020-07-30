import os, re
import cv2
import ffmpeg

root = os.path.dirname(__file__)+'/'

def get_video_info(input_path):
    try:
        probe = ffmpeg.probe(input_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)
        return video_stream
    except ffmpeg.Error as err:
        print(str(err.stderr, encoding='utf8'))
        sys.exit(1)

def split_video(input_path):
    # input = ffmpeg.input(input_path)
    split = ffmpeg.input('in.mp4').filter_multi_output('split') 
    split0 = split.stream(0) 
    split1 = split[1] 
    ffmpeg.concat(split0, split1).output('out.mp4').run()


if __name__ == "__main__": 
    video_info = get_video_info(root+'./in/in.mp4')
    print(video_info['duration'])