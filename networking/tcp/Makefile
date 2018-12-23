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
DBGEX0 = $(DBGDIR)/client
DBGEX1 = $(DBGDIR)/server
DBGOBJS = $(addprefix $(DBGDIR)/, $(OBJS))
DBGCFLAGS = -ggdb -O0 -DDEBUG


# Release build settings
RELDIR = release
RELEX0 = $(RELDIR)/client
RELEX1 = $(RELDIR)/server
RELOBJS = $(addprefix $(RELDIR)/, $(OBJS))
RELCFLAGS = -O2


.PHONY: all clean debug release


# Default build
all: debug release


# Debug rules
debug: prep_debug $(DBGEX0) $(DBGEX1)

$(DBGEX0): $(filter-out $(DBGEX1).o, $(DBGOBJS))
	$(CC) -o $(DBGEX0) $^ $(LDFLAGS)

$(DBGEX1): $(filter-out $(DBGEX0).o, $(DBGOBJS))
	$(CC) -o $(DBGEX1) $^ $(LDFLAGS)

$(DBGDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(DBGCFLAGS) -o $@ $<


# Release rules
release: prep_release $(RELEX0) $(RELEX1)

$(RELEX0): $(filter-out $(RELEX1).o, $(RELOBJS))
	$(CC) -o $(RELEX0) $^ $(LDFLAGS)

$(RELEX1): $(filter-out $(RELEX0).o, $(RELOBJS))
	$(CC) -o $(RELEX1) $^ $(LDFLAGS)

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
