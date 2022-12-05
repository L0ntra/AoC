package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed input
var input string

type Assignment struct {
	Start int
	End   int
}

func (a Assignment) FullyContains(b Assignment) bool {
	return a.Start <= b.Start && a.End >= b.End
}

// A starts and ends before B?
func (a Assignment) Before(b Assignment) bool {
	return a.Start < b.Start && a.End < b.Start
}

func NewAssignments(str string) (Assignment, Assignment) {
	fx := func(s string) int { i, _ := strconv.Atoi(s); return i }

	strs := strings.Split(str, ",")

	a1 := strings.Split(strs[0], "-")
	a2 := strings.Split(strs[1], "-")

	return Assignment{
			Start: fx(a1[0]),
			End:   fx(a1[1]),
		}, Assignment{
			Start: fx(a2[0]),
			End:   fx(a2[1]),
		}
}

func Part1() {
	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	s := 0
	for scanner.Scan() {
		line := scanner.Text()

		a1, a2 := NewAssignments(line)
		if a1.FullyContains(a2) || a2.FullyContains(a1) {
			s += 1
		}
	}

	fmt.Println(s)
}

func Part2() {
	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	s := 0
	for scanner.Scan() {
		line := scanner.Text()

		a1, a2 := NewAssignments(line)
		if !(a1.Before(a2) || a2.Before(a1)) {
			s += 1
		}
	}

	fmt.Println(s)
}

func main() {

	Part1()
	Part2()
}
