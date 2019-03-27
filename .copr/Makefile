PATCHES=$(wildcard *.patch)

.PHONY: srpm
srpm: tup.spec $(PATCHES)
	dnf install -y rpmdevtools rpm-build
	spectool -g -R $<
	cp $(PATCHES) ~/build/SOURCES
	rpmbuild -bs $< --define "%_srcrpmdir ${outdir}"
