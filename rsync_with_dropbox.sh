#!/bin/bash

CURRENT_DIR=`dirname $0`
ENV="$CURRENT_DIR/../env/bin/activate"

source $ENV
cd $CURRENT_DIR
fab rsync_with_dropbox
