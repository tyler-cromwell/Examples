# Compiler flags
CC      = gcc
CFLAGS  = -Wall -Wextra -std=c11
LDFLAGS = -lpthread


# Files
SRCS = sync.c
OBJS = $(SRCS:.c=.o)
EXE  = sync


# Debug build settings
DBGDIR = debug
DBGEXE = $(DBGDIR)/$(EXE)
DBGOBJS = $(addprefix $(DBGDIR)/, $(OBJS))
DBGCFLAGS = -ggdb -O0 -DDEBUG


# Release build settings
RELDIR = release
RELEXE = $(RELDIR)/$(EXE)
RELOBJS = $(addprefix $(RELDIR)/, $(OBJS))
RELCFLAGS = -O3


.PHONY: all clean debug release


# Default build
all: debug release


# Debug rules
debug: prep_debug $(DBGEXE)

$(DBGEXE): $(DBGOBJS)
	$(CC) -o $(DBGEXE) $^ $(LDFLAGS)

$(DBGDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(DBGCFLAGS) -o $@ $<


# Release rules
release: prep_release $(RELEXE)

$(RELEXE): $(RELOBJS)
	$(CC) -o $(RELEXE) $^ $(LDFLAGS)

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
