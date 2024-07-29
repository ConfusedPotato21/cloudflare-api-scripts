# For additional information visit:
# https://developers.cloudflare.com/ssl/reference/certificate-authorities/

# https://developers.cloudflare.com/api/operations/universal-ssl-settings-for-a-zone-universal-ssl-settings-details

# https://community.cloudflare.com/t/ssl-edge-certificate-stuck-in-pending-verification/685831

import http.client

conn = http.client.HTTPSConnection("api.cloudflare.com")

payload = "{\n  \"certificate_authority\":\"lets_encrypt\"\n}" # lets_encrypt , digicert , google - whatever you like - check link 1, some authorities don't support certain features.

headers = {
    'Content-Type': "application/json",
    'X-Auth-Email': "your_email", # Your email between quotes
    'X-Auth-Key': "your_global_api_key" # Your API key between quotes
    }

conn.request("PATCH", "/client/v4/zones/your_zone_id/ssl/universal/settings", payload, headers) # replace your_zone_id with your Zone ID - don't insert any quotes

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))