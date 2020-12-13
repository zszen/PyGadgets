DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/../..
echo $DIR
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 image/fold_img/foldimg.py
