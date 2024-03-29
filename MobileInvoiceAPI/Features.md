<!-- TOC depthFrom:1 insertAnchor:true -->

- [Features and key concepts](#features-and-key-concepts)
  - [Merchant account](#merchant-account)
  - [Mobile invoive flow](#mobile-invoive-flow)
  - [Payment Gateway](#payment-gateway)
  - [PreTransaction](#pretransaction)
  - [Transaction](#transaction)

<!-- /TOC -->
<a id="markdown-features-and-key-concepts" name="features-and-key-concepts"></a>
# Features and key concepts

<a id="markdown-merchant-account" name="merchant-account"></a>
## Merchant account
The merchant account is basically an online bank account that will temporarily hold your money (you are the merchant) until it is moved into your actual bank account. After a successful sale, money will be transferred into your merchant account and it will sit there for a predefined period of time, then, in most cases, it will automatically be transferred into your bank account – the one that you actually think of as your bank account where you withdraw funds and so forth. You can sort of think of your merchant account as a temporary holding tank for the money that comes in from online sales. LINK Mobility can help you get started with merchant accounts depending on the type of payments you want to accept. If you only need Mobile Subscription billing, a merchant account with LINK Mobility will be provided. If you also want to support credit card payment, you will need an external merchant account and provide LINK Mobility with your Merchant account information. LINK Mobility can assist you with acquiring a merchant account.

<a id="markdown-mobile-invoive-flow" name="mobile-invoive-flow"></a>
## Mobile invoive flow

1. Your server generates a HMAC authentication header (See Authentication)
2. You send an HTTP Request to the API method of your choice, including the HMAC signature in the request.
3. The LINK Mobility server receives your request and processes it.
4. The response from LINK Mobility is returned in JSON or XML format.

Figure - Mobile invoive flow
![Figure - Mobile invoive flow](images/MobileInvoiceFlow.png)

<a id="markdown-payment-gateway" name="payment-gateway"></a>
## Payment Gateway
A Payment Gateway is the service that processes credit card or mobile phone billing transactions for you. When your customers are buying something, they enter their payment information (like credit card number) during the checkout process. The Payment Gateway is responsible for authorizing the transaction and processing the payment. In case of Card payment, if the credit card information submitted to the payment gateway matches the information on file with the credit card company and the charge is approved, the payment gateway will then transfer the money from your customers credit card into your merchant account. In the case of Phone billing, the system submits the payment request to the user's mobile operator, and if the user has sufficient funds on their subscription, the user will receive an SMS receipt that the funds have been deducted. The money from all the SMS transactions will be transferred to your bank account from LINK Mobility once a month.

The LINK Payment system is integrated with several payment gateways, and is continually expanding your options. Currently you can choose between the following:

* Credit/Debet card payments.
* Mobile phone subscription billing via premium SMS

<a id="markdown-pretransaction" name="pretransaction"></a>
## PreTransaction
In short, pre-transaction is the format of a invoice.
The **POST/pre-transaction** API method is the method that creates and distributes the actual Mobile Invoice.
The pre-transaction consist of all necessary information for the service to create and populate both the delivery part of Mobile Invoice, as well as the landing page that the end user/recipient is viewing.
```
View the API resource to learn more about pre-transaction content.
```
When an end user initiates the payment process, a transaction is created.

<a id="markdown-transaction" name="transaction"></a>
## Transaction
Transactions are the actual payments that have been set up with an amount and a payment method from the payment selection page and are ready to be processed. Further processing happens on a PSP page requiring some more information about the payment itself.

```
For more information on transaction endpoints see the API resource.
```

