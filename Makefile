prefix = /usr/local

all: demo_libuv

demo_libuv: demo_libuv.c
	@echo "CFLAGS=$(CFLAGS)" | \
		fold -s -w 70 | \
		sed -e 's/^/# /'
	$(CC) $(CPPFLAGS) $(CFLAGS) $(LDCFLAGS) -luv -o $@ $^

install: demo_libuv
	# Outsourced to debian/install
	install -D demo_libuv \
		$(DESTDIR)$(prefix)/bin/demo_libuv

clean:
	-rm -f demo_libuv

distclean: clean

uninstall:
	-rm -f $(DESTDIR)$(prefix)/bin/demo_libuv
	-rm -f $(DESTDIR)$(prefix)/bin/greet.sh

.PHONY: all install clean distclean uninstall
