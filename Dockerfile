FROM mcr.microsoft.com/playwright/python:v1.30.0-jammy

WORKDIR /app

RUN apt-get update -y -q && \
    apt-get install -y fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

RUN pip install poetry
RUN pip install cachetools
RUN pip install pyrogram
RUN pip install asyncio
RUN pip install dotenv
# copy the source into the virtual space
COPY . /app/

# install dependencies
#RUN apt install poetry config virtualenvs.create false && poetry install

# run the program
CMD ["python", "."]
