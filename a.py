import africastalking

username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "c1b52636bea5738374a1566d32b3872bdaeeb0fb83aa50ad562476064cf4413d" # use your sandbox app API key for development in the test environment
africastalking.initialize("sandbox", "c1b52636bea5738374a1566d32b3872bdaeeb0fb83aa50ad562476064cf4413d")
sms = africastalking.SMS
response = sms.send("Jambo Mark! Your order is being processed and will be delivered in less than 30 minutes! thank you for being part of us", ["+254726830125"])
print(response)
