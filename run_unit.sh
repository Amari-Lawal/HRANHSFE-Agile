if [[ $1 == "" ]]
then
  python -m unittest HRANHSUnittests.HRANHSAuth.HRANHSAuth
else
  python -m unittest HRANHSUnittests.HRANHSAuth.HRANHSAuth.$1
fi