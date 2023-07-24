FROM buildpack-deps@sha256:8f28bd087741849791b564aea220968c88f2cace4063336681cd238858e05a79

RUN apt-get update; \
	apt-get install -y --no-install-recommends \
		libseccomp-dev \
	; \
	rm -rf /var/lib/apt/lists/*