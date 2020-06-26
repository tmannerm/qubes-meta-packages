install-vm-debian:
	install -d $(DESTDIR)/etc/apt/sources.list.d
	sed -e "s/@DIST@/`lsb_release -cs`/" qubes-contrib-r3.2.list.in \
		> $(DESTDIR)/etc/apt/sources.list.d/qubes-contrib-r3.2.list
	install -d $(DESTDIR)/etc/apt/trusted.gpg.d
	gpg --no-default-keyring --keyring \
		$(DESTDIR)/etc/apt/trusted.gpg.d/qubes-3-contrib-keyring.gpg \
		--import qubes-contrib-debian-3.asc

install-vm-fedora: install-fedora
	install -d $(DESTDIR)/etc/yum.repos.d
	install -m 0644 qubes-contrib-vm-r3.2.repo $(DESTDIR)/etc/yum.repos.d

install-vm-opensuse: install-opensuse
	install -d $(DESTDIR)/etc/yum.repos.d
	install -m 0644 qubes-contrib-vm-r3.2.repo-opensuse $(DESTDIR)/etc/yum.repos.d/qubes-contrib-vm-r3.2.repo

install-fedora:
	install -d $(DESTDIR)/etc/pki/rpm-gpg/
	install -m 0644 qubes-contrib-fedora-3.asc \
		$(DESTDIR)/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3-contrib
	ln -s RPM-GPG-KEY-qubes-3-contrib \
		$(DESTDIR)/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3.2-contrib
install-opensuse:
	install -d $(DESTDIR)/etc/pki/rpm-gpg/
	# Empty for now
	touch $(DESTDIR)/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3-contrib-opensuse
	ln -s RPM-GPG-KEY-qubes-3-contrib-opensuse \
		$(DESTDIR)/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3.2-contrib-opensuse
