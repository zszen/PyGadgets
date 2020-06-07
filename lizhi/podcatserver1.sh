# MYDIR=`pwd`
# echo $MYDIR
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# DIR="$( cd "$( dirname "$0"  )" && pwd  )"
# cd $pwd
podcats serve $DIR/podcast_server
