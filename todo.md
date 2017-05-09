# To-Do   
1. Prob request frame 
    * Get all fields data from pcapng file

2. Overall all packet analysis
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


  
    
      
  
Dear All,

I am using Pyshark to parse Wireshark sniffer log, and I used exported Json format file (based on pcapny file) to find field names when use 'get_field_value' function to retrieve field value. 

For example, in order to get BSSID value:
- In Json format file, this info is displayed as
       
        "wlan.bssid": "11:22:33:44:55:66"
- Then I could use:
        
        value = packet['wlan'].get_field_value('bssid')
- Result is expected:

        value == '11:22:33:44:55:66'
- For this case, it is working fine.


But I encounter an issue with below condition when I move to 'wlan_mgt' section in a beacon packet as example showing below:
- In Json format file, it shows:

          "wlan_mgt.tagged.all": {
            "wlan_mgt.tag": {
              "wlan_mgt.tag.number": "0",
              "wlan_mgt.tag.length": "5",
              "wlan_mgt.ssid": "MWIFI"
            },
            "wlan_mgt.tag": {
              "wlan_mgt.tag.number": "1",
              "wlan_mgt.tag.length": "6",
              "wlan_mgt.supported_rates": "24",
              "wlan_mgt.supported_rates": "164",
              "wlan_mgt.supported_rates": "48",
              "wlan_mgt.supported_rates": "72",
              "wlan_mgt.supported_rates": "96",
              "wlan_mgt.supported_rates": "108"
            },
            "wlan_mgt.tag": {
              "wlan_mgt.tag.number": "5",
              "wlan_mgt.tag.length": "7",
              "wlan_mgt.tim.dtim_count": "0",
              "wlan_mgt.tim.dtim_period": "1",
              "wlan_mgt.tim.bmapctl": "0x00000000",
              "wlan_mgt.tim.bmapctl_tree": {
                "wlan_mgt.tim.bmapctl.multicast": "0",
                "wlan_mgt.tim.bmapctl.offset": "0x00000000"
              },
              "wlan_mgt.tim.partial_virtual_bitmap": "00:10:00:00",
              "wlan.tim.aid": "0x0000000c"
            },

As we can see, there are multiple entries for "wlan_mgt.supported_rates", the field name (key) are the same, and the value for each entry is different which I will need to get them all. But if I use:
- If I use:

        value = packet['wlan_mgt'].get_field_value('supported_rates')
- Then it only gives me value '24' which is the value of 1st entry. And I have no idea how to retrieve other entry values since the key name is the same.

Should it return a list of all values like ['24', '164','48','72','96','108'], rather than only the 1st entry value?
Since based on sniffer log (Json format), there are many other entries with same field name, for example
 'wlan_mgt.tag.number', but different field value, so this issue is a blocker for me.  
 
Pls advice, and Thanks a lot in advance!

BR,  
Alex


Hi,   

Thanks a lot for the information!  

The usage of 
    
    packet_layer.field_names
is quite convenient, compare with using get_field_value() function. But it seems not solve the original issue I encountered, 
elaborate some details here:
Use
    
    value = packet.wlan_mgt 
Then print out value we could see all fields in wlan_mgt layer displayed, 
the 'supported_rates' looks like this:
    
    ... some other field values ...
    Supported Rates: 18(B) (0xa4)
    Supported Rates: 24 (0x30)
    Supported Rates: 36 (0x48)
    Supported Rates: 48 (0x60)
    Supported Rates: 54 (0x6c)
    ... some other field values ...

Use
    
    value = packet.wlan_mgt.supported_rates
Then print out value we see is
    
    24
which is only one of the value. I am expecting to get all values as 18, 24, 36, 48, 54 for supported_rates field.

          ...........
          "wlan_mgt.tagged.all": {
            "wlan_mgt.tag": {
              "wlan_mgt.tag.number": "0",
              "wlan_mgt.tag.length": "5",
              "wlan_mgt.ssid": "MWIFI"
            },
            "wlan_mgt.tag": {
              "wlan_mgt.tag.number": "1",
              "wlan_mgt.tag.length": "6",
              "wlan_mgt.supported_rates": "24",
              "wlan_mgt.supported_rates": "164",
              "wlan_mgt.supported_rates": "48",
              "wlan_mgt.supported_rates": "72",
              "wlan_mgt.supported_rates": "96",
              "wlan_mgt.supported_rates": "108"
            },
            "wlan_mgt.tag": {
              "wlan_mgt.tag.number": "5",
              "wlan_mgt.tag.length": "7",
              "wlan_mgt.tim.dtim_count": "0",
              "wlan_mgt.tim.dtim_period": "1",
              "wlan_mgt.tim.bmapctl": "0x00000000",
              "wlan_mgt.tim.bmapctl_tree": {
                "wlan_mgt.tim.bmapctl.multicast": "0",
                "wlan_mgt.tim.bmapctl.offset": "0x00000000"
              },
              "wlan_mgt.tim.partial_virtual_bitmap": "00:10:00:00",
              "wlan.tim.aid": "0x0000000c"
            },
          ...............

Therefore, is there any way to get all value for the same entry name?

BTW, I tried to use

    packet.wlan_mgt.tagged.all.tag
    
But it gives me 'AttributeError', if I use

    packet.wlan_mgt.tagged_all
it returns as below, but no details info:

    Tagged parameters (206 bytes)

Please let me know if I miss out something from your comment, 
or if there is any more info you need about this question.

Thank you very much!

BR,  
Alex

Hi,

Sorry for late reply, I just get up. It is my bad which not make
the question clear: I am reading the pcapng file directly using below basic cmds flow
 , I mentioned the Json format because I exported the pcapng to Json so that I
  can copy the key:value pair from that section and paste here to show you which field 
  value I tried to retrieve. 

    capture = 'assoc.pcapng'  # For example the, the saved capture name is 'assoc.pcapng'
    cap = pyshark.FileCapture(capture, only_summaries=False, display_filter=filter_str)
    packet = cap[0]
    
    value_0 = packet.wlan_mgt
    value_1 = packet.wlan_mgt_supported_rates
    
    print(value_1)  # only able to display one supported_rates value (24) here, I found
    not way to get all data rate values which are 18, 24, 36, 48, 54

Basically I am writing code to get all data from capture file categorized by frame types,
and do some analysis. Things went well in MAC layer data, they are exactly follow 
key:value pair which key name is unique. But when I stepped through to wlan_mgt layer, I 
encountered this issue, which field name are the same, but give different values. 
I can see all entries displayed if dump entire wlan_mgt info, so it should be a way
to display all data in this certain field, not just the 1st value...

Pls let me know if you need any more info, Thank you~ 

BR,  
Alex
