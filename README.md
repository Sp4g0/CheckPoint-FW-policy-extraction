### CheckPoint-FW-policy-extraction

Whit this script you can easly see the Chech-point firewall Domain/policy changes

It's tested only on the SMARTVIEV R80,

You'll need:

Audit log .ZIP file, version full\
Or audit logs .CSV file, automatically extract from the .ZIP file

It's necessary to download the audit logs with full columns to make this process working. The script need to extract values from "Domain" and "Changes" columns

First download this pip library from cmd or terminal:\
pip install pandas\
pip install openpyxl

