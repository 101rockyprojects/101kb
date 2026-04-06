# Stripe

Stripe es una plataforma de pagos con APIs para cobrar online (tarjeta, wallets, transferencias segun pais), gestionar suscripciones, emitir invoices, etc.

## Notas rapidas (API)

- API basada en REST, endpoints orientados a recursos, respuestas JSON.
- Tiene **test mode** vs **live mode** (segun la API key).
- Versionado de API: cambios se controlan por version.

Documentacion: https://docs.stripe.com/api

## Cosas a cuidar en pagos

- Webhooks: trata eventos como "source of truth" (no confies solo en el redirect del cliente).
- Idempotencia: reintentos son normales; usa idempotency keys y dedup. Ver [[concepts/Idempotencia]].

## Related

- [[concepts/Idempotencia]]
- [[concepts/Headers]]

You can use the Stripe API in test mode, which doesn’t affect your live data or interact with the banking networks. The API key you use to [authenticate](https://docs.stripe.com/api/authentication) the request determines whether the request is live mode or test mode.

The Stripe API doesn’t support bulk updates. You can work on only one object per request.

The Stripe API differs for every account as we release new [versions](https://docs.stripe.com/api/versioning) and tailor functionality. [Log in](https://stripe.com/login?redirect=https%3A%2F%2Fstripe.com%2Fdocs%2Fapi) to see docs customized to your version of the API, with your test key and data.

To know more: https://docs.stripe.com/api
