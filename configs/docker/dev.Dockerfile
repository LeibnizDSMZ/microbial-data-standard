FROM docker.io/almalinux:10

ARG UV
ARG PNPM
ARG USERNAME=devu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORK_DIR=/workspace
ENV HOME_MAIN="/home/${USERNAME}"ENV PATH="${HOME_MAIN}/.local/bin:${WORK_DIR}/${UV}:${WORK_DIR}/${PNPM}:${PATH}"
ENV CONTAINER="container"
ENV HISTFILE=/dev/null
ENV HISTSIZE=0
ENV HISTFILESIZE=0

ARG NODE_VERSION
ARG BIN_DEPLOY_PREP
ARG BIN_DEPLOY_REQ
ARG BIN_DEPLOY_ENTRY_DEV
ARG BIN_DEPLOY_HEALTH

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -m -d $HOME_MAIN \
    --uid $USER_UID --gid $USER_GID $USERNAME

COPY . /tmp/app

WORKDIR /tmp/app

COPY ./${BIN_DEPLOY_ENTRY_DEV} /entry_dev.sh
COPY ./${BIN_DEPLOY_HEALTH} /health.sh

RUN dnf clean all && dnf install -y bash
RUN bash "./${BIN_DEPLOY_PREP}" && bash "./${BIN_DEPLOY_REQ}"

WORKDIR /

RUN rm -rf /tmp/app

RUN userdel -r ${USERNAME} 2>/dev/null || true
RUN groupdel ${USERNAME} 2>/dev/null || true
RUN groupadd --gid ${USER_GID} ${USERNAME}
RUN useradd --uid ${USER_UID} --gid ${USER_GID} -m -d ${HOME_MAIN} ${USERNAME}

RUN mkdir -p ${WORK_DIR} && mkdir -p /var/www &&\
    chown ${USERNAME}:${USERNAME} -R ${WORK_DIR} && \
    chown ${USERNAME}:${USERNAME} -R ${HOME_MAIN} && \
    chown ${USERNAME}:${USERNAME} -R /var/www

RUN git config --global --add safe.directory ${WORK_DIR}
RUN dnf install -y openssh openssh-clients

HEALTHCHECK --interval=60s --timeout=6s --retries=1 CMD exit 0

USER ${USERNAME}

ENTRYPOINT ["/bin/bash", "/entry_dev.sh"]
