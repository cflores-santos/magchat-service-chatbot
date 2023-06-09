#This file is used to store configuration settings for your bot.
#You can define constants, API keys, endpoints, or any other configuration variables needed for your bot's operation.
#It helps separate configuration from the main bot logic and makes it easier to update settings as needed.

import os

# Azure Bot Service Credentials
BOT_ID = os.getenv('BOT_ID', '')
MICROSOFT_APP_ID = os.getenv('MICROSOFT_APP_ID', '')
MICROSOFT_APP_PASSWORD = os.getenv('MICROSOFT_APP_PASSWORD', '')

# Azure Cognitive Services Credentials
COGNITIVE_SERVICE_KEY = os.getenv('COGNITIVE_SERVICE_KEY', '')
LUIS_APP_ID = os.getenv('LUIS_APP_ID', '')
LUIS_ENDPOINT = os.getenv('LUIS_ENDPOINT', '')

# Other Configurations
# ...

