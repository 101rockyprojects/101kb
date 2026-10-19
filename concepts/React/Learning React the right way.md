# Retrospective

> A distilled, **noise-free** walkthrough of how each MAIN feature was built across branches
> `1 → 6`. The goal is not to re-read every diff, but to see the **crucial decisions**, the
> **React mindset** behind them, and the good practices that are easy to miss.

**Stack:** React 18 · TypeScript · Vite · Vitest + Testing Library + user-event · **Jotai** (global
state) · **SWR** + axios (data) · **react-hook-form** (forms) · react-router 7 · i18next · CSS Modules.

**How to read this file**
- Each branch = one concept to internalize.
- 🟢 = a good practice worth keeping · 🟡 = a trade-off or smell to watch.
- Code blocks are trimmed to the *crucial* lines only.

### One concept per branch

| Branch | MAIN feature | Core React concept |
|---|---|---|
| **1** `pagina-nueva-con-componente` | New page rendering a reusable card | Page (container) + presentational component |
| **2** `catalogo-con-paginacion` | Catalog with pagination | Lifting state up + controlled component + server state (SWR) |
| **3** `componentes-genericos-hoc-y-modal` | HOC loader + modal system | HOC + **compound components** + portals |
| **4** `formularios-y-filtros` | Create form + catalog filters | Reusable inputs + **react-hook-form** |
| **5** `gestion-de-errores-http-y-estados-globales` | Global alerts + HTTP errors | **Global state with Jotai** + centralized errors |
| **6** `carrito-de-compra` | Shopping cart | Persisted global state + **pure logic** + derived state |

---

## Branch 1 — `1-pagina-nueva-con-componente`

**Concept:** split responsibilities into a **page (container)** that owns data + state branching,
and a **presentational component** (`CharacterCard`) that just renders props.

### 🔑 The crucial idea: the page answers "what state am I in?"

```tsx
const { data: characters, isLoading, error } = useGetData<Character[]>({ url: '/personajes' });

if (isLoading) return <div>{t('characterlistpage.loading')}</div>;
if (error)     return <div>{t('characterlistpage.error')}</div>;
if (!characters?.length) return <div>{t('characterlistpage.noData')}</div>;

return characters.map(c => (
  <CharacterCard key={c.id} id={c.id} name={c.nombre} description={c.descripcion} />
));
```

> **Why it matters:** the page is a small state machine (`loading | error | empty | data`). The
> child never worries about any of that — it receives clean props. This is the mental model React
> is built around: *data flows down, UI is a function of state.*

### 🔑 The card encapsulates its own side effect (and cleans it up)

| ⛔ Naive (leaks memory) | ✅ What was done |
|---|---|
| `<img src={URL.createObjectURL(blob)} />` created on every render, never revoked | Create in `useEffect`, **revoke on cleanup** |

```tsx
useEffect(() => {
  if (!imageBlob) { setObjectImageUrl(undefined); return; }
  const objectUrl = URL.createObjectURL(imageBlob);
  setObjectImageUrl(objectUrl);
  return () => URL.revokeObjectURL(objectUrl); // 🟢 cleanup prevents blob-URL leaks
}, [imageBlob]);
```

- 🟢 **DTO → props mapping** (`nombre` → `name`) keeps the API shape out of the UI component.
- 🟢 `key={c.id}` uses stable identity, not array index.
- 🟢 Every user-facing string goes through i18n (`t(...)`).
- 🟡 A redundant `characters.length === 0` check remained in JSX after the early return; and the
  card wraps its output in an unnecessary `<>…</>` fragment.

---

## Branch 2 — `2-catalogo-con-paginacion`

**Concept:** **lift state up** to the page, pass it down to a **controlled** `Pagination`
component, and treat the server as the source of truth via **SWR**.

### 🔑 State lives in the parent; children are controlled

```tsx
const [currentPage, setCurrentPage] = useState(0);          // 0-based internally

const { data: catalogPage } = useGetData({
  url: '/catalogo',
  params: { pageNumber: currentPage.toString(), pageSize: PAGE_SIZE.toString() },
});

<Pagination currentPage={currentPage} totalPages={total} onPageChange={setCurrentPage} />
```

> **Controlled component pattern:** `Pagination` holds **no** state of its own. It renders from
> props and reports intent via `onPageChange`. The parent decides what to do. This makes the widget
> reusable anywhere.

### 🔑 Keep the "math" out of the render

```tsx
const getPaginationItems = (currentPage, totalPages): PaginationItem[] => {
  const ui = currentPage + 1;                          // 0-based state → 1-based UI
  if (totalPages <= 6) return range(totalPages);
  if (ui <= 4) return [1, 2, 3, 4, 'ellipsis', totalPages - 1, totalPages];
  // …windowing with ellipsis on both sides
};
```

- 🟢 Pure windowing logic is isolated → trivially unit-testable across boundaries.
- 🟢 `CatalogTable` stays "dumb": it receives `catalog: CatalogoDTO[]` and only renders.
- 🟢 Accessible nav: `<nav aria-label>`, buttons disabled at edges, localized labels.
- 🟢 SWR handles caching/revalidation; refetch is driven purely by `currentPage` changing.

| 🟡 Trade-off | Consequence |
|---|---|
| Pagination stored in local `useState` (not the URL) | Page isn't shareable via link and resets on refresh. Branch 4 moves toward query-param-derived params. |

---

## Branch 3 — `3-componentes-genericos-hoc-y-modal`

**Concept:** two reuse patterns — a **HOC/wrapper** (`WithLoader`) and a **compound component**
(`Modal` + `ModalHeader/Content/Footer`) — plus **portals** for overlays.

### 🔑 `WithLoader`: wrap, don't duplicate loading UI

```tsx
const WithLoader = ({ isLoading, loadingMessage, children }: WithLoaderProps) => {
  if (!isLoading) return <>{children}</>;
  return (
    <div role="status" aria-live="polite"> {/* 🟢 accessible loading region */}
      {/* spinner */}
      {loadingMessage && <p>{loadingMessage}</p>}
    </div>
  );
};
```

> **Why:** loading UI was previously repeated in every page. A wrapper centralizes it and makes it
> accessible (`role="status"`, `aria-live`) in one place.

### 🔑 Compound `Modal`: composition with guardrails + portal

```tsx
const allowedChildTypes = [ModalHeader, ModalContent, ModalFooter] as const;

const validated = React.Children.toArray(children);
validated.forEach(child => {
  if (!React.isValidElement(child) || !allowedChildTypes.includes(child.type))
    throw new Error(t('modal.invalid-child'));   // enforce valid composition
});

return createPortal(                              // 🟢 render above everything, escape overflow/z-index
  <dialog role="dialog" aria-modal="true" onClick={handleOverlayClick}>
    <button onClick={onClose}>&times;</button>
    {validated}
  </dialog>,
  document.body,
);
```

- 🟢 **Composition API:** consumers write `<Modal><ModalHeader/><ModalContent/><ModalFooter/></Modal>`
  — flexible slots, no giant prop list.
- 🟢 `createPortal(..., document.body)` escapes parent `overflow`/stacking contexts.
- 🟢 Closes on **overlay click** and **Escape** (keyboard listener added only while open, removed on cleanup).
- 🟢 The detail modal **defers its fetch until open**: `url: isOpen && id ? '/personajes/${id}/detalle' : null`.

| 🟡 Smell | Note |
|---|---|
| Runtime `React.Children` type validation | Defensive but heavy — TypeScript's `AllowedModalChild` union already covers most of it at compile time. |
| Modal tests use `fireEvent` | `userEvent` (used elsewhere) simulates real user behavior more faithfully. |

---

## Branch 4 — `4-formularios-y-filtros`

**Concept:** one **reusable `Input`** covering `text | select | textarea`, wired to
**react-hook-form**, and filters modeled as *transient form values* vs *applied state*.

### 🔑 One input primitive, three variants, accessible errors

```tsx
const Input = ({ id, label, type = 'text', registration, error, children }: InputProps) => (
  <div>
    <label htmlFor={id}>{label}</label>
    {type === 'select'   && <select   {...registration}>{children}</select>}
    {type === 'textarea' && <textarea {...registration} />}
    {type === 'text'     && <input    {...registration} />}
    <span id={`${id}-error`}>{error || ''}</span>  {/* aria-describedby target */}
  </div>
);
```

### 🔑 react-hook-form does the heavy lifting

| ⛔ Manual controlled form | ✅ react-hook-form |
|---|---|
| `useState` per field, manual `onChange`, manual validation, manual reset | `register` + `handleSubmit` + `formState.errors` + `reset()` |

```tsx
const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<Values>();

<Input id="name"
  registration={register('name', { required: t('createcharacter.required-field') })}
  error={errors.name?.message} />

// on success:
reset();  // 🟢 clears the form declaratively
```

- 🟢 Payload is **normalized before submit** (`nombre: values.name.trim()`), keeping the API clean.
- 🟢 Filters separate **what the user is typing** from **what is applied**:

```tsx
const [filters, setFilters] = useState<CatalogFiltersDTO>({ pageSize: 1 });
const onSubmit = v => { setPage(1); setFilters({ type: v.type || undefined, /* … */ }); };

// only active filters become query params:
const params = Object.fromEntries(
  Object.entries({ ...filters, pageNumber: page - 1 })
    .filter(([, val]) => val !== undefined && val !== '')
    .map(([k, val]) => [k, String(val)]),
);
```

| 🟡 Smell | Note |
|---|---|
| `Input` mixes UI + RHF integration | A bit "smart" for a primitive; fine here, but watch coupling. |
| Filters use both form state **and** local React state | Two sources of truth — harder to reason about than one. |

---

## Branch 5 — `5-gestion-de-errores-http-y-estados-globales`

**Concept:** **global UI state with Jotai** — a single `alertAtom` that any page can publish to,
rendered once, with **route-aware auto-dismissal**.

### 🔑 One atom = one source of truth for alerts

```ts
export interface AlertProps { type: 'success' | 'error'; message: string; closeOnPageChange?: boolean; }
export const alertAtom = atom<AlertProps | null>(null);
```

```tsx
// Publish from anywhere:
const setAlert = useSetAtom(alertAtom);
setAlert({ type: 'success', message: t('...'), closeOnPageChange: true });
```

> **Why Jotai over prop drilling:** the alert is cross-cutting — a form deep in the tree needs to
> notify a banner near the root. An atom decouples publisher from renderer without a Context wrapper
> ceremony.

### 🔑 Render once, dismiss on navigation

```tsx
const [alert, setAlert] = useAtom(alertAtom);
const { pathname } = useLocation();
const originPathname = useRef(pathname);

useEffect(() => {
  if (alert?.closeOnPageChange && pathname !== originPathname.current) {
    setAlert(null);                    // 🟢 avoid stale alerts after route change
    return;
  }
  originPathname.current = pathname;
}, [alert, pathname, setAlert]);
```

### 🔑 The create flow classifies the HTTP result

```tsx
const response = await request({ url: '/personajes', method: 'POST', data: payload });
if (response && !isAxiosError(response)) {
  setAlert({ type: 'success', message: t('...success'), closeOnPageChange: true });
  reset();
} else {
  setAlert({ type: 'error', message: t('...error', { error: response?.message }) });
}
```

- 🟢 **One global alert source**; any page publishes, one component renders.
- 🟢 Error **vs** success are explicit branches; user always gets feedback.
- 🟡 Alert lifecycle lives in a `useEffect` keyed on `alert` — implicit/stateful, but acceptable here.
- 🟢 Note the deliberate choice: **catalog load errors stay local** (`if (error) return <p>…</p>`),
  while **create/order errors go global**. Not every error belongs in a global banner.

---

## Branch 6 — `6-carrito-de-compra`

**Concept:** **persisted** global state (`atomWithStorage`), **pure business logic** extracted to
utils, and **derived state** (badge count) instead of duplicated state.

### 🔑 Persisted cart with almost no boilerplate

```ts
export interface ShoppingCartElement {
  productId: number; productName: string; productPrice: number; productQuantity: number;
}
export const shoppingCartAtom = atomWithStorage<ShoppingCartElement[]>('shoppingCart', []);
```

> `atomWithStorage` syncs to `localStorage` automatically — the cart survives refresh for free.

### 🔑 Business logic is **pure** (no React), so it's trivially testable

```ts
export const numberOfProductsInCart = (cart) =>
  cart.reduce((acc, p) => acc + p.productQuantity, 0);

export const addProductToCart = (cart, item) =>
  isProductInCart(cart, item.productId)
    ? changeProductQuantityIfExistsInCart(cart, item.productId, 'increment')
    : [...cart, item];

// quantity never drops below 1:
productQuantity: qty + delta > 0 ? qty + delta : 1
```

> **Why extract:** these functions take data in and return data out — no hooks, no DOM. That means
> fast, exhaustive unit tests and reuse across components. **Keep decisions in pure functions;
> keep React for wiring.**

### 🔑 Derive, don't duplicate

```tsx
const [shoppingCart] = useAtom(shoppingCartAtom);
const count = numberOfProductsInCart(shoppingCart);   // 🟢 derived on render, not stored separately
<p className={styles.cartCount}>{count}</p>
```

### 🔑 Clear side-effect boundaries on order submit

```tsx
const response = await request({ url: '/pedidos', method: 'POST', data: payload });
if (isAxiosResponse(response) && isStatusCreated(response)) {
  onClose(); setShoppingCart([]);                        // clear cart on success
  setGlobalAlert({ type: 'success', message: response.data ?? t('...') });
}
if (isAxiosError(response)) {
  navigate('/'); setGlobalAlert({ type: 'error', message: t('...') });
}
```

- 🟢 Cart math lives in pure utils; components only wire atoms to UI.
- 🟢 Badge is **derived state**, never a second copy that can drift.
- 🟡 A few `shoppingCart as ShoppingCartElement[]` casts hint the types could be tightened.
- 🟡 `ModalShoppingCart` has a `useEffect` that re-sets the same cart value — redundant.

---

## How the Tests Were Made — philosophy & the recurring questions

The tests share one belief: **test what the user experiences, not how the code is written.** If a
test breaks only because internals were refactored (not behavior), it was testing the wrong thing.

### Shared test infrastructure

**`tests/setup.ts`** — real i18n so assertions use real Spanish strings, and DOM cleanup:

```ts
i18next.use(initReactI18next).init({ lng: 'es', resources: { es: { translation: es } } });
afterEach(() => cleanup());   // isolate every test
```

**`tests/mocks/renderMock.tsx`** — the reusable wrappers that made global-state tests possible:

```tsx
export const WithJotaiHydration = ({ initialValues, children }) => (
  <Provider><HydrateAtoms initialValues={initialValues}>{children}</HydrateAtoms></Provider>
);
export const WithMemoryRouter = ({ children }) => <MemoryRouter>{children}</MemoryRouter>;
export const createInitialValues = (atom, value) => [[atom, value]];
```

> This tiny helper is the unlock for testing Jotai + routing: **seed a known atom state**, render,
> then assert both the **DOM** and the **store**.

### The layered strategy that emerged

| Layer | Tool / approach | Example from the branches |
|---|---|---|
| **Pure logic** | Plain unit tests, table of cases | `shopping-cart-utils.test.ts`: empty cart, increment, **floor at 1**, add new, remove |
| **Presentational component** | Render + query by role/text | `CharacterCard`, `Pagination`, `CatalogTable` |
| **Component + global state** | Hydrate atom / real `createStore()` + `store.set` | `Header`, `ShowGlobalAlert`, `ModalShoppingCart` |
| **Async / data** | Mock the data hook, not axios | `vi.mock('@/hooks/data/useGetData')`, mock `useAPIRequest` |
| **Browser APIs** | Stub them | mock `URL.createObjectURL` for image blobs |

### The query ladder (accessibility-first)

```
getByRole('button', { name })   ← prefer: matches how users/AT find elements
      ↓ (no role fits)
getByText(...)                  ← visible content
      ↓ (last resort)
getByTestId(...)                ← only when there's no accessible handle
queryBy* / queryByRole          ← for NEGATIVE assertions ("should NOT render")
```

- Interactions favor **`userEvent`** (real click/type sequences) over `fireEvent`.
- Negative assertions use `queryBy*` (returns `null`) instead of `getBy*` (throws).

### The recurring "am I writing a *good* unit test?" checklist

Each test round effectively asked:

1. **What state am I in?** — loading / error / empty / data. Is each branch covered?
2. **What would a user actually see or do?** — assert visible text, roles, and click/type flows.
3. **Where are the boundaries?** — first/last page, quantity flooring at 1, empty cart, replaced alert.
4. **Am I asserting behavior or internals?** — prefer role/text over class names and component internals.
5. **Did I isolate collaborators?** — mock data hooks, the router, the store, and browser APIs so a
   failure points at *this* unit.
6. **Is state seeded explicitly?** — hydrate atoms with `createInitialValues` so the starting point is known.
7. **Is each test independent?** — `cleanup()` + fresh store, no order dependence.

---

## Key Learnings (the resume)

1. **UI is a function of state.** Model pages as small state machines (`loading | error | empty |
   data`) and let children be pure functions of props.
2. **One source of truth.** Derive values (cart badge, active filters) instead of storing duplicates
   that can drift.
3. **Push decisions into pure functions.** Business logic with no React (`shopping-cart-utils`) is
   easier to reason about, reuse, and test than logic tangled in components.
4. **Pick the right reuse tool:** controlled components for widgets (`Pagination`), **compound
   components** for flexible slots (`Modal`), **HOC/wrapper** for cross-cutting UI (`WithLoader`),
   and **atoms** for cross-tree state (alerts, cart).
5. **Defer and gate work.** Fetch only when needed (`url: isOpen ? … : null`), and clean up side
   effects (`revokeObjectURL`, remove listeners) in `useEffect` returns.
6. **Accessibility is a first-class API.** Roles, `aria-live`, labels, and `aria-describedby` make
   the UI usable *and* make tests express intent (`getByRole`).
7. **Let libraries do the boring work.** react-hook-form for forms, SWR for server cache,
   `atomWithStorage` for persistence — less hand-rolled state, fewer bugs.
8. **Test behavior, not implementation.** The query ladder + `userEvent` + seeded stores produce
   tests that survive refactors.

## For future React systems — a checklist

- [ ] **Put shareable UI state in the URL** (pagination, filters) so links and refresh work.
- [ ] **Keep one source of truth** — avoid mirroring form values into a second `useState`.
- [ ] **Keep primitives dumb** — don't bake data-hook/RHF coupling into low-level components.
- [ ] **Centralize error handling**, but decide deliberately what is *global* vs *local*.
- [ ] **Tighten types** — treat `as` casts as a signal to fix the model, not silence it.
- [ ] **Prefer `userEvent` over `fireEvent`**, and `queryBy*` for negative assertions.
- [ ] **Extract pure logic** out of components and unit-test it exhaustively at the boundaries.
- [ ] **Co-locate tests** with components and seed global state explicitly in each test.
- [ ] **Isolate side effects** (network, navigation, storage) behind clear boundaries and clean them up.
- [ ] **Lean on TypeScript** for composition constraints before adding runtime validation.
