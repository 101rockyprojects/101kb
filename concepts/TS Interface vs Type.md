## Types and type aliases

`type` is a keyword in TypeScript that we can use to define the shape of data. The basic types in TypeScript include:
- String
- Boolean
- Number
- Array
- [Tuple](https://blog.logrocket.com/use-cases-named-tuples-typescript/)
- [Enum](https://blog.logrocket.com/typescript-string-enums-guide/)
- Advanced types
Each has unique features and purposes, allowing developers to choose the appropriate one for their particular use case.

Type aliases in TypeScript mean “a name for any type.” They provide a way of creating new names for existing types. **Type aliases don’t define new types**; instead, they provide an alternative name for an existing type.  
Type aliases can be created using the `type` keyword, referring to any valid TypeScript type, including primitive types.

`type MyNumber = number;`
`type User = {`
  `id: number;`
  `name: string;`
  `email: string;`
`}`

In the above example, we create two type aliases: `MyNumber` and `User`. We can use `MyNumber` as shorthand for a number type and use `User type aliases` to represent the type definition of a user.

`type ErrorCode = string | number;`
`type Answer = string | number;`

The two type aliases above represent alternative names for the same union type: `string | number`. While the underlying type is the same, the different names express different intents, which makes the code more readable.

## Interfaces in TypeScript

In TypeScript, an interface defines a contract that an object must adhere to. Below is an example:

`interface Client {` 
    `name: string;` 
    `address: string;`
`}`

We can express the same `Client` contract definition using type annotations:

`type Client = {`
    `name: string;`
    `address: string;`
`};`

### Union types

Union types allow us to describe values that can be one of several types and create unions of various primitive, literal, or complex types:

type Transport = 'Bus' | 'Car' | 'Bike' | 'Walk';

### Union interfaces

Union interfaces allow us to expand another interface if both have the same name:

`interface foo {` 
    `a: string;` 
`}
`interface foo {` 
    `b: string;` 
`}
`interface foo {` 
    `c: string;` 
`}
`function bar {` 
    `x.a;` 
    `x.b;` 
    `x.c;` 
`}
Like 