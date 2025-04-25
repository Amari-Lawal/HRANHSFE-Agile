if [[ $1 == "" ]]
then
  python -m unittest HRANHSUnittests.HRANHSUnittests.HRANHSUnittests
else
  python -m unittest HRANHSUnittests.HRANHSUnittests.HRANHSUnittests.$1
fi