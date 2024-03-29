<!-- TOC depthFrom:1 insertAnchor:true -->

- [Common user stories](#common-user-stories)
- [Typical Flow of a Credit Card Payment](#typical-flow-of-a-credit-card-payment)
- [Mobile Invoice basic sequence](#mobile-invoice-basic-sequence)

<!-- /TOC -->

<a id="markdown-common-user-stories" name="common-user-stories"></a>
# Common user stories

* Send invoice by sms to users.
* Request payment from a Mobile user
  Allow the user to choose payment method (Phone/SMS or Card).
* Initiate transactions directly when you already know the payment method.
* See transaction status and billing information.
* Define your own callback URL's for receiving status information.
* Define your own URL's for user navigation and landingpages.

<a id="markdown-typical-flow-of-a-credit-card-payment" name="typical-flow-of-a-credit-card-payment"></a>
# Typical Flow of a Credit Card Payment

* Invoice is sent to the API
* Sms is sent to user (inclusing link to landing page)
* User opens url (navigates to landing page)
* User selects paymentmethod (from included in the invoice)
* User is redirected to PSP site for payment.
* Payment done - user is redirected to receipt page.

![Typical credit card payment flow](images/start1.png)


<a id="markdown-mobile-invoice-basic-sequence" name="mobile-invoice-basic-sequence"></a>
# Mobile Invoice basic sequence
![Mobile Invoice basic sequence](images/flowchart.png)