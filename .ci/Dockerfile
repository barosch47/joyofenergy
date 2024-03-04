FROM python:3.11-slim as builder
RUN useradd -rm -d /home/user -u 1001 user && \
    mkdir -p /home/user/app && \
    chown -R user /home/user/app
USER user

WORKDIR /home/user/

COPY app.py poetry.lock pyproject.toml README.md app/
COPY src/ app/src/

WORKDIR /home/user/app

RUN pip install poetry==1.8.1 --user --no-cache-dir && \
    export PATH="${PATH}":"${HOME}"/.local/bin && \
    poetry config virtualenvs.in-project true && \
    poetry install --only main

FROM python:3.11-alpine
RUN addgroup -S appgroup && adduser -S user -G appgroup && \
    mkdir -p /home/user/app && \
    chown -R user /home/user/app
USER user

COPY --from=builder /home/user/app/ /home/user/app/
ENV PATH=/home/user/app/.venv/bin:$PATH
ENV PYTHONUNBUFFERED 1

WORKDIR /home/user/app

CMD ["uvicorn", "joy.main:app", "--root-path", " /api" , "--host", "0.0.0.0", "--port", "8020"]