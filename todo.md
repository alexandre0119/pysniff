# To-Do   
1. All frame type frame/radiotap/wlan_radio/wlan layers get and check data

2. !!! Need to draw code diagram !!!

3. Overall all packet analysis
    * Get all packet type, percentage, and plot chart.

# Issue
1. Frame field names are identical with different value, i.e. beacon frame 'supported_rates' and some other similar fields
    * Only able to get the first value due to Pyshark lib issue
    * Will try to find another method to fix it later

# Completed
1. Beacon
    * Get all fields data from pcapng file
        * Frame/Radiotap/WLAN/WLAN_Radio/WLAN_MGT layers
    * Fields to check reference data set in config file
    * All field data check
    * Beacon time delta display chart plot
    * Beacon wlan seq chart plot

2. Report summary
    * To CSV
        * Original all fields data to csv
        * Compare ref data vs get data results to csv
        * To PNG
    * Console Pass field, Fail fields, Skip fields display
    * Log file

3. Probe request/response
    * frame/radiotap/wlan_radio/wlan layers get and check data
