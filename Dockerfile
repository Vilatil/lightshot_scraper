FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

ARG DB_HOST
ARG DB_USER
ARG DB_DATABASE
ARG DB_PASSWORD

ENV DB_HOST=${DB_HOST}
ENV DB_USER=${DB_USER}
ENV DB_DATABASE=${DB_DATABASE}
ENV DB_PASSWORD=${DB_PASSWORD}

WORKDIR /lightshot_scraper
COPY pyproject.toml uv.lock .
RUN uv sync --locked --no-dev

FROM alpine:3.22
WORKDIR /lightshot_scraper

COPY . .
COPY --from=builder /lightshot_scraper/.venv /lightshot_scraper/.venv
ENV PATH="/lightshot_scraper/.venv/bin:$PATH"
EXPOSE 3306
CMD ["python", "main.py"]
