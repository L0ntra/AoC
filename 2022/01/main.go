package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

//go:embed input
var input string

func main() {

	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	var elfs []int
	calorieSum := 0
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			elfs = append(elfs, calorieSum)
			calorieSum = 0
			continue
		}

		calories, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}

		calorieSum += calories
	}

	sort.Ints(elfs)

	fmt.Println("Max", elfs[len(elfs)-1])
	fmt.Println("Top3", sum(elfs[len(elfs)-3:]))
	fmt.Println(elfs)

}

func sum(slice []int) (s int) {
	for _, n := range slice {
		s += n
	}
	return
}
