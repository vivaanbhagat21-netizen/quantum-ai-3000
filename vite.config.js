import { defineConfig, loadEnv } from 'vite'
import { quantumApiPlugin } from './server/middleware.js'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  if (env.OPENAI_API_KEY) process.env.OPENAI_API_KEY = env.OPENAI_API_KEY
  if (env.VITE_OPENAI_API_KEY) process.env.VITE_OPENAI_API_KEY = env.VITE_OPENAI_API_KEY

  return {
    plugins: [quantumApiPlugin()],
    server: {
      port: 5174,
      strictPort: true,
    },
  }
})
