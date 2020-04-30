cd client-lib-cpp
make clean
cmake .
cd ClientLib
make
cd ../..
python3 setup.py build_ext -i
cp *.so dp_client/
rm *.so