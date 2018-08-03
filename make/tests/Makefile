# Variables
CC      = gcc
CFLAGS  = -Wall -Wextra -std=c11 -pipe -O0 -ggdb -pg -D DEBUG
IFLAGS  =


.PHONY: all clean

# Default build
EXES = test1 \
       test2

all: $(EXES)

test1: test1.o
	$(CC) -o $@ $<

test2: test2.o
	$(CC) -o $@ $<

%.o: %.c
	$(CC) -c $(CFLAGS) $(IFLAGS) -o $@ $<

# Other rules
clean:
	rm -rf $(EXES)
	rm -rf *.o
	rm -rf gmon.out
