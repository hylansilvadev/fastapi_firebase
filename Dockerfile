FROM python:3.12.0-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY . .

RUN pip install poetry

ENV TYPE=service_account
ENV PROJECT_ID=teste-firabase-fastapi-v1
ENV PRIVATE_KEY_ID=f8a4c366e016a11e047d079817e348375935bb32
ENV PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDt5fhDObXdDt6u\n7N1O2fcJbqWVQ6E+YumMHx8Lv+mxEhrxf/KWJmVblnu3mF6nocksm9kQwsZoqIuV\nPm8YaJM+/QXpg0Qj9kQaoSm8qxXTV91rjiwR7xz5jkcrGuLL52DUvF1mT/cbVMBf\nd0xXB+FE9QJx3RlhHGFm6VDYf3rQvlKc6BdNuuj7F371wqMrEST1cbs0dooAPxak\nrUqNp21SrVDf4cpDQQdeSptq1LcaVJad3WEqx4UtPGeY+TbqWL2fMR7Sj4YdDwVL\nPLis62IcXtplm2I9M6HawUcY0RQ5QoejkNwQ2tAknqpowi3eSbJbuOlq+jlWlYiS\n0/o1WjM5AgMBAAECggEABHLT8SHfojoYdOnt+3787Rq6Eu/4UGvWFS4xzOzySELf\n6Rss5JzkMVG/j3/UaUsPsXtalEMoJaXdMlXACxNNiZR+q06ulAOTY3IXDzWdy11t\nwQigD1fK0WnVL9upWQnDGEdLcdHV+5dan45iCZCWqEzylkF9q4C125BKWDoOCGA1\nfH4duGouD73r0CVcM76oankmHuBfzdHYS/B6CvsqwABa+TFqfAOPZ8JOC/xz8+mV\n8SpRcABu9p7QeiIt6RC2L3UU38NUbPG0PmZLCbnkEntMV7cCnwfyVrGfPN873K2w\nWFmMQrUs5aJV7XIZ6gpdnU1uz17Ucz/IWccUxsBzgQKBgQD+IyXQKqNcIcHi1mV+\ngE5GlM8U0HaT9yGIt1josq34okMxTrnQUWXRrEktorV8gFKiTqbTy3pVNY85QCZf\nGU9rjJn4tDmMREN8uMIeS5rbFlGEFI5/AHKtTM2gqNdcD0XgQMnjWwPvESytRrbj\nuA4krtYXa2T2XQ221wTnB7ebWQKBgQDvpFoZfLp+I2Qd1PYV6waEUQ8mpX1Cjgur\nbR2n2AGN7h7tNp+ivvsv/Q8m59+84BVpcluBS0ZNGNUp+JhX7BAOqzyGI06FVL8r\nYjd04Sw40cBKuGEbNl5HqkPhPg4/IMjylGl336Gxl6B0dRLWz2DpwzpS0qQ8K02f\nEGziH3y64QKBgEP5MK76CJGm8c3zXFg2hzk3qh++FklDS3Pe3mf3CrM660/v56FB\ndENdmoEbSQGQ7Qk+kj6J6SGLXtCISPscsPJqO/Cae935kDd2z2z8+eFpmcoDGY38\nl6+koEc9gcS8zQrLKXSnLmkuJc3+4QINg7LqFJdVAT8n6ngiEMyecsyZAoGAHtJH\nmFGXdtO8c63JPMZunyQBy9mrA51bWN/+2XCJuqRuq9nDrF3d1q04fquB9jvn5RkF\nNdrlntLbz7sedOhypEBX13TBC5r7v2uxcEHpuyEXF0UhkCts8tCuTFD76higX7rA\n2d8UX8/9nhzUoHYpo8ctQCvBXc+/+v5U0rx0AWECgYEArKASLoRS8eU1Us7o1LyW\nFOqZbxzioZTWip454LARizOV28c12FZNyvAlLu5SHWWJIE8Jn6nM2+hUZ7cFiJjX\nSvrSTtNygB6y97kDCq0M0niiELC8sABujwpmx4EUMzmYxY0eRgWuxoByiD/ZeDuX\nkOOzvCn2a5XiIHGjEZD0/HU=\n-----END PRIVATE KEY-----\n"
ENV CLIENT_EMAIL=firebase-adminsdk-ksf9f@teste-firabase-fastapi-v1.iam.gserviceaccount.com
ENV CLIENT_ID=110446051638842051588
ENV AUTH_URI=https://accounts.google.com/o/oauth2/auth
ENV TOKEN_URI=https://oauth2.googleapis.com/token
ENV AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
ENV CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ksf9f%40teste-firabase-fastapi-v1.iam.gserviceaccount.com
ENV UNIVERSE_DOMAIN=googleapis.com

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8010
CMD ["python", "-m", "fastapi", "run", "app/main.py", "--port", "8010"]
