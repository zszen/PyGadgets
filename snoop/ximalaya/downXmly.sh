#!/bin/bash

ID=$1
TOTAL=0
TEMPTXT=temp.txt
if [[ $ID == "" ]]; then
  echo 'Please input the number in the url !'
  echo 'for example:'
  echo 'if download https://www.ximalaya.com/xiqu/14988280/'
  echo 'run ./downXmly.sh 14988280'
  exit 1
fi

if ! [ -x "$(command -v jq)" ]; then
  echo 'Error: jq is not installed. please install jq by apt install jq' >&2
  exit 1
fi

function getSign() {
  #md5(ximalaya-服务器时间戳) +(100以内的随机数) + 服务器时间戳 + (100以内的随机数) + 现在的时间戳
  serverTime=`curl -s https://www.ximalaya.com/revision/time`
  curTime=`date +%s%3N`
  md5=`echo -n "himalaya-$serverTime" | md5sum | cut -d" " -f1`
  sign=$md5"("$[$RANDOM%100]")"$serverTime"("$[$RANDOM%100]")"$curTime
  echo $sign
}

function down() {
  sign=`getSign`
  local dir=$1
  local title=$2
  local trackId=$3
  local result=`curl -H"xm-sign:$sign" -s https://www.ximalaya.com/revision/play/tracks?trackIds=$trackId`
  local src=`echo $result | jq '.data.tracksForAudioPlay[].src' | awk -F'"' '{print $2}'`
  wget --header="xm-sign:$sign" -q -O$dir/$title.m4a $src &
  wait
  echo "$title done" >> down.log
}

function parsingMainPage() {
  local temp=`curl -s https://www.ximalaya.com/xiqu/$ID/`
  local max=`echo $temp | awk -F"max=" '{print $2}' | awk '{print $1}' | awk -F'"' '{print $2}'`
  local tempJSON=`echo $temp | awk -F"__INITIAL_STATE__ = " '{print $2}' | awk -F";</script>" '{print $1}'`
  DIR=`echo $tempJSON | jq '.store.AlbumDetailPage.albumInfo.mainInfo.albumTitle' | sed 's/"//g' | sed 's/ /_/g'`
  if [[ $DIR == "" ]]; then
    echo "get source json error !"
    exit 1
  fi
  if [ -d $DIR ]; then
    echo "already exist $DIR!"
    exit 1
  fi
  mkdir $DIR
  echo $tempJSON | jq -r '.store.AlbumDetailTrackList.tracksInfo.tracks[] | .title + "#" + (.trackId|tostring) ' | sed 's/[[:space:]]/_/g' > $TEMPTXT
  for((i=2;i<=$max;i++));
  do
    parsingSubPage "https://www.ximalaya.com/xiqu/$ID/p$i/" &
  done
  wait
  echo "get list done"
  echo "$DIR download start " > down.log
}

function parsingSubPage() {
  local url=$1
  local tempJSON=`curl -s $url | awk -F"__INITIAL_STATE__ = " '{print $2}' | awk -F";</script>" '{print $1}'`
  echo $tempJSON | jq -r '.store.AlbumDetailTrackList.tracksInfo.tracks[] | .title + "#" + (.trackId|tostring) ' | sed 's/[[:space:]]/_/g' >> $TEMPTXT
}

function main() {
  parsingMainPage
  while IFS='#' read -r TITLE TRACKID
  do
    ((TOTAL=$TOTAL+1))
    down $DIR $TITLE $TRACKID
  done < $TEMPTXT
  wait
  rm $TEMPTXT
  echo "all is done total $TOTAL"
}
main