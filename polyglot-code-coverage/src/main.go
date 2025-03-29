package main

import "fmt"

// #include <stdint.h>
import "C"

func Add(a int, b int) int {
	return a + b
}

func main() {
	fmt.Println("Hello, Polyglot World!")
}
