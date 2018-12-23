# Compiler flags
CC      = gcc
CFLAGS  = -Wall -Wextra -std=c11
AS      = nasm
AFLAGS  = -f elf64
LDFLAGS =


# Files
CSRCS = lib.c
COBJS = $(CSRCS:.c=.o)
ASRCS = main.asm
AOBJS = $(ASRCS:.asm=.o)
EXE   = main


# Debug build settings
DBGDIR    = debug
DBGEXE    = $(DBGDIR)/$(EXE)
DBGCOBJS  = $(addprefix $(DBGDIR)/, $(COBJS))
DBGCFLAGS = -ggdb -O0 -DDEBUG
DBGAOBJS  = $(addprefix $(DBGDIR)/, $(AOBJS))
DBGAFLAGS = -g -F dwarf


# Release build settings
RELDIR    = release
RELEXE    = $(RELDIR)/$(EXE)
RELCOBJS  = $(addprefix $(RELDIR)/, $(COBJS))
RELCFLAGS = -O2
RELAOBJS  = $(addprefix $(RELDIR)/, $(AOBJS))
RELAFLAGS =


.PHONY: all clean debug release


# Default build
all: debug release


# Debug rules
debug: prep_debug $(DBGEXE)

$(DBGEXE): $(DBGCOBJS) $(DBGAOBJS)
	$(CC) -o $(DBGEXE) $^ $(LDFLAGS)

$(DBGDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(DBGCFLAGS) -o $@ $<

$(DBGDIR)/%.o: %.asm
	$(AS) -o $@ $< $(AFLAGS) $(DBGAFLAGS)


# Release rules
release: prep_release $(RELEXE)

$(RELEXE): $(RELCOBJS) $(RELAOBJS)
	$(CC) -o $(RELEXE) $^ $(LDFLAGS)

$(RELDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(RELCFLAGS) -o $@ $<

$(RELDIR)/%.o: %.asm
	$(AS) -o $@ $< $(AFLAGS) $(RELAFLAGS)


# Other rules
prep_debug:
	@mkdir -p $(DBGDIR)/

prep_release:
	@mkdir -p $(RELDIR)/

clean:
	@rm -rf $(DBGDIR)/
	@rm -rf $(RELDIR)/
