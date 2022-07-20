import razorpay

CLIENT_KEY = '<YOUR CLIENT KEY>'
SECRET_KEY = '<YOUR SECRET KEY>'


def MakePayment():
    client = razorpay.Client(auth=(CLIENT_KEY, SECRET_KEY))
    # amount is Rs: 50 so we multiply by 100 because Razorpay understand Rs in Paisa
    data = {"amount": 500, "currency": "INR", "receipt": "order_rcptid_11"}
    payment = client.order.create(data=data)
    return payment

if __name__ == "__main__":
    res = MakePayment()
    print(res)
