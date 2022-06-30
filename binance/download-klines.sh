#!/bin/bash

# This is a simple script to download klines by given parameters.
SHELL_FOLDER=$(dirname "$0")
basedir="${SHELL_FOLDER}/data/klines"
symbols=("BUSDUSDT") # add symbols here to download
intervals=("1h")
years=("2019" "2020" "2021")
months=(01 02 03 04 05 06 07 08 09 10 11 12)

baseurl="https://data.binance.vision/data/spot/monthly/klines"

for symbol in ${symbols[@]}; do
  for interval in ${intervals[@]}; do
    for year in ${years[@]}; do
      for month in ${months[@]}; do
        url="${baseurl}/${symbol}/${interval}/${symbol}-${interval}-${year}-${month}.zip"
        response=$(wget -P ${basedir} --server-response -q ${url} 2>&1 | awk 'NR==1{print $2}')
        if [ ${response} != '200' ]; then
          echo "File not exist: ${url}"
        else
          echo "downloaded: ${url}"
        fi
      done
    done
  done
done
unzip ${basedir}/\*.zip -d ${basedir}
rm -rf ${basedir}/*.zip
