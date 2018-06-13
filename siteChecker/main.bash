#!/bin/bash

URL="https://sports.linux.it.teu.ac.jp/"
DEBUG=1
DATE=$(date "+%Y/%m/%d %H:%M:%S")

# Send Req
RESPONSE_CODE=$(curl -LI $URL -o /dev/null -w '%{http_code}\n' -s)

# Handle ReqCode
if [ $RESPONSE_CODE -lt 500 ] ; then # RESPONSE_CODE < 500

  # SUCCESS
  test $DEBUG -gt 0 && echo "[DEBUG] Successful access"

else
  
  # FAIL
  test $DEBUG -gt 0 && echo "[DEBUG] Fail to access"

  ### Post to Slack
  TOKEN='xoxp-3987726559-181496154662-194463962320-f8bb0d513d333cf7e486096e07321e7b'
  USER='SiteChecker'
  CHANNEL='sportsfes'
  MESSAGE="[Error:$RESPONSE_CODE] Fail to access $URL at $DATE"

  curl -s -XPOST -d "token=$TOKEN" \
                 -d "channel=#$CHANNEL" \
                 -d "text=$MESSAGE" \
                 -d "username=$USER" \
                 "https://slack.com/api/chat.postMessage" # >& /dev/null &

fi

