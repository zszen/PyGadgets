DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/../..
echo $DIR
python3 ./ai/photo_scale_weifu2x/scale4x.py