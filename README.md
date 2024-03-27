# Introduction
This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend. One great use case of this is to write Next.js apps that use Python AI libraries on the backend.

To manage the Python dependencies, this project utilizes Poetry, a dependency management tool. Poetry allows you to define and install the required Python packages in a virtual environment.

To get started, make sure you have Poetry installed on your system. You can find the Poetry documentation [here](https://python-poetry.org/docs/).

Once you have Poetry installed, navigate to the project directory and run the following command to create a virtual environment and install the dependencies:

# How It Works
The Python/FastAPI server is mapped into to Next.js app under `/api/`.

This is implemented using [next.config.js](https://github.com/Kamil-cr/fastapi-nextjs/blob/main/fastapi_nextjs/next.config.mjs) rewrites to map any request to `/api/:path*` to the FastAPI API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.

In production, the FastAPI server is hosted as Python serverless functions on Vercel.

# Demo
https://fastapi-nextjs-starter.vercel.app/

# Deploy Your Own
You can clone & deploy it to Vercel with one click:

# Developing Locally
You can clone & create this repo with the following command
```bash
npx create-next-app fastapi-nextjs --example "https://github.com/kamil-cr/fastapi-nextjs"
```
# Getting Started
First, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
```

Then, run the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The FastApi server will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000) – feel free to change the port in package.json (you'll also need to update it in next.config.js).

# Learn More
To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [FastAPI Documentation](https://fastapi.tiangolo.com) - learn about FastAPI features and API.
- [Poetry Documentation](https://python-poetry.org/docs/) - learn about poetry and virtual environment.

You can check out the Next.js GitHub repository - your feedback and contributions are welcome!
