The Stripe API is organized around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns [JSON-encoded](http://www.json.org/) responses, and uses standard HTTP response codes, authentication, and verbs.

You can use the Stripe API in test mode, which doesn’t affect your live data or interact with the banking networks. The API key you use to [authenticate](https://docs.stripe.com/api/authentication) the request determines whether the request is live mode or test mode.

The Stripe API doesn’t support bulk updates. You can work on only one object per request.

The Stripe API differs for every account as we release new [versions](https://docs.stripe.com/api/versioning) and tailor functionality. [Log in](https://stripe.com/login?redirect=https%3A%2F%2Fstripe.com%2Fdocs%2Fapi) to see docs customized to your version of the API, with your test key and data.

To know more: https://docs.stripe.com/api