import razorpay

CLIENT_KEY = '<YOUR CLIENT KEY>'
SECRET_KEY = '<YOUR SECRET KEY>'
# Callback output you can catch this from the browser alert

PAYMENT_ID = "<PAYMENT ID>" #eg.   pay_29QQoUBi66xm2f
ORDER_ID = "<ORDER_ID>" #eg.  order_9A33XWu170gUtm
SIGNATURE_ID = "<SIGNATURE ID>" #eg. 9ef4dffbfd84f1318f6739a3ce19f9d85851857ae648f114332d8401e0949a3d

def Verify_Signature():
    client = razorpay.Client(auth=(CLIENT_KEY, SECRET_KEY))
    params_dict = {
        'razorpay_order_id': ORDER_ID,
        'razorpay_payment_id': PAYMENT_ID,
        'razorpay_signature': SIGNATURE_ID
    }
    check = client.utility.verify_payment_signature(params_dict)
    if check:
        print("Successful")
    else:
        print("Fail")


if __name__ == '__main__':
    Verify_Signature()
