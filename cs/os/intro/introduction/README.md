# About OS

> [제2장] 운영체제 개요

[Project Card](https://github.com/Jennas-Lee/cloud-skills-study/projects/1#card-78684446)

## Virtualizing the CPU

### Single Processor

**Compile**

```bash
gcc -o cpu.o cpu.c -Wall
```

**Execute**

```bash
./cpu.o "A"
```

### Multi Processor

**Compile**

```bash
gcc -o cpu.o cpu.c -Wall
```

**Execute**

```bash
./cpu.o A & ./cpu.o B & ./cpu.o C & ./cpu.o D
```

## Virtualizing Memory

### Single

**Compile**

```bash
gcc -o mem.o mem.c -Wall
```

**Execute**

```bash
./mem.o
```

### Multiple

**Compile**

```bash
gcc -o mem.o mem.c -Wall
```

**Execute**

```bash
./mem.o & ./mem.o
```

## Multi Thread

### Loops 1000

**Compile**

```bash
gcc -o thread.o thread.c -Wall -lpthread
```

**Execute**

```bash
./thread.o 1000
```

### Loops 100000

**Compile**

```bash
gcc -o thread.o thread.c -Wall -lpthread
```

**Execute**

```bash
./thread.o 100000
```

## Input/Output

**Compile**

```bash
gcc -o io.o io.c -Wall
```

**Execute**

```bash
./io.o
cat /tmp/file
```
