FROM docker.io/rockylinux:9

ENV HOME="/root"
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:${PATH}"

COPY . /tmp/app

WORKDIR /tmp/app

RUN bash ./bin/deploy.sh

WORKDIR /

RUN rm -rf /tmp/app

ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]

HEALTHCHECK --interval=5m --timeout=3s CMD /health.sh
