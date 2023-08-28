import http.client
import ssl 

conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

payload = "token=wgf891ab3ncy4csb&to=+584242526757&body=test from python"
payload = payload.encode('utf8').decode('iso-8859-1') 

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/instance59279/messages/chat", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))