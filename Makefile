RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

GIT_VERSION = $(shell git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null || echo git-`git rev-parse --short HEAD`)
VERSION=$(shell awk '/Version:/ { print $$2; }' clasp-lmount-server.spec)

all:
	mkdir -p build
	cp lmountd lmountd.bak
	awk '{sub("SOFTWARE_VERSION = .*$$","SOFTWARE_VERSION = \"$(VERSION) ($(GIT_VERSION))\""); print $0}' lmountd.bak > lmountd
	${RPMBUILD} -ba clasp-lmount-server.spec
	${RPMBUILD} -ba superwasp-lmount-server.spec
	${RPMBUILD} -ba halfmetre-lmount-server.spec
	${RPMBUILD} -ba observatory-lmount-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-lmount.spec
	mv build/noarch/*.rpm .
	rm -rf build
	mv lmountd.bak lmountd
