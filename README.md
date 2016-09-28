# iphone_check_availability
Checks availability of a Iphone 7 in the stores you specify

You will need to feed in the correct URL for your region. 
You will have to change the following in the script.
`region_url = "https://reserve.cdn-apple.com/NL/nl_NL/reserve/iPhone/"`

Then just fire away the script,
`python check_availability.py`

and it will start monitoring the stores for the availability of the models listed in the script.
It checks the store every 30 seconds.
One Dot for every 30 seconds until something is available.

