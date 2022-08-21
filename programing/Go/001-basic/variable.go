package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello World")

	// 使用 var 定义变量
	var a = "var_a"
	fmt.Println(a)

	var b, c = 1, 2
	fmt.Println(b, c)

	var d = true
	fmt.Println(d)

	var e int
	fmt.Println(e)

	// The := syntax is shorthand for declaring and initializing a variable
	f := "apple"
	fmt.Println(f)
}
