<!-- TOC depthFrom:1 insertAnchor:true -->

- [Get started](#get-started)
- [Using the api](#using-the-api)
- [Creating hmac](#creating-hmac)
- [How to send first mobile invoice](#how-to-send-first-mobile-invoice)
  - [Using MobileInvoice SDK](#using-mobileinvoice-sdk)
  - [Create the first invoice](#create-the-first-invoice)
  - [I don't use .NET (for my work and I want to keep it this way)](#i-dont-use-net-for-my-work-and-i-want-to-keep-it-this-way)

<!-- /TOC -->


<a id="markdown-get-started" name="get-started"></a>
# Get started

Before you can start using the API, you will receive 2 pieces of information that will be provided by LINK Mobility:

1. A Partner identification number.
2. A secret key. (***Important:*** _This key is highly confidential and you must keep it secure at all times!_) 

Also you have to have a merchant account for your chosen PSPs. 
* MerchantId: Is required to use a PSP, but note that some of the PSPs require a couple of extra properties.

The LINK Payment system is integrated with several payment gateways, and is continually expanding your options. Currently you can choose between the following:

* Credit/Debet card payments.
* Mobile phone subscription billing via premium SMS



<a id="markdown-using-the-api" name="using-the-api"></a>
# Using the api
> **HTTPS only**  
The Payment API allows HTTPS only, and is tested for security threats annualy.  

API urls

Environment | BaseUrl
----------- | -------
Production | "https://pay-core.linkmobility.com"
Test | "https://test-pay-core.linkmobility.com"

Generate a HMAC authentication header (See Creating hmac),  
including the HMAC signature in the request.  
The response from LINK Mobility is returned in JSON or XML format.
  
Integrating with the api is easiest using our [nuget](https://www.nuget.org/packages/LinkMobility.PaymentCore.Sdk/) package (which unfortunately is only available in C#).

Otherwise the HMAC header needs to be created, and included in any requests made.



<a id="markdown-creating-hmac" name="creating-hmac"></a>
# Creating hmac
[HMAC (Hashed based Message Authentication Code)](CreatingHmac.md)



<a id="markdown-how-to-send-first-mobile-invoice" name="how-to-send-first-mobile-invoice"></a>
# How to send first mobile invoice
```
Prerequisites: You have a Partner ID and a valid secret key provided from LinkMobility..
```


<a id="markdown-using-mobileinvoice-sdk" name="using-mobileinvoice-sdk"></a>
## Using MobileInvoice SDK

You can use the client library by referencing a NuGet package called <a href="https://www.nuget.org/packages/LinkMobility.PaymentCore.Sdk/" target="_blank">**LinkMobility.PaymentCore.Sdk**</a> 
The cornerstone of this library is the IPaymentCoreClient interface. To get an instance of the client you need to invoke the ClientFactory. At this point you’ll need your Partner Id and shared key provided by LinkMobility.

```csharp
var client = LinkMobility.PaymentCore.Sdk.ClientFactory.Create(myPartnerId, mySecretKey);
```

<a id="markdown-create-the-first-invoice" name="create-the-first-invoice"></a>
## Create the first invoice
To create your first invoice, you need to register a pre-transaction with MobileInvoice.
To do so, you need to prepare a PreTransactionRequest and then call the CreatePreTransactionAsync method.

```csharp
// Take all payment providers that are configured for the partnerId 
var paymentProviders = await client.GetAvailablePaymentProvidersAsync(myPartnerId); 
var preTransactionRequest = new PreTransactionRequest 
{     
    PartnerId = myPartnerId, // Change with partnerId.      
    Msisdn = "+123456789", // Change with the actual phone you want to send to.     
    SmsNotificationOriginator = "My Company", // This will appear as the name of the sender of the SMS     
    SmsNotificationText = "My message.To pay click here: {{paymentSelectionPageUrl}}", // This is your actual SMS message. Bear in mind that long messages will be transported as multiple SMS messages.
    Currency = "EUR", // The currency you're charging. Supported values as of now are EUR, USD, NOK, SEK, DKK, BGN 
    Amount = 1,    // The amount you're charging with the invoice.     
    PaymentProviders = paymentProviders.ToArray() }; // The payment channels you want to have available for the invoice.  
```

Here is a short description of what the fields in the request represent:
* PartnerId – This is your partner ID, assigned to you by LinkMobility.
* Msisdn – This is the phone number you want to send the invoice to.
* SmsNotificationOriginator – that’s the name that will show up as the sender of the SMS.
* SmsNotificationText – The text of the SMS message. Keep in mind that the SMS standard limits the length of the message, so long strings will be transmitted over multiple physical messages.
* Currency – The currency of the invoice. Supported values are NOK, DKK, SEK, EUR, USD, BGN.

That’s it! You have successfully sent your first Mobile Invoice!


<a id="markdown-i-dont-use-net-for-my-work-and-i-want-to-keep-it-this-way" name="i-dont-use-net-for-my-work-and-i-want-to-keep-it-this-way"></a>
## I don't use .NET (for my work and I want to keep it this way)
That's good. LinkMobility provides a web API. In fact, the above NuGet package is a thin layer over the web API to make calling the methods a little bit easier.
To see a full list of available API endpoints go to the **API resource**.
Sending an invoice is actually a single API call: a **POST** call to **/api/pre-transactions**. The request needs to conform to the following restrictions:
* Use **HTTPS** to call the endpoint
* Have a valid HMAC header. See [how to compose the HMAC](CreatingHmac.md) for your request
* Have a valid preTransactionRequest object in the body of the request

```
Upon success you would receive a 204 response code.
```