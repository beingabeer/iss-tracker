## iss-tracker
A simple python script for tracking the International Space Station (ISS).

## Details
This script uses [Open Notify](http://open-notify.org/)

>"Open Notify is an open source project to provide a simple programming interface for some of NASA’s awesome data.".

## How to use

Clone the repo.

`git clone https://github.com/beingabeer/iss-tracker.git`
`cd iss-tracker`

Install dependencies:

```
pip install requests
```

then run the script passing in 3 possible arguments(loc, pass or people):

examples - 
```
python iss-tracker.py people 

output - 
There are 3 people aboard the ISS. They are Chris Cassidy, Anatoly Ivanishin, Ivan Vagner.

```

```
python iss-tracker.py loc 

output - 
Ths ISS current location at 2020-08-27 09:36:58 is -34.0983 127.0608

```

```
python iss-tracker.py pass 
Enter latitude: 34
Enter longitude: 56

output - 
The ISS will be overhead lat 34 long 56 at -

2020-08-27 17:38:03 for 610 seconds
2020-08-27 19:14:39 for 624 seconds
2020-08-27 20:53:55 for 441 seconds
2020-08-27 22:33:18 for 335 seconds
2020-08-28 00:10:05 for 519 seconds

```
