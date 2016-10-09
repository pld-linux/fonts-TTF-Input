#!/bin/sh

# abort on errors
set -e
# work in package dir
dir=$(dirname "$0")
cd "$dir"

prefix='Input-Font'
snap=$(date +%Y%m%d%H%M%S)
tmptarget="$prefix-$snap.zip"

url='http://input.fontbureau.com/build/?fontSelection=whole&a=0&g=0&i=0&l=0&zero=0&asterisk=0&braces=0&preset=default&line-height=1.2&accept=I+do&email='
licname="Font Software License Agreement"
licurl=http://input.fontbureau.com/license/

cat <<EOF

You must accept the $licname
to download this software.

$licurl

Press "ENTER" to Accept License Agreement
Press Ctrl-C to Decline License Agreement

EOF
read license

wget "$url" -O "$tmptarget"
version="$(unzip -c "$tmptarget" ChangeLog.txt | grep -m 1 '^\* v [0-9]\(\.[0-9]\)\+' | awk '{ print $3; }')"
echo "Version determined: $version"
mv "$tmptarget" "$prefix-$version.zip"
echo "Saved $prefix-$version.zip"
