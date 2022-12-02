package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"strings"
)

//go:embed input
var input string

const (
	win  = 6
	lose = 0
	draw = 3
)

type Shoot interface {
	Value() int
	Compare(shoot Shoot) int
	Outcome(shoot Shoot) int
}

// Lose
type Rock struct{}

func (r Rock) Value() int { return 1 }

func (r Rock) Compare(shoot Shoot) int {
	switch shoot.Value() {
	case 1:
		return draw
	case 2:
		return lose
	default:
		return win
	}
}

func (r Rock) Outcome(shoot Shoot) int {
	switch shoot.Value() {
	case 1:
		return lose + Scissors{}.Value()
	case 2:
		return draw + Rock{}.Value()
	default:
		return win + Paper{}.Value()
	}
}

// Draw
type Paper struct{}

func (p Paper) Value() int { return 2 }

func (p Paper) Compare(shoot Shoot) int {
	switch shoot.Value() {
	case 1:
		return win
	case 2:
		return draw
	default:
		return lose
	}
}

func (p Paper) Outcome(shoot Shoot) int {
	switch shoot.Value() {
	case 1:
		return lose + Rock{}.Value()
	case 2:
		return draw + Paper{}.Value()
	default:
		return win + Scissors{}.Value()
	}
}

// Win
type Scissors struct{}

func (s Scissors) Value() int { return 3 }

func (s Scissors) Compare(shoot Shoot) int {
	switch shoot.Value() {
	case 1:
		return lose
	case 2:
		return win
	default:
		return draw
	}
}

func (Scissors) Outcome(shoot Shoot) int {
	switch shoot.Value() {
	case 1:
		return lose + Paper{}.Value()
	case 2:
		return draw + Scissors{}.Value()
	default:
		return win + Rock{}.Value()
	}
}

type Game struct {
	Opponent Shoot
	Me       Shoot
}

func (g Game) Play() int {
	return g.Me.Compare(g.Opponent) + g.Me.Value()
}

func (g Game) Play2() int {
	return g.Opponent.Outcome(g.Me)
}

func ToShoot(c rune) Shoot {
	switch c {
	case 'A', 'X':
		return Rock{}
	case 'B', 'Y':
		return Paper{}
	default:
		return Scissors{}
	}
}

func main() {

	reader := strings.NewReader(input)
	scanner := bufio.NewScanner(reader)

	var games []Game
	for scanner.Scan() {
		line := scanner.Text()
		games = append(games, Game{
			Opponent: ToShoot(rune(line[0])),
			Me:       ToShoot(rune(line[2])),
		})
	}

	total := 0
	total2 := 0
	for _, game := range games {
		total += game.Play()
		total2 += game.Play2()
	}
	fmt.Println(total)
	fmt.Println(total2)
}
