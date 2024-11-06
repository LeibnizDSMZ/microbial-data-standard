FROM docker.io/rockylinux:9

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORK_DIR=/workspace
ENV HOME="/home/${USERNAME}"
ENV PATH="$HOME/.local/bin:$PATH"

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -m -d $HOME \
    --uid $USER_UID --gid $USER_GID $USERNAME

ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:${PATH}"

COPY . /tmp/app

WORKDIR /tmp/app

RUN bash ./bin/deploy/prep.sh && bash ./bin/deploy/req.sh

WORKDIR /

RUN rm -rf /tmp/app

RUN git config --global --add safe.directory $WORK_DIR

RUN mkdir -p $WORK_DIR && \
    chown $USERNAME:$USERNAME -R $WORK_DIR && \
    chown $USERNAME:$USERNAME -R $HOME

USER $USERNAME

ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
