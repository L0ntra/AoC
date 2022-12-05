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

func parseStack(s []string) [][]string {
	maxLen := 0
	for _, s2 := range s {
		if len(s2) > maxLen {
			maxLen = len(s2)
		}
	}

	/* transpose the stack in reverse order
	    a b c     x 1 a
		1 2 3  => y 2 b
		x y z     z 3 c
	*/
	transposed := make([][]string, maxLen)
	for _, row := range s {
		for i, r := range row {
			sr := string(r)
			// Drop extra characters
			if sr == "[" || sr == "]" || sr == " " {
				continue
			}
			// prepend, to revers the normal transposed order
			transposed[i] = append([]string{sr}, transposed[i]...)
		}
	}

	out := make([][]string, 0)
	for _, t := range transposed {
		// Drop empty rows
		if len(t) == 0 {
			continue
		}

		out = append(out, t[1:])
	}
	return out
}

func parseCommand(command string) (int, int, int) {
	parts := strings.Split(command, " ")
	n, _ := strconv.Atoi(parts[1])
	from, _ := strconv.Atoi(parts[3])
	to, _ := strconv.Atoi(parts[5])
	return n, from - 1, to - 1
}

func Part1() {
	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	rawStacks := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		rawStacks = append(rawStacks, line)
	}

	stacks := parseStack(rawStacks)

	for scanner.Scan() {
		line := scanner.Text()
		n, from, to := parseCommand(line)

		for i := 0; i < n; i++ {
			// Pop
			x := stacks[from][len(stacks[from])-1]
			stacks[from] = stacks[from][:len(stacks[from])-1]
			stacks[to] = append(stacks[to], x)
		}
	}

	for _, stack := range stacks {
		if len(stack) == 0 {
			fmt.Print(" ")
			continue
		}
		fmt.Print(stack[len(stack)-1])
	}
	fmt.Println()
}

func Part2() {
	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	rawStacks := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		rawStacks = append(rawStacks, line)
	}

	stacks := parseStack(rawStacks)

	for scanner.Scan() {
		line := scanner.Text()
		n, from, to := parseCommand(line)

		x := stacks[from][len(stacks[from])-n:]
		stacks[from] = stacks[from][:len(stacks[from])-n]
		stacks[to] = append(stacks[to], x...)
	}

	for _, stack := range stacks {
		if len(stack) == 0 {
			fmt.Print(" ")
			continue
		}
		fmt.Print(stack[len(stack)-1])
	}
	fmt.Println()
}

func main() {
	Part1()
	Part2()
}
