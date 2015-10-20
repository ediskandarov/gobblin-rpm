VERSION := 0.5.0
RELEASE ?= 1
SRPM := gobblin-$(VERSION)-$(RELEASE).el6.src.rpm
RPM := gobblin-$(VERSION)-$(RELEASE).el6.x86_64.rpm

all: $(RPM)

gobblin/.git:
	git submodule init
	git submodule update

clean: gobblin/.git
	rm -f $(RPM) $(SRPM)

gobblin/gobblin-dist.tar.gz:
	cd gobblin && ./gradlew clean build -PuseHadoop2

$(SRPM): gobblin/gobblin-dist.tar.gz
	/usr/bin/mock \
		--define "__version $(VERSION)" \
		--define "__release $(RELEASE)" \
		--resultdir=. \
		--buildsrpm \
		--spec=gobblin.spec \
		--sources=gobblin

$(RPM): $(SRPM)
	/usr/bin/mock \
		--define "__version $(VERSION)" \
		--define "__release $(RELEASE)" \
		--resultdir=. \
		--rebuild gobblin-$(VERSION)-$(RELEASE).el6.src.rpm
