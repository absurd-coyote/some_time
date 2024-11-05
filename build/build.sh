echo "Custom build script"

rm -rf public
mkdir public
cp -r deploy/* public/
mkdir public/some_time
cp -r some_time/domain public/some_time
cp -r some_time/inputs public/some_time
cp -r some_time/outputs public/some_time
