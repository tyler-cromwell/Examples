# Compiler flags
CC      = gcc
CFLAGS  = -Wall -Wextra -std=c11
LDFLAGS =


# Files
SRCS = client.c \
       server.c \
       utils.c
OBJS = $(SRCS:.c=.o)


# Debug build settings
DBGDIR = debug
DBGCLNT = $(DBGDIR)/client
DBGSERV = $(DBGDIR)/server
DBGOBJS = $(addprefix $(DBGDIR)/, $(OBJS))
DBGCFLAGS = -ggdb -O0 -DDEBUG


# Release build settings
RELDIR = release
RELCLNT = $(RELDIR)/client
RELSERV = $(RELDIR)/server
RELOBJS = $(addprefix $(RELDIR)/, $(OBJS))
RELCFLAGS = -O2


.PHONY: all clean debug release


# Default build
all: debug release


# Debug rules
debug: prep_debug $(DBGCLNT) $(DBGSERV)

$(DBGCLNT): $(filter-out $(DBGSERV).o, $(DBGOBJS))
	$(CC) -o $(DBGCLNT) $^ $(LDFLAGS)

$(DBGSERV): $(filter-out $(DBGCLNT).o, $(DBGOBJS))
	$(CC) -o $(DBGSERV) $^ $(LDFLAGS)

$(DBGDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(DBGCFLAGS) -o $@ $<


# Release rules
release: prep_release $(RELCLNT) $(RELSERV)

$(RELCLNT): $(filter-out $(RELSERV).o, $(RELOBJS))
	$(CC) -o $(RELCLNT) $^ $(LDFLAGS)

$(RELSERV): $(filter-out $(RELCLNT).o, $(RELOBJS))
	$(CC) -o $(RELSERV) $^ $(LDFLAGS)

$(RELDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(RELCFLAGS) -o $@ $<


# Other rules
prep_debug:
	@mkdir -p $(DBGDIR)/

prep_release:
	@mkdir -p $(RELDIR)/

clean:
	@rm -rf $(DBGDIR)/
	@rm -rf $(RELDIR)/
