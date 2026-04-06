Todas mis preguntas están en esta conversación con Deepseek: https://chat.deepseek.com/a/chat/s/8a3998cf-86d0-442b-be32-1e78fa10c5dd

# **PRIMEROS PASOS**
## **Asignación de valor**
En Go, no solo se usa `=`, también se usa `:=`.
### Diferencias clave:

|Característica|`:=`|`=`|
|---|---|---|
|Declara variable|✅ Sí|❌ No|
|Asigna valor|✅ Sí|✅ Sí|
|Variable debe existir|❌ No|✅ Sí|
|Se puede usar fuera de funciones|❌ No|✅ Sí|
#### Ejemplo:
```go
package main

import "fmt"

// variable global - debe usar var
var global = "Soy global"

func main() {
    // Declaración y asignación en una línea
    mensaje := "Hola Mundo"
    
    // Re-asignación
    mensaje = "Hola Go!"
    
    // Declaración explícita luego asignación
    var contador int
    contador = 10
    contador = 15  // Re-asignación
    
    // Múltiples variables
    a, b := 1, 2
    a, b = b, a  // Intercambio de valores
    
    fmt.Println(mensaje, contador, a, b)
}
```

## **Declaración de variables**
En Go existe la función `make()` la cual genera una instancia segura para ciertos tipos de variables.
```go
// Inicializar con make en lugar de usar nil
var safeMap = make(map[string]int)  // ✅ Mejor práctica
safeMap["clave"] = 1                // ✅ Funciona seguro

var safeSlice = make([]int, 0)      // ✅ Slice vacío, no nil
safeSlice = append(safeSlice, 1)    // ✅ Funciona
```

#### Ejemplos de tipos en Go:
```go
package main

import "fmt"

func main() {
    // 1. PUNTERO
    var pointer *int = nil
    if pointer == nil {
        num := 42
        pointer = &num
    }
    fmt.Printf("Puntero: %d\n", *pointer)

    // 2. SLICE
    var slice []int = nil
    if slice == nil {
        slice = make([]int, 0)
        slice = append(slice, 1, 2, 3)
    }
    fmt.Printf("Slice: %v\n", slice)

    // 3. MAP
    var m map[string]int = nil
    if m == nil {
        m = make(map[string]int)
        m["edad"] = 25
    }
    fmt.Printf("Map: %v\n", m)

    // 4. CHANNEL
    var ch chan int = nil
    if ch == nil {
        ch = make(chan int, 1)
        ch <- 100
    }
    fmt.Printf("Channel: %d\n", <-ch)

    // 5. FUNCIÓN
    var f func() = nil
    if f == nil {
        f = func() {
            fmt.Println("Función ejecutada!")
        }
    }
    f()

    // 6. INTERFACE
    var iface interface{} = nil
    if iface == nil {
        iface = "Soy una interface ahora"
    }
    fmt.Printf("Interface: %v\n", iface)
}

// SALIDA
// Puntero: 42
// Slice: [1 2 3]
// Map: map[edad:25]
// Channel: 100
// Función ejecutada!
// Interface: Soy una interface ahora
```

## **Valor nulo Nil**
En Go, para representar el concepto de ausencia de valor se usa `nil`.
```go
// nil representa la ausencia de valor para:
var pointer *int = nil       // punteros
var slice []int = nil        // slices
var m map[string]int = nil   // maps
var ch chan int = nil        // channels
var f func() = nil           // funciones
var iface interface{} = nil  // interfaces

// Pero NO para primitivos:
var str string           // strings (valor por defecto "")
var num int              // numericos (valor por defecto 0)
var check bool           // booleanos (valor por defecto false)
```


## **Ciclos e iterables**
En Go, se trabajan los objetos iterables con el ciclo for, tal como se muestra en el siguiente ejemplo:
```go
for i, fruta := range frutas {
    fmt.Printf("%d: %s\n", i, fruta)
}
```
Donde se describe primero las variables i (índice o posición) y fruta (valor de la posición), a partir del `range frutas.

#### Otros ejemplos:
```go
// Solo valores (ignorar índice)
for _, fruta := range frutas {
    fmt.Println(fruta)
}

// Solo índice
for i := range frutas {
    fmt.Println(i)
}

// Con arrays, slices, maps, e incluso strings!!!
palabra := "Hola"
for i, letra := range palabra {
    fmt.Printf("%d: %c\n", i, letra)
}
```

## **Condicionales**
En Go, no se usan los paréntesis para encapsular la condición en un if.
Y curiosamente, se pueden hacer declaraciones en la propia condicional.

#### Ejemplo:
```go
if edad, existe := edades["Ana"]; existe {  // value, bool := map[key]
    fmt.Println("Edad de Ana:", edad)
} else {
    fmt.Println("Ana no existe en el map")
}
```
##### **Desglose:**
- `edad, existe := edades["Ana"]`: Declara y asigna variables
- `; existe`: Condición que se evalúa
- El scope de `edad` y `existe` es SOLO dentro del if/else

Esto no es _camisa de fuerza_, puede hacerse de forma tradicional:
```go
edad, existe := edades["Ana"]  // Variables visibles en todo la función
if existe {
    fmt.Println("Edad de Ana:", edad)
} else {
    fmt.Println("Ana no existe")
}
// edad y existe siguen existiendo aquí
```
##### **Ventajas del estilo Go:**
- **Scope limitado**: Las variables solo existen en el bloque if/else
- **Código más limpio**: No contaminas el scope exterior
- **Menos errores**: Evitas usar variables no inicializadas}

### ¿Por qué no solo usar `edad := edades["Ana"]`?
En lenguajes como Java o PHP, esto podría provocar devolver un null o incluso una excepción.
Incluso, podríamos argumentar que genera una ambigüedad, pues en caso de que retorne `null` no podríamos saber si Ana no existe en el mapa o sí existe pero su edad está almacenada como null.
En Go, al usar `edad, existe := edades["Ana"]` no solo estamos obteniendo el valor de la colección, en este caso un mapa, sino también información de su existencia.
```go
edad := edades["Ana"]  // Si Ana no existe, edad = 0
// ❌ No sabes si Ana existe o si tiene 0 años
```
Incluso podríamos evaluar la edad a partir de la declaración al estilo Go, pero sin necesidad de obtener la edad.
```go
 if _, existe := edades["Ana"]; existe {
    fmt.Println("Ana existe en el map")
} else {
    fmt.Println("Ana no existe")
}
 ```
 