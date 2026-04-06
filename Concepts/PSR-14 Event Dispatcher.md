#### [Definitions](https://www.php-fig.org/psr/psr-14/#definitions "Permalink")

- **Event** - An Event is a message produced by an _Emitter_. It may be any arbitrary PHP object.
- **Listener** - A Listener is any PHP callable that expects to be passed an Event. Zero or more Listeners may be passed the same Event. A Listener MAY enqueue some other asynchronous behavior if it so chooses.
- **Emitter** - An Emitter is any arbitrary code that wishes to dispatch an Event. This is also known as the "calling code". It is not represented by any particular data structure but refers to the use case.
- **Dispatcher** - A Dispatcher is a service object that is given an Event object by an Emitter. The Dispatcher is responsible for ensuring that the Event is passed to all relevant Listeners, but MUST defer determining the responsible listeners to a Listener Provider.
- **Listener Provider** - A Listener Provider is responsible for determining what Listeners are relevant for a given Event, but MUST NOT call the Listeners itself. A Listener Provider may specify zero or more relevant Listeners.