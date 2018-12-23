# Compiler flags
AR      = ar
CC      = gcc
CFLAGS  = -Wall -Wextra -std=c11 -fPIC -pipe
IFLAGS  =
LDFLAGS = -shared


# Files
NAME = test
SRCS = test.c
OBJS = $(SRCS:.c=.o)
HEADER = $(NAME).h
TARGET = lib$(NAME).so
ARCHIVE = lib$(NAME).a


# Directories
PREFIX = $(DESTDIR)/usr
LIBDIR = $(PREFIX)/lib
INCDIR = $(PREFIX)/include/$(NAME)


# Debug build settings
DBGDIR = debug
DBGSLIB = $(DBGDIR)/$(TARGET)
DBGALIB = $(DBGDIR)/$(ARCHIVE)
DBGOBJS = $(addprefix $(DBGDIR)/, $(OBJS))
DBGCFLAGS = -O0 -ggdb -pg -D DEBUG


# Release build settings
RELDIR = release
RELSLIB = $(RELDIR)/$(TARGET)
RELALIB = $(RELDIR)/$(ARCHIVE)
RELOBJS = $(addprefix $(RELDIR)/, $(OBJS))
RELCFLAGS = -O2


.PHONY: all clean debug release

# Default build
all: debug release


# Debug rules
debug: prep_debug $(DBGSLIB) $(DBGALIB)

$(DBGSLIB): $(DBGOBJS)
	$(CC) -o $(DBGSLIB) $^ $(LDFLAGS)

$(DBGALIB): $(DBGOBJS)
	$(AR) -r $(DBGDIR)/$(ARCHIVE) $^

$(DBGDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(DBGCFLAGS) -o $@ $<


# Release rules
install: release
	install -D $(RELDIR)/$(TARGET) $(LIBDIR)/$(TARGET)
	install -D $(HEADER) $(INCDIR)/$(HEADER)
	ldconfig

install-strip: release
	install -D -s $(RELDIR)/$(TARGET) $(LIBDIR)/$(TARGET)
	install -D $(HEADER) $(INCDIR)/$(HEADER)
	ldconfig

release: prep_release $(RELSLIB) $(RELALIB)

$(RELSLIB): $(RELOBJS)
	$(CC) -o $(RELSLIB) $^ $(LDFLAGS)

$(RELALIB): $(RELOBJS)
	$(AR) -r $(RELDIR)/$(ARCHIVE) $^

$(RELDIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $(RELCFLAGS) -o $@ $<


# Other rules
prep_debug:
	mkdir -p $(DBGDIR)/

prep_release:
	mkdir -p $(RELDIR)/

clean:
	rm -rf $(DBGDIR)/
	rm -rf $(RELDIR)/

uninstall:
	rm -rf $(LIBDIR)/$(TARGET)
	rm -rf $(INCDIR)/$(HEADER)
	rmdir $(INCDIR)
	ldconfig
