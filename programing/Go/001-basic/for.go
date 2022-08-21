package main

import "fmt"

func main() {
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	for {
		fmt.Println("loop")
		break // 没有就无限下去
	}

	for f := 0; f < 100; f++ {
		if f%2 == 0 {
			continue
		}
		fmt.Println(f)
	}

}
