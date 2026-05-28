import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        chatbot: 'chatbot.html',
        document: 'document.html',
        rights: 'rights.html',
      }
    }
  }
})