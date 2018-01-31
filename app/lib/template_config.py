# Configuration Data
#
# Instructions:
#   1. Set each value approperiately
#   2. Create a config directory in lib/
#   3. Rename this file to config.py and move to lib/config/
#
#   `mkdir config && cp template_config.py config.py && mv config.py config/`
#
# *** IMPORTANT *** 
#   Turn OFF Debugging mode when going live!!
#
# Examples/Documentation:
# 
#   Field            |  Value  |  Description
#####################################################################
# DEBUG              | boolean | Display trace in browser on failure.
# SECRET_KEY         | string  | Flask app key.
# MAIL_SERVER        | string  | Set mail server address.
# MAIL_PORT          | int     | Set mail server port.
# MAIL_USE_SSL       | boolean | (Don't)Use SSL.
# MAIL_USERNAME      | string  | Sending email address.
# MAIL_PASSWORD      | string  | Sending email password.
# MAIL_DEFAULT_SENDER| string  | Same as MAIL_USERNAME
# TARGET_EMAIL       | string  | Where you want your forms sent.
# ZIP_API_KEY        | string  | Key from zipcodeapi.com, fill this in only if 
#                    |         | you are using the dynamic addressing feature.
# ZIP_FORMAT         | string  | DO NOT CHANGE
# ZIP_UNIT           | string  | DO NOT CHANGE
# HOMEBASES          | list    | Enter zipcodes of your addresses.
# ADDRESSES          | ls/dict | List of dict entries. Enty: Full addresses.
# DEFAULT_ZIP        | int     | Failsafe for dynamic addresses.
# DYNAMIC_ADDRESS    | boolean | False = Uses DEFAULT_ZIP

# Server
DEBUG=True
SECRET_KEY=""

# Mail
MAIL_SERVER=""
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME=""
MAIL_PASSWORD=""
MAIL_DEFAULT_SENDER=""
TARGET_EMAIL=""

# Dynamic/Static Address
DYNAMIC_ADDRESS=False
ZIP_API_KEY=""
ZIP_FORMAT="json"
ZIP_UNIT="mile"
HOMEBASES=[00000]
ADDRESSES=[
{"street": "123 Main Street", "city": "Liberty Town", "state": "VA", "zipcode": 00000}]
DEFAULT_ZIP=ADDRESSES[0]['zipcode']
