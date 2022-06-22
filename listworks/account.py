accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]



# # for ac in accounts:
# #     if ac["acno"]==1002:
# #         trans=ac.pop("transcations")
# #         print(ac)
# saving_details=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
# print(saving_details)
#
# accounts.sort(reverse=True,key=lambda ac:ac["balance"])
# print(accounts)
# accounts.sort(reverse=True,key=lambda ac:ac["balance"])
# print(accounts)
# print all phine_pay transaction
# transaction=[ac["transactions"] for ac in accounts ]
# phone_pay=[trans for ftrans in transaction for trans in ftrans if trans["method"]=="phone-pay"]
# print(phone_pay)
#
# #q4 prit all transactions where transaction amount > 500
# greater=[trans for ftrans in transaction for trans in ftrans if trans["amount"]>500]
# print(greater)
# #q5 crredit transactions of 1002
# credit=[trans for ftrans in transaction for trans in ftrans if trans["to"]==1002]
# print(credit)
#q6 aggregate transactions based on payment mode



pms={}
all_transaction=[ac["transactions"] for ac in accounts ]
transactions=[trans for t in all_transaction for trans in t]
for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount
print(max(pms.items(),key=lambda ite:ite[1]))
