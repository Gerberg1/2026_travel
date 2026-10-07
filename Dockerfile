FROM python:3.9-slim AS builder
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
RUN useradd --uid 10001 --no-create-home appuser
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY --chown=10001:10001 . .
USER 10001
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000", "--debug", "--reload"]