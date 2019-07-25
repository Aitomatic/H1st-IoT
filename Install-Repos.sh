#!/bin/bash


CURRENT_DIR_PATH=$(pwd)


SDK_REPO_URL=https://github.com/adatao/SDK
SDK_DIR_NAME=SDK

BAI_DEV_REPO_URL=https://github.com/adatao/BAI-dev
BAI_DEV_DIR_NAME=BAI-dev

PRED_MAINT_DIR_NAME=PredMaint


git config --global credential.helper cache
git config --global credential.helper "cache --timeout=3600"


python2 -m pip install --upgrade pip --user


if [ ! -d $SDK_DIR_NAME ]; then
  git clone $SDK_REPO_URL
else
  cd $SDK_DIR_NAME
  git pull
  cd $CURRENT_DIR_PATH
fi

python2 -m pip install -e $SDK_DIR_NAME --upgrade --user


if [ ! -d $BAI_DEV_DIR_NAME ]; then
  git clone $BAI_DEV_REPO_URL
else
  cd $BAI_DEV_DIR_NAME
  git pull
  cd $CURRENT_DIR_PATH
fi

python2 -m pip install -e $BAI_DEV_DIR_NAME --upgrade --user


cd $PRED_MAINT_DIR_NAME
git pull
cd $CURRENT_DIR_PATH

python2 -m pip install -e $PRED_MAINT_DIR_NAME --upgrade --user