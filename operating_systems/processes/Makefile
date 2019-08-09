CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -ggdb

SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)
TARGETS = main arithmetic pipeline

all : $(TARGETS)

main:	main.c

arithmetic:	arithmetic.c

pipeline: pipeline.c

ultraclean: clean
	@rm -f $(TARGETS)

clean: 
	@rm -f $(OBJS)
	@rm -f $(TARGETS)
