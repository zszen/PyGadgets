DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/../..
echo $DIR
echo please input image
read image
echo $image
python3 ./ocr/prices/prices_detect.py -i "$image"