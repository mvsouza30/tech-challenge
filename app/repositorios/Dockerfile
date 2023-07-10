FROM postgres:latest
COPY init.sql /docker-entrypoint-initdb.d/
RUN su - postgres
ENV POSTGRES_HOST=db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=C0n3ct4
ENV POSTGRES_DB=qtop_db
ENV POSTGRES_PORT=5432

