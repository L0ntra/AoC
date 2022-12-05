package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"strings"
)

//go:embed input
var input string

func contains(str, char string) bool {
	for _, s := range str {
		if char == string(s) {
			return true
		}
	}
	return false
}

func findDupe(l, r string) string {
	for _, lc := range l {
		_lc := string(lc)
		if contains(r, _lc) {
			return _lc
		}
	}
	return ""
}

func findDupe2(a, b, c string) string {
	for _, ch := range a {
		_ch := string(ch)
		if contains(b, _ch) && contains(c, _ch) {
			return _ch
		}
	}
	return ""
}

func Value(c string) int {
	cv := int(c[0]) - 96
	if cv < 0 {
		cv += 58
	}
	return cv
}

func Part1() {
	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	s := 0
	for scanner.Scan() {
		line := scanner.Text()
		l := len(line) / 2
		left := line[l:]
		right := line[:l]

		s += Value(findDupe(left, right))
	}

	fmt.Println(s)
}

func Part2() {
	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	s := 0
	for scanner.Scan() {
		l1 := scanner.Text()
		scanner.Scan()
		l2 := scanner.Text()
		scanner.Scan()
		l3 := scanner.Text()

		s += Value(findDupe2(l1, l2, l3))
	}

	fmt.Println(s)
}

func main() {

	Part1()
	Part2()
}
