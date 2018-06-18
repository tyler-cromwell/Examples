CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -ggdb

SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)
TARGETS = server client

all : $(TARGETS)

server:	server.c

client:	client.c

ultraclean: clean
	@rm -f $(TARGETS)

clean: 
	@rm -f $(OBJS)
	@rm -f $(TARGETS)
