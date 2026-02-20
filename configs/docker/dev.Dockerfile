FROM docker.io/almalinux:10

ARG UV
ARG USERNAME=devu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORK_DIR=/workspace
ENV HOME="/home/${USERNAME}"
ENV PATH="${HOME}/.local/bin:${WORK_DIR}/${UV}:${PATH}"
ENV CONTAINER="container"

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -m -d $HOME \
    --uid $USER_UID --gid $USER_GID $USERNAME

COPY . /tmp/app

WORKDIR /tmp/app

RUN bash ./bin/deploy/prep.sh && bash ./bin/deploy/req.sh

WORKDIR /

RUN rm -rf /tmp/app

RUN git config --global --add safe.directory $WORK_DIR

RUN mkdir -p $WORK_DIR && \
    chown $USERNAME:$USERNAME -R $WORK_DIR && \
    mkdir -p "${HOME}/.local/bin" && \
    chown $USERNAME:$USERNAME -R $HOME

USER $USERNAME

ENTRYPOINT ["sleep", "infinity"]
