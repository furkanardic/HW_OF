import requests
first = input("Your first money unit:")
second = input("Your second money unit:")
try:
    url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market={}-{}".format(first,second)
    variable = requests.get(url)
    data = variable.json()
    if data['success'] == False:
        print("Your selections are not accessible.Try another money units...")
    else:
        print("{} currency for {}:".format(second, first), data["result"][0]["Last"], "\nLast time stamp:",data["result"][0]["TimeStamp"])
except:
    print("Source is not available...Please try another time or make contact with your developer...")

#try,except added for some bugs.
