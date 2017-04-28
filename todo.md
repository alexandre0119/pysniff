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

