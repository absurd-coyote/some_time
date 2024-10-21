echo "Custom build script"

rm -rf public
mkdir public
cp -r deploy/* public/
cp -r some_time/domain public/
cp -r some_time/inputs public/
cp -r some_time/outputs public/
