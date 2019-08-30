## Post PreTransaction
(Add reference to SDK)
```csharp
void Main()
{
	//********* Test settings ************
	int partnerId = $"{partnerId}";
	var paymentProviders = new[] { "dibs","nets" };
	var baseUri = new Uri("https://test-pay-core.linkmobility.com/");
	string sharedKey = $"{sharedKey}";
	string msisdn = $"{mobileNo}";
	var expiryUtc = DateTime.UtcNow.AddDays(1);
	var referenceId = Guid.NewGuid().ToString();
	//********* /Test settings ************

	var request = new PreTransactionRequest
	{
		PartnerId = partnerId,
		ReferenceId = referenceId,
		CorrelationId = Guid.NewGuid().ToString(),
		ExpiryUtc = expiryUtc,
		Msisdn = msisdn,
		SmsNotificationOriginator = "Link",
		SmsNotificationText = "Betal her: {{paymentSelectionPageUrl}}",
		Currency = "NOK",
		Amount = 1,
		PaymentProviders = paymentProviders,
		Description = "SDK Test",
		SourceId = null,
		CustomLandingPageUrl = null,
	};

	var str = Task.Run(async () => await PostRequestAsync(partnerId, sharedKey, baseUri, request));
	str.Dump();

}

public static async Task<string> PostRequestAsync(int partnerId, string sharedKey, Uri baseUri, PreTransactionRequest request)
{
	string result;
	using (var paymentCoreClient = ClientFactory.Create(partnerId, sharedKey, baseUri, ClientFactory.DefaultTimeout, RetryPolicy.DefaultExponential))
	{
		Console.WriteLine("Processing...");

		var res = await paymentCoreClient.CreatePreTransactionAsync(request);
		result = res;
	}
	return result;
}
```