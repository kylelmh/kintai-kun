import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/static/static/',
  server: {
    host: '0.0.0.0'
  },
  build: {
    manifest: true,
    rollupOptions: {
      input: {asset: '/vite/src/main.js'}
    },
    outDir: '/vite/dist'
  }
})
