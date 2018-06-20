import africastalking

username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "c1b52636bea5738374a1566d32b3872bdaeeb0fb83aa50ad562476064cf4413d" # use your sandbox app API key for development in the test environment
africastalking.initialize("sandbox", "c1b52636bea5738374a1566d32b3872bdaeeb0fb83aa50ad562476064cf4413d")
sms = africastalking.SMS
response = sms.send("an order has been made,check your order list", ["+254726830125"],["+254726830125"])
print(response)
