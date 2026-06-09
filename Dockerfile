FROM docker.io/almalinux:10 AS appbuilder

ARG BIN_DEPLOY_PREP
ARG BIN_DEPLOY_REQ
ARG CONTAINER="container"

COPY . /tmp/app

WORKDIR /tmp/app

RUN dnf clean all && dnf install -y bash
RUN bash "./${BIN_DEPLOY_PREP}" && bash "./${BIN_DEPLOY_REQ}"
RUN make build

RUN --mount=type=secret,id=env_file,target=/run/secrets/env_file \
    bash -c "\
        while IFS='=' read -r key value; do \
            if [[ ! \${key} =~ ^# && -n \${key} ]]; then \
                export \${key}=\${value}; \
            fi; \
        done < /run/secrets/env_file && make runBuild \
    "

FROM docker.io/almalinux:10 AS main

ARG USERNAME=runner
ARG USER_UID=1001
ARG USER_GID=${USER_UID}
ARG HOME_MAIN="/home/${USERNAME}"

RUN dnf clean all && dnf install -y bash

RUN userdel -r ${USERNAME} 2>/dev/null || true
RUN groupdel ${USERNAME} 2>/dev/null || true
RUN groupadd --gid ${USER_GID} ${USERNAME}
RUN useradd --uid ${USER_UID} --gid ${USER_GID} -m -d ${HOME_MAIN} ${USERNAME}
RUN mkdir -p "${HOME_MAIN}/.local/bin" \
    && chown ${USERNAME}:${USERNAME} -R ${HOME_MAIN}

ARG BIN_DEPLOY_PREP
ARG BIN_DEPLOY_REQ

COPY ./${BIN_DEPLOY_PREP} /prep.sh
COPY ./${BIN_DEPLOY_REQ} /req.sh

COPY --from=appbuilder /tmp/app/dist /tmp/build
COPY --from=appbuilder /health.sh /health.sh
COPY --from=appbuilder /entry.sh  /entry.sh

WORKDIR /tmp/build
RUN bash /prep.sh && rm /prep.sh
RUN bash /req.sh && rm /req.sh
RUN rm -rf  /tmp/build

HEALTHCHECK --interval=5m --timeout=3s CMD /health.sh

USER ${USERNAME}

WORKDIR ${HOME_MAIN}

ENTRYPOINT ["/bin/sh", "/entry.sh"]
