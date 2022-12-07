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

var test string = `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`

type Object interface {
	Size() int
	GetName() string
	Build(scanner *bufio.Scanner)
	Print(indent string)
	SumLTE(maxSize int) int
	Find(minSize int) []Object
}

var _ Object = &Directory{}

type Directory struct {
	Objects []Object
	Name    string
}

func (d *Directory) Find(minSize int) []Object {
	found := make([]Object, 0)
	if d.Size() >= minSize {
		found = append(found, d)
	}
	for _, object := range d.Objects {
		found = append(found, object.Find(minSize)...)
	}
	return found
}

func (d *Directory) SumLTE(maxSize int) int {
	sum := 0
	if d.Size() <= maxSize {
		sum += d.Size()
	}

	for _, object := range d.Objects {
		sum += object.SumLTE(maxSize)
	}
	return sum
}

func (d *Directory) Print(indent string) {
	fmt.Println(indent + "- " + d.Name)
	indent += "  "
	for _, object := range d.Objects {
		object.Print(indent)
	}
}

func (d *Directory) Size() int {
	totalSize := 0
	for _, object := range d.Objects {
		totalSize += object.Size()
	}
	return totalSize
}

func (d *Directory) GetName() string {
	return d.Name
}

func (d *Directory) Build(scanner *bufio.Scanner) {
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, " ")
		switch parts[0] {
		case "$":
			if parts[1] == "ls" {
				continue
			}
			if parts[2] == ".." {
				return
			}
			for _, object := range d.Objects {
				if object.GetName() == parts[2] {
					object.Build(scanner)
				}
			}

		case "dir": // Process Directory
			d.Objects = append(d.Objects, &Directory{Name: parts[1]})
		default: // Process File
			size, err := strconv.Atoi(parts[0])
			if err != nil {
				panic(err.Error())
			}
			d.Objects = append(d.Objects, &File{size: size, Name: parts[1]})
		}
	}
}

var _ Object = &File{}

type File struct {
	size int
	Name string
}

func (f *File) Find(_ int) []Object {
	return nil
}

func (f *File) SumLTE(_ int) int {
	return 0
}

func (f *File) Print(indent string) {
	fmt.Printf("%s%s size=%d \n", indent, f.Name, f.Size())
}

func (f *File) Size() int {
	return f.size
}

func (f *File) GetName() string {
	return f.Name
}

func (f *File) Build(_ *bufio.Scanner) {
	panic("File Not Dir")
}

func BuildFileSystem(s string) Object {
	reader := strings.NewReader(s)
	scanner := bufio.NewScanner(reader)

	root := &Directory{Name: "/"}
	scanner.Scan() // Skip the first command which is `cd /`

	root.Build(scanner)

	return root
}

func Part1(s string) {
	root := BuildFileSystem(s)

	fmt.Println(root.SumLTE(100000))
}

func Part2(s string) {
	root := BuildFileSystem(s)

	maxDiskSpace := 70000000
	upgradeDiskSpace := 30000000
	usedDiskSpace := root.Size()

	freeSpace := maxDiskSpace - usedDiskSpace
	minSpaceToFree := upgradeDiskSpace - freeSpace

	found := root.Find(minSpaceToFree)
	smallest := usedDiskSpace
	for _, f := range found {
		size := f.Size()
		if size < smallest {
			smallest = size
		}
	}
	fmt.Println(smallest)

}

func main() {
	Part1(input)
	Part2(input)
}
